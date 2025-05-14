from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from app.extensions import db

class Posts(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(String(500), nullable=False)

    images: Mapped[list["ImagesPost"]] = relationship("ImagesPost", back_populates="post", cascade="all, delete-orphan")

    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("Users", back_populates="posts")

    categories_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("categories.id"))
    categories = relationship("Categories", back_populates="posts")

    comments = relationship("Comment", back_populates="parent_post", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class ImagesPost(db.Model):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    filename: Mapped[str] = mapped_column(String(200))
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("posts.id"))
    post: Mapped[Posts] = relationship("Posts", back_populates="images")