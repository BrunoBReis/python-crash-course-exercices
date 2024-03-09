def make_shirt(size='large', message='I love python'):
    """Make a shirt"""
    print(
        f"You're shirt was created with {size} size and this message {message}")


make_shirt('small', 'I love python')
make_shirt(message='I love python', size='medium')
make_shirt()
