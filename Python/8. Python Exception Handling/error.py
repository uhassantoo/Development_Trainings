# Python try...except Block
# The try...except block is used to handle exceptions in Python. Here's the syntax of try...except block:

# try:
#     # code that may cause exception
# except:
#     # code to run when exception occurs
# try:
#     even = [2,8,12,14]
#     print(even[6])
    

# except:
#     print('Error occured')

# odd = [3,6,7,32]
# print(odd[8])

try :
    odd = [3,5,7,12,11]
    print(odd[1])
    
except:
    print('Out of index number')