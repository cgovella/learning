import tkinter as tk
import tkinter.messagebox as mb
import oxo_logic

top = tk.Tk()

def buildMenu(parent):
    menus = (
        ("File" , ( ("New", evNew),
                    ("Resume", evResume),
                    ("Save", evSave),
                    ("Exit", evExit))),
        ("Help", (("Help", evHelp),
                      ("About", evAbout)))
        )
        
    menubar = tk.Menu(parent)
    for menu in menus:
        m = tk.Menu(parent)
        for item in menu[1]:
            m.add_command(label=item[0], command=item[1])
        menubar.add_cascade(label=menu[0], menu=m)

    return menubar

def dummy():
    mb.showinfo("Dummy", "Event to be done")


evNew = dummy
evResume = dummy
evSave = dummy
evExit = top.quit
evHelp = dummy
evAbout = dummy


def evClick(row,col): 
	mb.showinfo("cells", "Cell clicked: row:{}, col:{}".format(row,col))
	
def buildBoard(parent):
	outer = tk.Frame(parent, border=2, relief="sunken")
	inner = tk.Frame(outer)
	inner.pack()
	
	for row in range(3):
		for col in range(3):
			cell = tk.Button(inner, text=" ",  width="5", height="2", 
			                        command=lambda r=row, c=col : evClick(r,c) )
			cell.grid(row=row, column=col)
	return outer

mbar = buildMenu(top)
top["menu"] = mbar

board = buildBoard(top)
board.pack()
status = tk.Label(top, text="testing", border=0, background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True)

tk.mainloop()
