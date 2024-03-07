# Counting to million

numbers = [number for number in range(1,1_000_001)]

# Verifing if goes to a million
print(max(numbers))

num_string = ''
for number in numbers:
    num_string += f'{number} '

print(num_string)