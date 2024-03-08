# Ordinal numbers

ordinal_numbers = [number for number in range(1,10)]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        sufix = 'st'
    elif ordinal_number == 2:
        sufix = 'nd'
    elif ordinal_number == 3:
        sufix = 'rd'
    else:
        sufix = 'th'
    print(f"{ordinal_number}{sufix}")