artists = {"Juice Wrld":["Lucid Dreams", "All Girls are the Same", "Robbery", "Lean Wit Me", "Armed and Dangerous"], "Lil Tecca":["Ransom", "Love Me", "Did It Again", "Shots", "Somebody"], "Nav":["Wanted You (feat. Lil Uzi Vert)", "Myself", "Some Way", "Champion (feat. Travis Scott)", "Up"], "Lil Uzi Vert": ["XO Tour Llif3", "The Way Life Goes (feat. Oh Wonder)", "Money Longer", "You Was Right", "Erase Your Social"], "Lil Tjay":["Pop Out (feat. Polo G)", "F.N", "Brothers (feat. Lil Durk) - Remix", "Leaked", "Goat"] }

def find_songs(artist_name):
    for key in artists:
        if key == artist_name:
            return artists[key]
