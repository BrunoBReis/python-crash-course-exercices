favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

# Printing each favorite lanuage for each person
for name, languages in favorite_languages.items():
    print(f'{name.title()} likes:')
    for language in languages:
        print(f"\t{language}")