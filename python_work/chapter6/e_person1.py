# Creating a person

person_0 = {
    'first_name' : 'Bruno',
    'last_name' : 'Reis',
    'age' : '21',
    'city' : 'Brasília',
}
person_1 = {
    'first_name' : 'Lucas',
    'last_name' : 'Costa',
    'age' : '30',
    'city' : 'Brasília',
}
person_2 = {
    'first_name' : 'Anna',
    'last_name' : 'Lutra',
    'age' : '22',
    'city' : 'Brasília',
}

people = [person_0, person_1, person_2]

for person in people:
    for key, value in person.items():
        print(key, value)
    print('-----')