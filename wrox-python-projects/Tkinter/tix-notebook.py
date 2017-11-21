import tkinter.tix as tix
import tkinter.messagebox as mb

top = tix.Tk()

nb = tix.NoteBook(top, width=300, height=200)
nb.pack(expand=True, fill='both')

nb.add('page1', label="Text")
f1 = tix.Frame(nb.subwidget('page1'))
st = tix.ScrolledText(f1)
st.subwidget('text').insert("1.0", "Here is where the text goes...")
st.pack(expand=True)


nb.add('page2', label="Message Boxes")
f2 = tix.Frame(nb.subwidget('page2'))
tix.Button(f2, text="error",  bg="lightblue",
                 command=lambda t="error", m="This is bad!": 
				 mb.showerror(t,m) ).pack(fill='x',expand=True)
tix.Button(f2, text="info",  bg='pink',
                 command=lambda t="info", m="Information": 
				 mb.showinfo(t,m) ).pack(fill='x',expand=True)
tix.Button(f2, text="warning", bg='yellow',
                 command=lambda t="warning", m="Don't do it!": 
		                 mb.showwarning(t,m) ).pack(fill='x',expand=True)
tix.Button(f2, text="question", bg='green',
                 command=lambda t="question", m="Will I?": 
		                 mb.askquestion(t,m) ).pack(fill='x',expand=True)
tix.Button(f2, text="yes-no", bg='lightgrey',
                 command=lambda t="yes-no", m="Are you sure?": 
		                 mb.askyesno(t,m) ).pack(fill='x',expand=True)
tix.Button(f2, text="yes-no-cancel", bg='black', fg='white',
                 command=lambda t="yes-no-cancel", m="Last chance...": 
		                 mb.askyesnocancel(t,m) ).pack(fill='x',expand=True)

f1.pack()
f2.pack(side='top', fill='x')

top.mainloop()


