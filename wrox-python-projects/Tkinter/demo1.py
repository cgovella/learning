import tkinter as tk

# create the event handler to clear the text
def evClear():
  lHistory['text'] = eHello.get()
  eHello.delete(0, tk.END)

# create the top level window/frame
top = tk.Tk()
F = tk.Frame(top)
F.pack(fill="both")

# Now the frame with text entry
fEntry = tk.Frame(F, border=1)
eHello = tk.Entry(fEntry)
eHello.pack(side="left")
lHistory = tk.Label(fEntry, text="     ", foreground="steelblue")
lHistory.pack(side="bottom", fill="x")
fEntry.pack(side="top")

# Finally the frame with the buttons. 
# We'll sink this one for emphasis
fButtons = tk.Frame(F, relief="sunken", border=1)
bClear = tk.Button(fButtons, text="Clear Text", command=evClear)
bClear.pack(side="left", padx=5, pady=2)
bQuit = tk.Button(fButtons, text="Quit", command=F.quit)
bQuit.pack(side="left", padx=5, pady=2)
fButtons.pack(side="top", fill="x")

# Now run the eventloop
F.mainloop()
