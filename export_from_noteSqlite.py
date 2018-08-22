# -*- coding: utf8 -*-

################################################################################
# Program Python 3
# Author: Maurice Clere, 2018
# licene: GPL
################################################################################
# Obj: export personnal notes from 'note.sqlite' into files (one per book)
# New: sqlite library: cur2.fetchone()[0] will read "row by row". so it cannot be
# inserted into a loops on "for row in cur1:" because it will creat an invisible
# "continue" (next iteration)

# Import external function #####################################################
import sqlite3


# Main #########################################################################

conn = sqlite3.connect('note.sqlite')
cur1 = conn.cursor()
cur2 = conn.cursor()

cur1.execute('SELECT book_id, note_content, note_type_id, position_start FROM Notes ORDER by book_id, position_start ')

book_title = []

for row in cur1:

#    print("Cur = ", cur1)
#    print("--------------------------------------------")
#    print("row = ", row)
#    print("--------------------------------------------")
#    print("Book_id = ", row[0])
    cur2.execute('SELECT title FROM Books WHERE id = ? LIMIT 1',(row[0], ))

    book_title = cur2.fetchone()[0]
    if len(book_title) > 50 :
        print("too long file name. lengh reduce to 50 character : ", file_name)
    file_name = book_title[0:51] + ".txt"
    file_name = file_name.replace(":","_")
    file_name = file_name.replace("'","_")
    file_name = file_name.replace('"',"_")
    file_name = file_name.replace("/","_")
    file_name = file_name.replace("(","_")
    file_name = file_name.replace(")","_")

    f = open(file_name,"a", encoding="utf8")

    try:
        note_type = row[2]
    except:
        print("Book : ", row[0], "at position ", row[3])

    if note_type == 3 :
        f.write("\n" + row[1].upper() + "\n")
    elif note_type == 1 :
        f.write("    - " + row[1] + "\n")
    elif note_type == 2 :
        f.write("    NOTE : " + row[1] + "\n")
    elif note_type == 4 :
        f.write(" * " + row[1] + "\n")
    elif note_type == 5 :
        f.write("     " + row[1] + "\n")

    f.close

cur1.close()
cur2.close()
