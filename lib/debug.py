import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models import Anime, Studio, Review, Session, Base, ENGINE

def seed_and_print_all():
    
    Base.metadata.create_all(ENGINE)
    session = Session()

    
    studios_data = [
        {"name": "Studio Ghibli", "location": "Japan"},
        {"name": "MAPPA", "location": "Japan"},
        {"name": "Madhouse", "location": "Japan"},
        {"name": "A-1 Pictures", "location": "Japan"},
        {"name": "Studio Pierrot", "location": "Japan"},
    ]

    for data in studios_data:
        studio = session.query(Studio).filter_by(name=data["name"]).first()
        if not studio:
            studio = Studio(name=data["name"], location=data["location"])
            session.add(studio)
            print(f"Added studio: {studio}")
    session.commit()

    
    studio_map = {studio.name: studio.id for studio in session.query(Studio).all()}

    
    animes_data = [
        {"title": "Spirited Away", "genre": "Fantasy", "studio": "Studio Ghibli"},
        {"title": "Attack on Titan", "genre": "Action", "studio": "MAPPA"},
        {"title": "Frieren", "genre": "Fantasy", "studio": "Madhouse"},
        {"title": "Eminence in the Shadow", "genre": "Action", "studio": "A-1 Pictures"},
        {"title": "Bleach", "genre": "Action", "studio": "Studio Pierrot"},
    ]

    for data in animes_data:
        anime = session.query(Anime).filter_by(title=data["title"]).first()
        if not anime:
            anime = Anime(title=data["title"], genre=data["genre"], studio_id=studio_map[data["studio"]])
            session.add(anime)
            print(f"Added anime: {anime}")
    session.commit()

    
    anime_map = {anime.title: anime.id for anime in session.query(Anime).all()}

    
    reviews_data = [
        {"anime": "Spirited Away", "rating": 9, "comment": "Magical and emotional."},
        {"anime": "Attack on Titan", "rating": 10, "comment": "Epic story and animation."},
        {"anime": "Frieren", "rating": 8, "comment": "Thoughtful fantasy with great art."},
        {"anime": "Eminence in the Shadow", "rating": 7, "comment": "Dark and cool, fun watch."},
        {"anime": "Bleach", "rating": 9, "comment": "Classic with epic fights!"},
    ]

    for data in reviews_data:
        anime_id = anime_map[data["anime"]]
        review = session.query(Review).filter_by(anime_id=anime_id).first()
        if not review:
            review = Review(anime_id=anime_id, rating=data["rating"], comment=data["comment"])
            session.add(review)
            print(f"Added review: {review}")
    session.commit()

    
    print("\n=== All Studios ===")
    for studio in session.query(Studio).all():
        print(studio)

    print("\n=== All Anime ===")
    for anime in session.query(Anime).all():
        print(anime)

    print("\n=== All Reviews ===")
    for review in session.query(Review).all():
        print(review)

    
    print("\n=== Anime Details with Studios and Reviews ===")
    for anime in session.query(Anime).all():
        studio = session.query(Studio).filter_by(id=anime.studio_id).first()
        print(f"Title: {anime.title} | Genre: {anime.genre} | Studio: {studio.name if studio else 'Unknown'}")

        reviews = session.query(Review).filter_by(anime_id=anime.id).all()
        if reviews:
            for r in reviews:
                print(f"  Review: Rating {r.rating} - {r.comment}")
        else:
            print("  No reviews yet.")
        print()

    session.close()

if __name__ == "__main__":
    seed_and_print_all()
