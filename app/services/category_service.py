from flask_login import current_user
from sqlalchemy import or_
from app.models.category import Categories
from app.extensions import db
from app.models.post import Posts
from sqlalchemy.orm import joinedload

#----- Get all categories -----#
def get_all_categories():
    result = db.session.execute(db.select(Categories))
    categories = result.scalars().all()
    return categories

#----- Create -----#
def create_new_category(category_name, logo_url, author):
    new_category = Categories(
        category_name=category_name, 
        logo_url=logo_url,
        author=author
    )
    db.session.add(new_category)
    db.session.commit()
    
#----- Get id -----#
def get_category_by_id(category_id):
    return Categories.query.get_or_404(category_id)

#----- Update -----#  
def update_category(category_id, category_name, logo_url, author):
    category = Categories.query.get(category_id)
    if category:
        category.category_name = category_name
        category.logo_url = logo_url
        category.author = author
        db.session.commit()
        
#----- Delete -----#   
def delete_category(category_id):
    category = Categories.query.get_or_404(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()


#----- Get category post -----#   
def get_category_posts(category_id):
    posts = Posts.query.filter_by(categories_id=category_id).all()
    return posts