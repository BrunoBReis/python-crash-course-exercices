# Guest list

names = ["Lucas", "Antonio", "Fernando"]
message = "welcome to my dinner"

print(f"{names[0]}, {message}")
print(f"{names[1]}, {message}")
print(f"{names[2]}, {message}")

print(f"\n{names[0]}, can't go to dinner\n")

names.remove("Lucas")
names.append("Joao")

print(f"{names[0]}, {message}")
print(f"{names[1]}, {message}")
print(f"{names[2]}, {message}")

print("\nI found a bigger table, more guests are coming\n")


names.insert(0, "Toninho")
print(names)
names.insert(2, "Davi")
print(names)
names.append("Alice")
print(names)

print(f"{names[0]}, {message}")
print(f"{names[1]}, {message}")
print(f"{names[2]}, {message}")
print(f"{names[3]}, {message}")
print(f"{names[4]}, {message}")
print(f"{names[5]}, {message}")

print("\nUnfortunately I was wrong, only two people can stay\n")

# I use this while to save some writing
while (len(names) > 2 ):
    univitation_letter = "I'm sorry for that"
    popped_name = names.pop()
    print(f"{popped_name} {univitation_letter}")

message = "you're still invited"
print(f"{names[0]} {message}")
print(f"{names[1]} {message}")

del names[0]
del names[0]

print(names)