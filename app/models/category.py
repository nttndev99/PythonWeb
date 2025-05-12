from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from app.extensions import db


class Categories(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    logo_url: Mapped[str] = mapped_column(String(250), nullable=True)
    
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("Users", back_populates="categories")
        
    posts = relationship("Posts", back_populates="categories")
    

