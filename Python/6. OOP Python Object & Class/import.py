from classes import Student 

ms = Student()
bs = Student()
# Access Prop
ms.name = 'Sara'
ms.course = 'Python'
print(f'Student Details:.. {ms.name} , {ms.std_id} , {ms.course}')


# Python Methods

class Room:
    length = 0.0
    breadth = 0.0
    
    
    # Create a Method
    def cal_area(self):
        print('Calculate Area is.. ', self.length * self.breadth )
        
# Create a obj
meeting_room = Room()


# Access Prop
meeting_room.length = 42.0
meeting_room.breadth = 30.0

# call inside method
meeting_room.cal_area()

# Python Constructors

class Room1:
    def __init__(self ,length , breadth ):
         self.length = length
         self.breadth = breadth

    def cal_area1(self):
        print('Calculate Area is.. ', self.length * self.breadth )
        
# Create a obj
study = Room()


# Access Prop
study.length = 52.0
study.breadth = 33.0

# call inside method
study.cal_area()