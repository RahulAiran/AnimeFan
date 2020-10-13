import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from animefan.models import Anime

def run():
    fhand = open('animefan/anime.csv', encoding="utf8")
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Anime.objects.all().delete()

    # Format
    # anime_id name genre type episodes rating members

    for row in reader:
        # print(row)

        anime_id = int(row[0])
        name = row[1]
        genre = row[2]
        animetype = row[3]

        try:
            episodes = int(row[4])
        except:
            episodes = 1

        try:
            rating = float(row[5])
        except:
            rating = 0.0

        try:
            members = int(row[6])
        except:
            members = 0
        
        mood = row[7]

        anime = Anime.objects.create(
            anime_id = anime_id,
            name = name,
            genre = genre,
            animetype = animetype,
            episodes = episodes,
            rating = rating,
            members = members,
            mood = mood,
        )
        anime.save()
    print("Finished")