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

mbar = buildMenu(top)
top["menu"] = mbar

tk.mainloop()
