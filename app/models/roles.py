from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.extensions import db

roles_users = Table(
    'roles_users',
    db.Model.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

class Role(db.Model):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    permissions = Column(String(500))  # save permissions JSON or csv
    
    users = relationship('Users', secondary=roles_users, back_populates='roles')
    
    def has_permission(self, permission):
        # permissions save wwith csv string: "view_post,edit_post,delete_post"
        return permission in self.permissions.split(',')