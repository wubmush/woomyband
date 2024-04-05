import random

sea_adjectives = ["Abyssal", "Pelagic", "Benthic", "Halophilic", "Thalassic", "Planktonic", "Chitinous", "Piscine", "Littoral", "Molluscoid", "Pinniped", "Hydrothermal", "Sessile", "Vermarine", "Pleuronectiform", "Twilight", "Hadal", "Pacific", "Atlantic", "Indian", "Arctic", "Southern", "High-Pressure", "Tidal", "Ink", "Cloudy", "Marine", "Nautical", "Beached", "Drowned", "Sanitized", "Fuzzy", "Siamese Fighting", "Painted", "Boiling", "Melting", "Freezing", "Blood"]
marine_nouns = ["Bloom", "Nautilus", "Jellyfish", "Bioluminescence", "Gyre", "Krill", "Hydrozoan", "Phytoplankton", "Narwhal", "Estuary", "Brinepool", "Porifera", "Isopod", "Cephalopod", "Crustacean", "Tentacles", "Squid", "Octopus", "Sea", "Ocean", "Lake", "River", "Pond", "Stream", "Delta", "Depths", "Island", "Beach", "Fish", "Whale", "Dolphin", "Tide", "Moon", "Bubbles", "Cloud", "Seal", "Salmon", "Splash", "Bath", "Shower", "Zone", "Pool"]
genres = ["Rock", "Metal", "Pop", "Electronic", "Jazz", "Blues", "Funk", "Reggae", "Hip Hop", "Country", "Classical", "Punk", "Indie", "R&B", "Soul", "Folk", "Alternative", "Experimental", "Grunge", "Ska", "Industrial", "Disco", "Reggae"]

def generate_band_name():
    adjective = random.choice(sea_adjectives)
    noun = random.choice(marine_nouns)
    return f"{adjective} {noun}"

def generate_member():
    species = random.choices(
        ["Inkling", "Octoling"] * 50 +
        ["AI", "Cat", "Bear"] +
        ["Sanitized Octoling", "Fuzzy Octoling", "Octarian", "Salmonid", "Jelleton", "Jellyfish", "Shrimp", "Sea urchin", "Cuttlefish", "Nautilus", "Horseshoe crab", "Hagfish", "Lamprey", "Eel", "Shark", "Sea slug", "Sea cucumber"] * 10,
        k=1
    )[0]
    color = random.choice(["Blue", "Green", "Red", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White", "Turquoise", "Cyan", "Indigo", "Grey", "Gold", "Silver"])
    instrument = random.choice(["Guitar", "Bass", "Drums", "Keyboard", "Saxophone", "Trumpet", "Violin", "Cello", "Flute", "Vocals"])
    if instrument == "Vocals":
        return f"{color} {species} singing"
    else:
        return f"{color} {species} playing {instrument}"

if __name__ == "__main__":
    num_bands = int(input("How many bands are playing Inkopolis today? "))
    for _ in range(num_bands):
        print("Band Name:", generate_band_name())
        print("Genre:", random.choice(genres))
        num_members = random.randint(2, 5)
        has_vocalist = False
        print("Band Members:")
        for _ in range(num_members):
            member = generate_member()
            if "singing" in member:
                has_vocalist = True
            print("- " + member)
        if not has_vocalist:
            # Ensure there's at least one vocalist
            print("- " + generate_member())
        print()
