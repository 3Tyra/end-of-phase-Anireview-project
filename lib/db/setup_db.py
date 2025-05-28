from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///anireview_db.sqlite')
Session = sessionmaker(bind=engine)
