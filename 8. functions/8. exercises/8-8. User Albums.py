# My answers

def make_album(artist_name, title, total_songs=0):
    """Return a dictionary of info about an album."""
    album_dict = {
        'artist': artist_name.title(), 
        'title': title.title(),
        }
    if total_songs:
        album_dict['tracks'] = total_songs
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat is the album's title? "
artist_prompt = "Who is the artist? "
continue_prompt = "\nEnter 'q' when finished and 'n' to continue. "

# responses stored in dict ('key': 'value') >>> {artist_name: title}
infos = {}

while True:
    # ask users
    title = input(title_prompt)
    if title == 'q':
        break
    
    artist = input(artist_prompt)
    if artist == 'q':
        break
    
    # store information
    infos[artist] = title
    
    # enter quit value 'q' when finished
    quit = input(continue_prompt)
    if quit == 'q':
        break
    
    music_album = make_album(artist, title)
    print(f"Results: {music_album}")
  
  
# continue and break is different. Use print() call for break statement.
