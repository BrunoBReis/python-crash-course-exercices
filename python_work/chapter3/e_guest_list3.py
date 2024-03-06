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
