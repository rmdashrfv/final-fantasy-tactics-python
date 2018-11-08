import sqlite3

conn = sqlite3.connect('game.db')
c = conn.cursor()
c.execute('''CREATE TABLE game
             (id int, mainName varchar(255))''')

def savegame():
    slot = input('Save game to which slot?')
    slot = int(slot)
    c.execute(f'''INSERT INTO game WHERE id = {slot}
                 (date text, trans text, symbol text, qty real, price real)''')


# create a game table
# game table has fkeys to: party, and stores the name of the main character
