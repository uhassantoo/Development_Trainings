# Type Conversion
#Implicit Conversion
num = 123
num1 = 12.3

new_num = num + num1
print(new_num)
print('type is: ', type(new_num))

#Explicit Conversion
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))
