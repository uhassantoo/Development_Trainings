file = open('filehandle.txt', 'r')
for data in file:
    print(data)
    
#Second Way
file = open('filehandle.txt', 'r')
print(file.read())

# File write () Function

file = open('um.txt', 'w')
file.write('My Name is Umer hassan')
file.write('Python Course')
file.close()

# Second Way
with open('ume.txt','w') as new:
    new.write('This is new file of python ')