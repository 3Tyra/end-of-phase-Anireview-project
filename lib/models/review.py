from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    anime_id = Column(Integer, ForeignKey('animes.id'))
    rating = Column(Integer)
    comment = Column(String)

    anime = relationship("Anime", back_populates="reviews")

    def __repr__(self):
        return f"<Review(rating={self.rating}, comment={self.comment})>"