class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f'I am Cat and My name is {self.name} and my age is {self.age}')
        
    def makesound(self):
        print('Meow')
        
class Tiger:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
          print(f'I am tiger and My name is {self.name} and my age is {self.age}')
        
    def makesound(self):
        print('Wowwww')
        
        
cat1 = Cat('Kitty',2)
tiger1 = Tiger('Hellow', 3)
for animal in (cat1, tiger1):
    animal.info()
    animal.makesound()
    
    
num1 = 1
num2 = 2
print(num1+num2)

a = 2
b = 2
print(a+b)

str1 = 'Python'
str2 = 'OOP'
print(str1+str2)