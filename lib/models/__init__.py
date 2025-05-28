from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .studio import Studio
from .anime import Anime
from .review import Review

from ..db.setup_db import engine as ENGINE
from ..db.setup_db import Session
