# List of messages

def show_messages(list_names:list[str]):
    """Printing list names"""
    for name in list_names:
        print(name.title())

names = ['bruno', 'julia', 'antonio']

show_messages(names[:])
