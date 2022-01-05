''' Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each persons name and their favorite places. '''

# A list in a dcitionary

favorite_places = {
    'yunho': ['gwangju', 'dubai'],
    'eunji': ['busan', 'seoul', 'jeju do', 'tokyo'],
    'huh gak': ['seoul'],
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:    # 'list' object has no attribute 'title'
        print(f"- {place.title()}")