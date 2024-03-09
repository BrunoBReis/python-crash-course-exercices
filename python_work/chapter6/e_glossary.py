# Some python's words

glossary = {
    'print()' : "it's a function that prints what is inside",
    '.lower()' : "it's a method that lowers strings",
    'list' : "it's a python built in type",
    '.append()' : "it's a method that includes a new item in list",
    'if' : "it's a conditional statement in python"
}

for key, value in glossary.items():
    print(f"{key} {value}")