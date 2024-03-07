# Working on a list with every function

letters = ['b', 'c', 'd', 'e', 'f']

# Adding a upper case to each element
upper_letters = []
for letter in letters:
    upper_letters.append(letter.upper())

print(upper_letters)

# Adding elements
upper_letters.append('G')
upper_letters.insert(0, 'A')

print(upper_letters)

# Deleting numbers
del upper_letters[-1]
del upper_letters[0]

print(upper_letters)

# Poping numbers
upper_letters.pop()
upper_letters.pop()

print(upper_letters)

# Sorting
print(sorted(upper_letters))
upper_letters.sort(reverse=True)
print(upper_letters)
print(len(upper_letters))