
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from app.extensions import db
from app.models.roles import roles_users

class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)    
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    # 1 - n    
    categories = relationship("Categories", back_populates="author")
    # 1 - n 
    posts = relationship("Posts", back_populates="author")
    # 1 - n 
    comments = relationship("Comment", back_populates="comment_author")
    # n - n 
    roles = relationship('Role', secondary=roles_users, back_populates='users')
    def has_permission(self, permission):
        return any(role.has_permission(permission) for role in self.roles)


