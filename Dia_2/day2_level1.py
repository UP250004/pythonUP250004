#Dia 2 programando en Python
# Variables in Python
import math

first_name = 'Brian'
last_name = 'Rubio'
country = 'Mexico'
city = 'Aguascalientes'
age = 23
is_married = False
skills = ['HTML', 'CSS', 'Python', "C++"]
person_info = {
    'firstname':first_name, 
    'lastname':last_name, 
    'country':country,
    'city':city
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Brian', 'Rubio', "Mexico", 23, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


#####################
print(type(first_name))   # String
print(type(last_name)) # String
print(type(country))    # String
print(type(person_info))    # Dict
#####################

#####################
print(len(first_name)) 
print(len(last_name)) 
print(len(country)) 
print(len(first_name)) 
#####################