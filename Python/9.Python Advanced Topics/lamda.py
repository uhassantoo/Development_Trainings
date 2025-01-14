def greet():
    print('Hello Today is Python Day')
    
greet()     


greet1 = lambda : print('hello')

greet1()
greet1()
greet1()

add = lambda : print(2+2)

add()

greet_user = lambda user , name : print('this is parameter', name , user)

greet_user('hello','hi')