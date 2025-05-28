import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models import Base, Studio, Anime
from lib.db.setup_db import engine, Session

def seed():
    Base.metadata.create_all(engine)  
    session = Session()

    
    if not session.query(Studio).first():
        studios = [
            Studio(name="Studio Ghibli", location="Japan"),
            Studio(name="MAPPA", location="Japan"),
            Studio(name="Madhouse", location="Japan"),
            Studio(name="A-1 Pictures", location="Japan"),
            Studio(name="Studio Pierrot", location="Japan"),
        ]
        session.add_all(studios)
        session.commit()
        print("Studios seeded!")

   
    if not session.query(Anime).first():
        
        ghibli = session.query(Studio).filter_by(name="Studio Ghibli").first()
        mappa = session.query(Studio).filter_by(name="MAPPA").first()
        madhouse = session.query(Studio).filter_by(name="Madhouse").first()
        a1 = session.query(Studio).filter_by(name="A-1 Pictures").first()
        pierrot = session.query(Studio).filter_by(name="Studio Pierrot").first()

        anime_list = [
            Anime(title="Spirited Away", genre="Fantasy", studio_id=ghibli.id),
            Anime(title="Attack on Titan", genre="Action", studio_id=mappa.id),
            Anime(title="Frieren", genre="Fantasy", studio_id=madhouse.id),
            Anime(title="Eminence in the Shadow", genre="Action", studio_id=a1.id),
            Anime(title="Bleach", genre="Action", studio_id=pierrot.id),
        ]
        session.add_all(anime_list)
        session.commit()
        print("Anime seeded!")

    session.close()

if __name__ == "__main__":
    seed()
    print("Seeding complete.")

