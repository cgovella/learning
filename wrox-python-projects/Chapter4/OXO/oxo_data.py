''' oxo_data is the data module for a tic-tac-toe (or OXO) game. 
    It saves and restores a game board. The functions are:
         saveGame(game) -> None
         restoreGame() -> game
    Note that no limits are placed on the size of the data.
    The game implementation is responsible for validating
    all data in and out.'''

import os.path
game_file = "oxogame.dat"

def _getPath():
    ''' getPath -> string
    Returns a valid path for data file. 
    Tries to use the users home folder, defaults to cwd'''

    try:
        game_path = os.environ['HOMEPATH'] or os.environ['HOME']
        if not os.path.exists(game_path):
            game_path = os.getcwd()
    except (KeyError, TypeError):
        game_path = os.getcwd()
    return game_path

def saveGame(game):
    ''' saveGame(game) -> None

    saves a game object in the data file in the users home folder.
    No checking is done on the input which is expected to
    be a list of characters'''
    
    path = os.path.join(_getPath(), game_file)
    try:
        with open(path, 'w') as gf:
           gamestr = ''.join(game)
           gf.write(gamestr)
    except FileNotFoundError:
        print("Failed to save file")

def restoreGame():
    ''' restoreGame() -> game

    Restores a game from the data file.
    The game object is a list of characters'''
    
    path = os.path.join(_getPath(), game_file)    
    with open(path) as gf:
        gamestr = gf.read()
        return list(gamestr)

def test():
    print("Path = ", _getPath())
    saveGame(list("XO XO XO "))
    print(restoreGame())

if __name__ == "__main__": test()
