from array import array

# List
name_list = ['Theethawat', 'Sirinuch', 'Theematach', 'Songpon']

# Array
scores = array('i')
scores.append(156)
scores.append(99)

# Dictionary
person = {'first': 'Theethawat', 'last': 'Savastham'}
person['first'] = 'Songpon'

# Displaying
print(name_list)
print(scores)
print(person)

# Test For Loop
index = 0
print('For Loop')
while(index < len(name_list)):
    name = name_list[index]
    print(name)
    index = index + 1

# Test While Loop
print('Test While Loop')
index = 0
while index < len(name_list):
    name = name_list[index]
    print(name)
    index = index + 1
