import tkinter.tix as tix

top = tix.Tk()

lab = tix.Label(top)
lab.pack()

cb = tix.ComboBox(top, command=lambda s: lab.config(text=s))
for st in ["Fred","Ginger","Gene","Debbie","Tommy"]:
	cb.insert("end", st)
cb.pick(0)
lab['text'] = "Pick a value, any value..."
cb.pack()

top.mainloop()
