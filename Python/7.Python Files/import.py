import os
# What are the 4 file handling functions?
#  The four primary functions used for file handling in Python are: 


#  open()  : Opens a file and returns a file object. 
#  read()  : Reads data from a file. 
#  write()  : Writes data to a file. 
#  close()  : Closes the file, releasing its resources. 
def createfile(filename):
    with open(filename , 'w') as f:
        print('File' +filename+ 'Created')
        

# Read File

def readfile(filename):
    with open(filename , 'r') as  f:
        content = f.read()
        print(content)

# Append file      
def appendfile(filename, text):
    with open(filename , 'a') as f:
        f.write(text)
        print('Text append to this file' +filename+ 'Successfully')

# Append to the new line
def appendfile1(filename, text):
    with open(filename , 'a+') as f:
        f.write(text)
        print('New text append to this file' +filename+ 'Successfully')
#rename the file 
def renamefile(filename,new_file):
    os.rename(filename , new_file)
    print('File : '+filename+'reanamed to '+new_file+'Changed File Name Sucessfully')
# delete


# Create  a object

filename = 'example.txt'

createfile(filename)
readfile(filename)
appendfile(filename, 'this is new line text')
appendfile1(filename, 'Append this line new one \n')
renamefile(filename,new_file='Renamed_File')