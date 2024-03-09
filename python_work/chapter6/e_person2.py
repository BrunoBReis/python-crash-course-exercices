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

favorite_places = {
    'beach' : 'santa monica',
    'forest' : 'amazonica',
    'place' : 'home',
}

# Allocating favorite placest o each person 
person_0['favorite_places'] = favorite_places
person_1['favorite_places'] = favorite_places
person_2['favorite_places'] = favorite_places

# Allocate each person into a list
people = [person_0, person_1, person_2]

# Split person
for person in people:
    # Split key from value
    for key, value in person.items():
        # If key is equal to favorite_palce dictionary split into it
        if key == 'favorite_places':
            for place, name in favorite_places.items():
                print(f'\tFavorite places: {place} {name}')
        else:
            print(f'{key} {value}')