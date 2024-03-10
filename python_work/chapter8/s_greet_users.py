def greet_users(names:list[str]):
    """Print a greet message"""
    for name in names:
        msg = f'Hello, {name.title()}'
        print(msg)
    

usernames = ['sarah', 'elizabeth', 'toninho']

greet_users(usernames)