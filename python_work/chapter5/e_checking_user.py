# Checking usernames

current_users = ["funny_coder", "data_explorer", "pizza_lover",
                 "bookworm123", "iopa"]
new_users = ["funny_coder", "codebreaker101", "music_lover24",
             "traveling_feet", "cloud_surfer99"]

# Verifiy if new_users exists
if new_users:
    for new_user in new_users:
        # Verifiy if current_users exists
        if current_users:
            # Checking if new_user was taken
            if new_user in current_users:
                print(f"{new_user} was already taken. Choose antoher username.")
            else:
                print(f"{new_user} can be use!")
        else:
            print("No new users")
            break
else:
    print("No current users")

# obs: using new_user to loop insted of looping current_user is better!