from pprint import pprint

song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
]

artists = set()
for song, artist in song_library:
    artists.add(artist)

pprint(artists)
print("Opeth" in artists)
alphabetical = list(artists)
alphabetical.sort()
pprint(alphabetical)

print('----')
artists2 = {"Guns N' Roses", 'Vixy and Tony', 'Sarah Brightman', 'Opeth'}
bands = {"Opeth", "Guns N' Roses"}
print(artists2.issuperset(bands))
print(bands.issuperset(artists2))
