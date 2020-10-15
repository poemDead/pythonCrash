def make_album(singer,title,num=None):
    album = {
        'singer':singer.title(),
        'title':title.title(),
    }
    if num:
        album['number_of_songs'] = num
    return album

while True:
    print("\nPlease enter the album details.")
    print("(you can enter 'q' at any time to quit)")

    singer = input("Singer is: ")
    if singer == 'q':
        break
    title = input("Title of the album is: ")
    if title == 'q':
        break
    num = input("How many songs in it: \n(You can press enter to skip this step.)")
    if num == 'q':
        break

    album = make_album(singer,title,num)
    print(album)
    print('---------------')