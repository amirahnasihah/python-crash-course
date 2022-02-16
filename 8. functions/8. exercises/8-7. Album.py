# no optional arguments
def make_album(artist_name, title):
    """Return a dictionary info about an album."""
    album_dict = {
        'artist': artist_name.title(),
        'title': title.title(),
        }
    return album_dict

music_album = make_album('vivaldi', 'four seasons')
print(music_album)

music_album = make_album('beethoven', 'fur elise')
print(music_album)

music_album = make_album('strauss', 'the blue danube')
print(music_album)


print("\n")
# add an optional parameter
def make_album(artist_name, title, total_songs=None):
    """Return a dictionary of info about an album."""
    album = {
        'artist': artist_name.title(), 
        'title': title.title(),
        }
    if total_songs:
        album['total'] = total_songs
    return album

music_album = make_album('vivaldi', 'four seasons', total_songs=10)
print(music_album)

music_album = make_album('hishaisi', 'summer', total_songs=20)
print(music_album)

music_album = make_album('mozart', 'requiem', total_songs=5)
print(music_album)