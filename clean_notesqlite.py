# -*- coding: utf8 -*-

################################################################################
# Program Python 3
# Author: Maurice Clere, 2018
# licene: GPL
################################################################################
# Obj: if the personnal note is "1", "2" or "3". this code change the note type
# of the corresponding "highlight" to "title_1", "tilte_2" or "title_3". This
# type is Then use during the export of the notes to create a file where the
# title of the mains chapters are present.

# New: connection object "cur1" (to sqlite DB), will update itself on a cur1.execute()
# meaning that we cannot loop on "for row in cur1:" and use the cur1.execute() inside the loop
# --> we need to creat another "cur2 = conn.cursor()"

# Import external function #####################################################
import sqlite3

# Main #########################################################################
conn = sqlite3.connect("note.sqlite")
cur1 = conn.cursor()
cur2 = conn.cursor()

cur2.execute('DELETE FROM Notes WHERE note_content IS NULL')
conn.commit()

cur1.execute("SELECT id, book_id, note_content, note_type_id, position_start, position_end, read_date, user_id FROM Notes ORDER by book_id, position_start")

pos_s_b = -1  # position-start buffer (one spet before)
pos_e_b = -1  # position-end buffer (one spet before)
read_date_b = ""
id_b = 0
listup = ("1","2","3")
i = 0

for row in cur1:
    pos_s = row[4]
    pos_e = row[5]
    id = row[0]
    note_type_id = row[3]
    content = row[2]

#   if (pos_s == pos_s_b or pos_e == pos_e_b) :
    if ( pos_s_b <= pos_s < pos_e_b) or ( pos_s_b <= pos_e < pos_e_b ) or ( pos_s <= pos_e_b < pos_e ) or ( pos_s <= pos_s_b < pos_e ) or ( pos_s == pos_e == pos_s_b == pos_e_b) :
#       print(content in listup," --- content type = ", type(content), " --- position Start = ", pos_s, " --- position End = ", pos_e, " --- note_type_id = ", note_type_id, " --- content = ", content[:10] )
        if note_type_id == 2 and (content in listup) :
            id_to_delete = id
            title_type_id = int(content) + 2  # note content (should be a number 1 to 3)
            cur2.execute('UPDATE  Notes SET note_type_id = ? WHERE id = ?',(title_type_id,id_b))
        elif note_type_id_b == 2 and  (content_b in listup) :
            id_to_delete = id_b
            title_type_id = int(content_b) + 2  # note content (should be a number 1 to 3)
            cur2.execute('UPDATE  Notes SET note_type_id = ? WHERE id = ?',(title_type_id,id))
        else :
            id_to_delete = min(id_b,id)     # delete older version (lower id)

        print ("delete row id == ", id_to_delete)
        cur2.execute('DELETE FROM Notes WHERE id = ?',(id_to_delete,))
        conn.commit()

    pos_s_b = pos_s
    pos_e_b = pos_e
    id_b = id
    note_type_id_b = note_type_id
    content_b = content
    i = i + 1
    # print("iteration : ", i)

cur1.close()
cur2.close()
