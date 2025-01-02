def greet():
    print('Hello Today is cold weather')


greet()

def cal(a,b):
    print('Calculator')
    print('Addition numbers', a+b)
    print ('Subtraction numbers', a-b)
    
    
cal(22,33)
cal (12,22)
cal(44,26)
cal(77,56)
cal(229,333)

# def cal1(*a):
#     print('Args')
    
#     print('Multiple',a)
    
# cal1(2,3,24,44,7)

# Default Value Function
def cal2 (a=2,b=5):
    print('Calculator Function')
    print('Multiple:', a*b)
    
cal2(20,20)