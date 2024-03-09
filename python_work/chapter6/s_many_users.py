# Working with users

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user, data in users.items():
    print(f'User {user} data is: ')
    for item, name in data.items():
        print(f'\t{name}')