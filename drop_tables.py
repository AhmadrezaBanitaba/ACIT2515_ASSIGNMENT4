import sqlite3

conn = sqlite3.connect('menu.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE menu
          ''')

conn.commit()
conn.close()
