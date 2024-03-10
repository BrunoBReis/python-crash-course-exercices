# Opitional argumento could be None or '' 
def get_formatted_name(first_name, last_name, middle_name=None):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"

    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("enter 'q' to quit")

    quit_message = 'q'

    f_name = input("First name: ")
    if f_name == quit_message:
        break
    l_name = input("Last name: ")
    if l_name == quit_message:
        break
    print("Do you want middle name? (y/n)")
    answer = input().lower()
    if answer == quit_message:
        break
    if answer == 'y':
        m_name = input("Middle name: ")
        name = get_formatted_name(f_name, l_name, m_name)
        print("Here is your name\n")
        print(name)
        break
    if answer == 'n':
        print("Here is your name\n")
        name = get_formatted_name(f_name, l_name)
        print(name)
        break






# person = get_formatted_name('bruno', 'reis')
# print(person)
# person = get_formatted_name('bruno', 'reis', 'bragança')
# print(person)
