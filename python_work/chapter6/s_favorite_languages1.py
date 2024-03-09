# Working with formatation

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Call a specific value
language = favorite_languages['sarah'].title()
print(f"Sarah favorite language is {language}")

# Loopping through all keys and values
for name, language in favorite_languages.items():
    print(f'My name is {name.title()} and I like {language} language')

# Lopping through all keys and find my favorite friends language
friends = ['jen', 'edward']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name]
        print(f'Hi, {name.title()}! I see you like {language}')

print()
# Printing all names in order
for key in sorted(favorite_languages.keys()):
    print(key.title())
print()

# Looping through all languages (removing duplicates)
for value in set(sorted(favorite_languages.values())):
    print(value.title())