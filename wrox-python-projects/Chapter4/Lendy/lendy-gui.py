import tkinter.tix as tix
import tkinter.messagebox as mb
import optionsdialog as od
import lendydata as data
import os

class LendingLibrary:
    def __init__(self, root):
        self.isDirty = False
        self.top = root
        root['menu'] = self.buildMenus(root)
        mainWin = self.buildNoteBook(root)
        mainWin.pack(fill='both', expand=True)
        self.top.protocol('WM_DELETE_WINDOW', self.evClose)
        self.top.title('Lending Library')
        data.initDB()   # use default file
        self.items = data.get_items()
        self.members = data.get_members()
        self.populateItemList()
        self.populateMemberList()
        
    def buildMenus(self, top):
        menus= (
           ("Item", (("New",    self.evNewItem),
                     ("Edit",   self.evEditItem),
                     ("Delete", self.evDeleteItem),
                     )),
           ("Member", (("New",   self.evNewMember),
                       ("Edit",  self.evEditMember),
                       ("Delete",self.evDeleteMember),
                       )),
           ("Help", (("Help",  self.evHelp),
                     ("About", lambda : mb.showinfo(
                               "Help About",
                               "Lender application\nAuthor: Alan Gauld""")
                     ))))

        self.menubar = tix.Menu(top)
        for menu in menus:
            m = tix.Menu(top)
            for item in menu[1]:
                m.add_command(label=item[0], command=item[1])
            self.menubar.add_cascade(label=menu[0], menu=m)

        return self.menubar

    def buildNoteBook(self, top):
        mono_font = self.getMonoFont() 
        nb = tix.NoteBook(top)

        nb.add("itemPage",label="Items", 
               raisecmd=lambda pg="item": self.evPage(pg))
        fr = tix.Frame(nb.subwidget("itemPage"))
        self.itemFmt = "{:15} {:15} {:10} ${:<8} {:12}"
        tix.Label(fr, font=mono_font,
                  text=self.itemFmt.format("Name","Description",
                                           "Owner","Price",
                                           "Condition")).pack(anchor='w')
        slb = tix.ScrolledListBox(fr, width=500, height=200)
        slb.pack(fill='both', expand=True)
        fr.pack(fill='both', expand=True)
        self.itemList = slb.subwidget("listbox")
        self.itemList.configure(font=mono_font, bg='white')
        self.itemList.bind('<Double-1>', self.evEditItem)
        
        nb.add("memberPage",label="Members", 
               raisecmd=lambda pg="member": self.evPage(pg))
        fr = tix.Frame(nb.subwidget("memberPage"))
        self.memberFmt = "{:<15} {:<40}"
        tix.Label(fr, font=mono_font,
                  text=self.memberFmt.format("Name","Email Address")).pack(anchor='w')
        slb = tix.ScrolledListBox(fr, width=40, height=20)
        slb.pack(fill='both', expand=True)
        fr.pack(fill='both', expand=True)
        self.memberList = slb.subwidget("listbox")
        self.memberList.configure(font=mono_font, bg='white')
        self.memberList.bind('<Double-1>', self.evEditMember)
        
        return nb

    def getMonoFont(self):
        if os.name == 'nt':
           return ('courier','10','')
        else: 
           return ('mono','10','')

    def populateItemList(self):
        self.itemList.delete('0','end')
        for item in self.items:
            item = list(item[1:])
            item[2] = data.get_member_name(item[2])
            self.itemList.insert('end', self.itemFmt.format(*item))

    def populateMemberList(self):
        self.memberList.delete('0','end')
        for mbr in self.members:
            self.memberList.insert('end', self.memberFmt.format(*mbr[1:]))
    
    def evClose(self, event=None):
        data.closeDB()
        self.top.quit()
        
    ##### notebook event handler #####
    def evPage(self, page):
        if page=='item':
            self.menubar.entryconfigure('Item', state='active')
            self.menubar.entryconfigure('Member', state='disabled')
        if page=='member':
            self.menubar.entryconfigure('Item', state='disabled')
            self.menubar.entryconfigure('Member', state='active')
 
    ######### Item Event Handlers #######
    def evNewItem(self):
        dlg = od.OptionsDialog(top,(
                               ["Name",        "" ],
                               ["Description", "" ],
                               ["Owner",       "" ],
                               ["Price",       "" ],
                               ["Condition",   "" ]))
        if dlg.changed:
            ownerID = self.get_member_id(dlg.options[2][1])
            data.insert_item(dlg.options[0][1],dlg.options[1][1],
                             ownerID,     int(dlg.options[3][1]),
                             dlg.options[4][1])
            self.items = data.get_items()
            self.populateItemList()

    def evEditItem(self, event=None):
        # get selected member
        indices = self.itemList.curselection()
        index = int(indices[0]) if indices else 0
        item = self.items[index]
        ownerID = item[3]
        ownerName = data.get_member_name(ownerID)
        dlg = od.OptionsDialog(top,(
                               ["Name",        item[1] ],
                               ["Description", item[2] ],
                               ["Owner",     ownerName ],
                               ["Price",       item[4] ],
                               ["Condition",   item[5] ]))
        if dlg.changed:
            if dlg.options[2][1] != ownerName:  # its changed
                ownerID = self.get_member_id(dlg.options[2][1])
            data.update_item(item[0],dlg.options[0][1],dlg.options[1][1],
                                     ownerID,     int(dlg.options[3][1]),
                                     dlg.options[4][1])
            self.items = data.get_items()
            self.populateItemList()

    def evDeleteItem(self):
        indices = self.itemList.curselection()
        index = int(indices[0]) if indices else 0
        item = self.items[index]
        data.delete_item(item[0])
        self.items = data.get_items()
        self.populateItemList()
 
    # Ideally should use a combo box in options dialog.
    # this gives potential error if more than one member with same name
    def get_member_id(self, name):
        for member in self.members:
            if member[1] == name:
                return member[0]

    ######### Member Event Handlers #######
    def evNewMember(self):
        dlg = od.OptionsDialog(top,(
                               ["Name",""],
                               ["Email",""]))
        if dlg.changed:
           data.update_member(None,dlg.options[0][1],dlg.options[1][1])
           self.members = data.get_members()
           self.populateMemberList()

    def evEditMember(self, event=None):
        indices = self.memberList.curselection()
        index = int(indices[0]) if indices else 0
        mbr = self.members[index]
        dlg = od.OptionsDialog(top,(
                               ["Name",mbr[1]],
                               ["Email",mbr[2]]))
        if dlg.changed:
           data.update_member(mbr[0],dlg.options[0][1],dlg.options[1][1])
           self.members = data.get_members()
           self.populateMemberList()

    def evDeleteMember(self):
        indices = self.memberList.curselection()
        index = int(indices[0]) if indices else 0
        mbr = self.members[index]
        data.delete_member(mbr[0])
        self.members = data.get_members()
        self.populateMemberList()

    #### Help event handler #
    def evHelp(self):
        mb.showinfo("Help", """
Lending Library Application

Item->New:  
      Create a new item in the library
Item->Edit:
      Modify the attributes of the
      selected item (default is first)
Item->Delete:
      Delete selected item (no default)

Member->New: 
      Add a member to the library
Member->Edit: 
      Modify selected members data 
      (default is first)
Member->Delete: 
      Delete selected member (no default)

Help->Help: 
      Display this screen
Help->About: 
      About the program.""")

if __name__ == "__main__":
    top = tix.Tk()
    app = LendingLibrary(top)
    top.mainloop()
