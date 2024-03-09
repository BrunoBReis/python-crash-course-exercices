# Working with dictionary

rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}

for key, value in sorted(rivers.items()):
    print(f"The {key.title()} runs through {value}")

for key in sorted(rivers.keys()):
    print(key)

for value in sorted(rivers.values()):
    print(value)