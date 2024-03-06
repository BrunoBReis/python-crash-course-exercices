# Guest list

names = ["Lucas", "Antonio", "Fernando"]
message = "welcome to my dinner"

print(f"{names[0]}, {message}")
print(f"{names[1]}, {message}")
print(f"{names[2]}, {message}")

print(f"\n{names[0]}, can't go to dinner\n")

names.remove("Lucas")
names.insert(0, "Joao")

print(f"{names[0]}, {message}")
print(f"{names[1]}, {message}")
print(f"{names[2]}, {message}")