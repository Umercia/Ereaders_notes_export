# -*- coding: utf8 -*-

################################################################################
# Program Python 3
# Author: Maurice Clere, 2018
# licene: GPL
################################################################################
# Obj: import kindle notes "My Clippings.txt" into SQLite Database "note.sqlite"
# New string methodes: .strip(), .rfind(), .find(), .startswith(), isnumeric()

# New: module datetime have a function called
# "datetime" also: mind how the module/function is imported and called.
#for example:
#       import datetime
#       date = datetime.strptime('Jun 1 2005 1:33PM', '%b %d %Y %I:%M%p')
# OR:
#       from datetime import datetime
#       date = datetime.datetime.strptime('Jun 1 2005 1:33PM', '%b %d %Y %I:%M%p')

# methode:  .strptime(): string to datetime format
#           .strptime(): datetime to string format

# Import external function #####################################################
from import_to_notesqlite import notesqlite_import
from datetime import datetime

# Main #########################################################################
# parse kindle notes
handle = open("My Clippings.txt", encoding="utf8")
n_count = 0
title_b = True

print("-----------------------------------------------------")

i = 0
text = ""

for line in handle :
	line = line.strip() # remove spaces, tabs, or newlines at the begin and end
	if i == 0 :
		from_pos = line.rfind("(")
		to_pos = line.rfind(")",from_pos)
		title = line[0:from_pos-1]
		author = line[from_pos+1:to_pos]
		print("Title =", title,)
		print("Author =", author)
		i = i + 1

	elif i == 1 :
		if line.startswith('- Your Highlight'):
			type_note = "highlight"
		elif line.startswith('- Your Note'):
			type_note = "note"

		from_pos = line.find("location")
		to_pos = line.find(" |",from_pos)
		loc = line[from_pos + 9:to_pos]

		if loc.isnumeric():
			start_loc = end_loc = loc
		else:
			start_loc = loc.split(sep = "-")[0]
			end_loc = loc.split(sep = "-")[1]

		from_pos = line.find(", ")
		to_pos = len(line) - 1
		date_note = line[from_pos+2:to_pos]

		date_note = datetime.strptime(date_note, '%d %B %Y %H:%M:%S')  # convert string to date
		date_note = datetime.strftime(date_note, '%Y-%m-%d %H:%M:%S')  # convert date to formated string

		print("Type of note = ", type_note)
		print("Start_loc = ", start_loc)
		print("End_loc = ", end_loc)
		print("date is :", date_note)
		i = i + 1

	elif i == 2 :
		i = i + 1
		continue

	else :
		if not (line.startswith('====')):
			line = line.strip()
			text = text + line
		else :
			print("Content =", text)
			print("---------------------------------")
			print("---------------------------------")
			notesqlite_import(title, author, type_note, start_loc, end_loc, date_note,
			text, "Maurc", "Kindle_Voyage")
			text = ""
			i = 0
