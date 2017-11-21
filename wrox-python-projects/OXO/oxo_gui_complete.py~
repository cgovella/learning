import tkinter as tk
import tkinter.messagebox as mb
import oxo_logic

top = tk.Tk()

def buildMenu(parent):
    menus = (
        ("File", (("New", evNew),
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

def evNew():
      status['text'] = "Playing game"
      game2cells(oxo_logic.newGame())

def evResume ():     
      status['text'] = "Playing game"
      game = oxo_logic.restoreGame()
      game2cells(game)

def evSave():
      game = cells2game()
      oxo_logic.saveGame(game)
      
def evExit ():
      if status['text'] == "Playing game":
          if mb.askyesno("Quitting","Do you want to save the game before quitting?"):
              evSave()
      top.quit()
      
def evHelp ():
	mb.showinfo("Help",'''
	File->New:  starts a new game of tic-tac-toe
	File->Resume: restores the last saved game and commences play
	File->Save: Saves current game.
	File->Exit: quits, prompts to save active game
        Help->Help: shows this page
        Help->About: Shows information about the program and author''')

def evAbout():
      mb.showinfo("About","Tic-tac-toe game GUI demo by Alan Gauld")

def evClick(row,col): 
	if status['text'] == "Game over":
		mb.showerror("Game over", "Game over!")
		return
		
	game = cells2game()
	index = (3*row) + col
	result = oxo_logic.userMove(game, index)
	game2cells(game)
	
	if not result:
		result = oxo_logic.computerMove(game)
		game2cells(game)
	if result == "D":
		mb.showinfo("Result", "It's a Draw!")
		status['text'] = "Game over"
	else:
		if result =="X" or result == "O":
		    mb.showinfo("Result",  "The winner is: {}".format(result))
		    status['text'] = "Game over"
		
def game2cells(game):
	table = board.pack_slaves()[0]
	for row in range(3):
		for col in range(3):
			table.grid_slaves(row=row,column=col)[0]['text'] = game[3*row+col]

	
def cells2game():
	values = []
	table = board.pack_slaves()[0]
	for row in range(3):
	    for col in range(3):
                values.append(table.grid_slaves(row=row, column=col)[0]['text'])
	return values
	
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
status = tk.Label(top, text="Playing game", border=0, background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True)

tk.mainloop()
