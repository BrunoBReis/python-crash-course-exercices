def make_album(artist_name:str, album_title:str, number_songs:int=None):
    album = {
        'artist_name' : artist_name.title(),
        'album_title' : album_title.title(),
    }
    if number_songs:
        album['number_songs'] = number_songs
    return album

first_album = make_album('Pedro', 'coisas da geracao')
print(first_album)
second_album = make_album('pedro', 'depois do fim', 13)
print(second_album)

while True:
    print("To quit just type.\n")
    quit_message = 'quit'
    a_name = input("What is artist name:\n").strip()
    if a_name == quit_message:
        break
    a_title = input("What is album title:\n").strip()
    if a_name == quit_message:
        break
    print('Do you want number of functions?')
    answer = input().lower()
    if a_name == quit_message:
        break
    elif answer == 'y':
        n_songs = int(input("Number of songs:\n")).strip()
        print("Great! Here's your album")
        album = make_album(a_name, a_title, n_songs)
        print(album)
        break
    elif answer == 'n':
        print("Great! Here's your album")
        album = make_album(a_name, a_title)
        print(album)
        break