from flask import flash
from app.models.roles import Role
from app.models.user import Users
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(name, email, password):
    hash_and_salted_password = generate_password_hash(
            password,
            method='pbkdf2:sha256',
            salt_length=8)
    new_user = Users(name=name, email=email, password=hash_and_salted_password)
    viewer_role = Role.query.filter_by(name="viewer").first()
    if viewer_role:
        new_user.roles.append(viewer_role)
    else:
        flash("⚠️ Role 'viewer' not found in DB. Please seed roles first.")
    db.session.add(new_user)
    db.session.commit()


def login_service(email, password):
    user = Users.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
        

    
 

