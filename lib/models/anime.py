from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Anime(Base):
    __tablename__ = 'animes'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    studio_id = Column(Integer, ForeignKey('studios.id'), nullable=False)
    
    # Relationship to Studio
    studio = relationship("Studio", back_populates="animes")
    reviews = relationship("Review", back_populates="anime", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Anime(title={self.title}, genre={self.genre})>"
