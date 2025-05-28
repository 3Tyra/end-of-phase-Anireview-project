from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from . import Base

class Studio(Base):
    __tablename__ = 'studios'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    animes = relationship("Anime", back_populates="studio", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Studio(name={self.name})>"
