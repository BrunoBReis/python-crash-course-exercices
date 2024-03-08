# Hello admin

usernames = ["funny_coder", "data_explorer", "pizza_lover", "bookworm123", "admin"]

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, welcome")
else:
    print("We need to find more users.")