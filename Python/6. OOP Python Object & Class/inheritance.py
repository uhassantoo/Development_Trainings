class Cars: # Superclass
    def __init__(self,name = '' ,make = '',model = ''):
        self.name = name
        self.make = make
        self.model = model
        
# Create a Object
Ha_cars = Cars()

# Access
Ha_cars.name = 'Hashir Cars'
Ha_cars.make = 'BMW'
Ha_cars.model = '7 series'
print('Cars Details....',Ha_cars.name,Ha_cars.model,Ha_cars.make)     

class Car1(Cars): #sub class
    color = ''
    
    def display(self):
     print('Parent Car Details' , self.name)
     

#Create a object
child_car = Car1

#Acces
child_car.color = 'Blue'


# Task Python Inheritance
        
        