import sqlite3

conn = sqlite3.connect('menu.sqlite')

c = conn.cursor()

c.execute('''
          CREATE TABLE menu
          (id INTEGER PRIMARY KEY ASC, 
           menu_item_name VARCHAR(100) NOT NULL,
           menu_item_no INTEGER NOT NULL,
           date_added DATETIME NOT NULL,
           price FLOAT NOT NULL,
           calories FLOAT NOT NULL,
           cuisine_country VARCHAR(20),
           main_ingredient VARCHAR(20),
           portion_size VARCHAR(100),
           is_vegetarian INTEGER,
           manufacturer VARCHAR(100),
           size VARCHAR(100),
           is_fizzy INTEGER,
           is_hot INTEGER,
           type VARCHAR(5) NOT NULL)
          ''')

conn.commit()
conn.close()
