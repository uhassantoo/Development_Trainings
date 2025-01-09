class Perfume:
    frangance = ''
    lasting = ''
    nature = ''
    
    def arabic(self):
        print("Oud Perfume")
    
    def western(self):
        print('The Queen')
        
        
class Abc(Perfume):
    
    def arabic1(self):
        print('Attar and Perfume')
        
        
perf = Abc()

perf.frangance = 'Jasmine'
perf.lasting = 8
perf.nature = 'woody'

#Access from subclass
perf.western()
perf.arabic1()

print(perf.frangance,perf.lasting,perf.nature)


#override method 

class Animal:
    name = ''
    
    def eat(self):
        print('I eat chickens')
        
class Cat(Animal):
    #overirde method
    
    def eat(self):
        print('I eat mouse and chicken')
        
a = Cat()
b = Animal()

a.eat()
b.eat()

# Super Function
class Dog(Animal):
    def eat(self):
     super().eat()
      
    print('I eat Dogs')

c = Dog()
c.eat()

#Multiple Inheritance

class Birds:
    def info(self):
        print('I have parrots')
        
class Tiger:
    def info1(self):
        print('I have tigers info')
        
class Baby(Birds,Tiger):
    def info_baby(self):
        print('I am BABY')
        
pet = Baby()

pet.info()
pet.info1()
pet.info_baby()


# Multilevel
class Dada:
    def super_baba(self):
     print('This is Base class')
    
class Baba(Dada):
    def baba_g(self):
        print('This is baba g')
        
class Beta(Baba):
    def beta_g(self):
        print('This is beta')
    
sons = Beta()

sons.super_baba()
sons.baba_g()
sons.beta_g()