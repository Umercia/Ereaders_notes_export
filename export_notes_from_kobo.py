# -*- coding: utf8 -*-

################################################################################
# Program Python 3
# Author: Maurice Clere, 2018
# licene: GPL
################################################################################
# Obj: import kobo notes "KoboReader.sqlite" into SQLite Database "note.sqlite"
# New: results of  "cur.execute('SELECT Text FROM Bookmark')" would be somehow
# executed only when we will loop on the rows (for row in cur:). Then each row is
# extract as a Python tuple.
# Note: It seems that "KoboReader.sqlite" does not store author information


# Import external function #####################################################
import sqlite3
from import_to_notesqlite import notesqlite_import
from datetime import datetime

# Main #########################################################################

conn = sqlite3.connect('KoboReader.sqlite')
cur1 = conn.cursor()
cur2 = conn.cursor()

cur1.execute('SELECT Text, DateCreated, VolumeID, StartContainerPath, EndContainerPath FROM Bookmark')

for row in cur1:
    if not len(row[0] == 0) :
        date_note = row[1][:-4]
        date_note = datetime.strptime(date_note, '%Y-%m-%dT%H:%M:%S')  # convert string to date
        date_note = datetime.strftime(date_note, '%Y-%m-%d %H:%M:%S')  # convert date to formated string
        text = row[0]
        book_id = row[2]
        author = ""
        type_note = "highlight"  # ---> to be updated
        start_loc = row[3]
        end_loc =row[4]

        # find Book title using book_id
        cur2.execute('SELECT BookTitle FROM content WHERE BookID = ? LIMIT 1',
        (book_id, ))
        try:
            title = cur2.fetchone()[0]
        except:
            print("error fecthing book_id")

        print("book_id is:", book_id)
        print("Title is:", title)
        print("---------------------------")

        notesqlite_import(title, author, type_note, start_loc, end_loc, date_note,
    text, "Maurc","Kobo_H2O")


cur1.close()
cur2.close()
