#!/usr/bin/python3
#shebang (#!/usr/bin/python3): used to specify which interpreter will be used to run the program.

import zipfile
#import zipfile: library is imported which allows creating, reading, and modifying ZIP files in Python.

f = open("names.txt", "r")
#text file named names.txt is opened in read mode ("r").

names = [name.strip() for name in f.readlines()]
#names.txt are read using f.readlines(), which returns a list of lines from the file.
#strip() method is used to remove any leading/trailing whitespace or newline characters (\n) from each line.
#names containing clean names (without newline characters or extra spaces).

inputfile = 'secret.txt'

for name in (names):
#for loop iterates over each name in the names list.

	with zipfile.ZipFile(name, 'w', compression=zipfile.ZIP_DEFLATED) as COMP:
#new ZIP file is created using zipfile.ZipFile.
#name: The name of the new ZIP file (taken from the names list).
#'w': Write mode, which means a new file will be created, or an existing file with the same name will be overwritten.
#compression=zipfile.ZIP_DEFLATED: Files are compressed using the DEFLATE algorithm (the default compression method for ZIP files).
#with statement is used to open the file, ensuring it is automatically closed after the operation is complete.

		COMP.write(inputfile)
#function in Python's zipfile library is used to add files to a compressed archive (ZIP).
#inputfile: The file to be compressed.

		inputfile = name
#After creating the archive, inputfile is updated to the name of the newly created archive (name).
