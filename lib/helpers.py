from lib.db.setup_db import Session
from lib.models import Studio, Anime, Review

session = Session()

def list_anime():
    animes = session.query(Anime).all()
    if not animes:
        print("No anime found.")
    else:
        for anime in animes:
            print(f"{anime.id}. {anime.title} - Genre: {anime.genre}")

def add_anime():
    studios = session.query(Studio).all()
    if not studios:
        print("No studios found. Please add studios before adding anime.")
        return

    title = input("Enter anime title: ")
    genre = input("Enter anime genre: ")

    print("Studios:")
    for studio in studios:
        print(f"{studio.id}. {studio.name}")

    studio_id = input("Enter studio ID for this anime: ")
    studio = session.query(Studio).filter_by(id=studio_id).first()
    if not studio:
        print("Invalid studio ID. Anime not added.")
        return

    new_anime = Anime(title=title, genre=genre, studio_id=studio.id)
    session.add(new_anime)
    session.commit()
    print(f"Added anime: {title}")

def delete_anime():
    anime_id = input("Enter anime ID to delete: ")
    anime = session.query(Anime).filter_by(id=anime_id).first()
    if not anime:
        print("Anime not found.")
        return
    session.delete(anime)
    session.commit()
    print(f"Deleted anime: {anime.title}")

def list_studios():
    studios = session.query(Studio).all()
    if not studios:
        print("No studios found.")
    else:
        for studio in studios:
            print(f"{studio.id}. {studio.name} - Location: {studio.location}")

def add_review():
    animes = session.query(Anime).all()
    if not animes:
        print("No anime found to review.")
        return

    print("Anime List:")
    for anime in animes:
        print(f"{anime.id}. {anime.title}")

    anime_id = input("Enter anime ID to review: ")
    anime = session.query(Anime).filter_by(id=anime_id).first()
    if not anime:
        print("Invalid anime ID.")
        return

    try:
        rating = int(input("Enter rating (1-10): "))
        if rating < 1 or rating > 10:
            print("Rating must be between 1 and 10.")
            return
    except ValueError:
        print("Invalid rating. Must be a number between 1 and 10.")
        return

    comment = input("Enter review comment: ")

    review = Review(anime_id=anime.id, rating=rating, comment=comment)
    session.add(review)
    session.commit()
    print(f"Review added for {anime.title}.")

def exit_program():
    print("Exiting program...")
    exit(0)