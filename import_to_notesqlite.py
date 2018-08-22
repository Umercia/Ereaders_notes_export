# 2. Update local DB -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
def notesqlite_import(title, author, type_, from_pos, to_pos, date_note, content, user, device):
# title, author, type, from_pos, to_pos, date_note, content

###############################################################################
# Import external functions
    import sqlite3
    from time import localtime, strftime

    s_time = strftime("%Y-%m-%d %H:%M:%S", localtime())

###############################################################################
# Main
    conn = sqlite3.connect('note.sqlite')
    cur = conn.cursor()

    # define a tuple with a single element (note the coma at the end)

    # update Books table and fetch book_id
    cur.execute('SELECT id FROM Books WHERE title = ? LIMIT 1',
    (title, ))
    try:
        book_id = cur.fetchone()[0]
    except:
        cur.execute('INSERT  OR IGNORE INTO Books (title) VALUES (?)', (title,))
        book_id = cur.lastrowid
    conn.commit()


    # update Authors table and fetch author_id
    cur.execute('SELECT id FROM Authors WHERE name = ? LIMIT 1',
    (author, ))
    try:
        author_id = cur.fetchone()[0]
    except:
        cur.execute('INSERT  OR IGNORE INTO Authors (name) VALUES (?)', (author,))
        author_id = cur.lastrowid
    conn.commit()

    # update note_type table and fetch types_id  (not sure it is needed since there is only two type)
    cur.execute('SELECT id FROM Note_types WHERE type = ? LIMIT 1',
    (type_, ))
    try:
        type_id = cur.fetchone()[0]
    except:
        cur.execute('INSERT  OR IGNORE INTO Note_types (type) VALUES (?)', (type_,))
        type_id = cur.lastrowid
    conn.commit()

    # update Users table and fetch user_id
    cur.execute('SELECT id FROM Users WHERE name = ? LIMIT 1',
    (user, ))
    try:
        user_id = cur.fetchone()[0]
    except:
        cur.execute('INSERT  OR IGNORE INTO Users (name) VALUES (?)', (user,))
        user_id = cur.lastrowid
    conn.commit()

    # update Device_types table and fetch device_id
    cur.execute('SELECT id FROM Device_types WHERE type = ? LIMIT 1',
    (device, ))
    try:
        device_id = cur.fetchone()[0]
    except:
        cur.execute('INSERT  OR IGNORE INTO Device_types (type) VALUES (?)', (device,))
        device_id = cur.lastrowid
    conn.commit()

    # update Notes table
    # ---> to update
    cur.execute('INSERT  OR IGNORE INTO Notes (note_content, position_start, position_end, read_date, book_id, author_id, note_type_id, user_id, import_date, device_type_id) VALUES (?,?,?,?,?,?,?,?,?,?)', (content,from_pos, to_pos, date_note,book_id, author_id, type_id, user_id, s_time, device_id))
    conn.commit()
    cur.close()
