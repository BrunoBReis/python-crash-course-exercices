# Modifing lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding names
motorcycles.append("honda")
print(motorcycles)

motorcycles.insert(0, "volks")
print(motorcycles)

# Deleting names
del motorcycles[-1]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

popped_motorcycles = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycles)

motorcycles.remove("ducati")
print(motorcycles)