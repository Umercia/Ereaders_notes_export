import sqlite3

# creation de la data base
conn = sqlite3.connect('note.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Users')  # to be removed at the end
cur.execute('DROP TABLE IF EXISTS Books')  # to be removed at the end
cur.execute('DROP TABLE IF EXISTS Authors')  # to be removed at the end
cur.execute('DROP TABLE IF EXISTS Note_types')  # to be removed at the end
cur.execute('DROP TABLE IF EXISTS Notes')  # to be removed at the end
cur.execute('DROP TABLE IF EXISTS Device_types')  # to be removed at the end

cur.execute('CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Authors (id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Books (id INTEGER PRIMARY KEY, title TEXT UNIQUE)')
cur.execute('CREATE TABLE Note_types (id INTEGER PRIMARY KEY, type TEXT UNIQUE)')
cur.execute('CREATE TABLE Device_types (id INTEGER PRIMARY KEY, type TEXT UNIQUE)')

# *** to avoid doublon on more than one parameters see below the UNIQUE add to the end
cur.execute('CREATE TABLE Notes (id INTEGER PRIMARY KEY, note_content TEXT, note_type_id INTEGER, position_start INTEGER, position_end INTEGER, read_date TIMESTAMP,import_date TIMESTAMP, user_id INTEGER, book_id INTEGER, author_id INTEGER, device_type_id INTEGER, UNIQUE(note_content, position_start, user_id) )')

cur.execute('INSERT  OR IGNORE INTO Note_types (id, type) VALUES (1, "highlight")')
cur.execute('INSERT  OR IGNORE INTO Note_types (id, type) VALUES (2, "note")')
cur.execute('INSERT  OR IGNORE INTO Note_types (id, type) VALUES (3, "title_1")')
cur.execute('INSERT  OR IGNORE INTO Note_types (id, type) VALUES (4, "title_2")')
cur.execute('INSERT  OR IGNORE INTO Note_types (id, type) VALUES (5, "title_3")')
conn.commit()

conn.close()
