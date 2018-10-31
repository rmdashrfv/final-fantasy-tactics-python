import sqlite3

conn = sqlite3.connect('game.db')
c = conn.cursor()
c.execute('''CREATE TABLE game
             (date text, trans text, symbol text, qty real, price real)''')

def savegame():
    c.execute('''INSERT INTO game
                 (date text, trans text, symbol text, qty real, price real)''')
