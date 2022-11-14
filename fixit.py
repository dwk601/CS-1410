# Opens and reads the contents of both a.txt and b.txt into separate strings
# Performs the following actions on the strings (not the files):
# a. Reverses the contents of a.txt: “tacocat” becomes “tacocat” and “olleH” would become "Hello".
# b. Performs the following replacements in the contents of b.txt:
# - Remove all instances of the string “xx”
# - Replace every ‘4’ with ‘.’
# - Replace every ‘q’ with ‘/’
# - Replace every ‘@’ with ‘"’ (double quotes)
# c. Creates a new file called rework.py
# d. Writes the newly modified strings to this file, first ‘a’ then ‘b’
# From the command line, run the file Classes/CS1410/Files/rework.py that you just created
# Note that you now have a “Notes” subfolder in each of the subfolders for Classes (CS1410 and MATH1100)
# In main.py write code to perform the following actions:
# a. Move the file Notes/CS1410/today.txt to Classes/CS1410/Notes
# b. Move the file Notes/MATH1100/yesterday.txt to Classes/MATH1100/Notes
# c. Delete the folder Notes
# Use tar to create a tar.gz file of your folder structure from the folder Classes: tar -czvf project3.tar.gz Classes/


import os
import shutil

#Open file a and read contents into a string
with open('a.txt', 'r') as a:
    a = a.read()
    print("Contents of a.txt: " + a)
    a = a[::-1] #Reverse string
    print("\nReversed contents of a.txt: " + a)
    
#Open file b and read contents into a string
with open('b.txt', 'r') as b:
    b = b.read()
    print("\nContents of b.txt: " + b)
    b = b.replace("xx", "") #Remove all instances of "xx"
    b = b.replace("4", ".") #Replace all 4's with .
    b = b.replace("q", "/") #Replace all q's with /
    b = b.replace("@", '"') #Replace all @'s with "
    print("\nModified contents of b.txt: " + b)
    
#Create new file rework.py and write modified strings to it
rework = open('rework.py', 'w')
rework.write(a)
rework.write(b)
rework.close()

#Move today.txt to CS1410/Notes
shutil.move("Notes/CS1410/today.txt", "Classes/CS1410/Notes")
#Move yesterday.txt to MATH1100/Notes
shutil.move("Notes/MATH1100/yesterday.txt", "Classes/MATH1100/Notes")
#Delete Notes folder
os.rmdir("Notes")

#Create tar.gz file of Classes folder
os.system("tar -czvf project3.tar.gz Classes/")

