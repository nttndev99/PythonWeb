import os
from pathlib import Path
from flask_login import current_user
from sqlalchemy import or_
from app.config import Config
from app.models.category import Categories
from app.extensions import db
from app.models.post import Posts
from sqlalchemy.orm import joinedload
from werkzeug.utils import secure_filename

#----- Get all categories -----#
def get_all_categories():
    result = db.session.execute(db.select(Categories))
    categories = result.scalars().all()
    return categories

#----- Create -----#
def create_new_category(category_name, logo_file , author):
    new_category = Categories(
        category_name=category_name, 
        author=author
    )
    db.session.add(new_category)
    if logo_file  and logo_file.filename:
        upload_folder = Path(Config.LOGO_IMAGES_FOLDER) 
        upload_folder.mkdir(parents=True, exist_ok=True)

        filename = secure_filename(logo_file.filename)
        logo_path = upload_folder / filename

        logo_file.save(logo_path)
        
        new_category.logo_url = filename    
        
    db.session.commit()
    return new_category

#----- Get id -----#
def get_category_by_id(category_id):
    return Categories.query.get_or_404(category_id)

#----- Update -----#  
def update_category(category_id, category_name, logo_file, author):
    category = Categories.query.get(category_id)
    if category:
        category.category_name = category_name
        category.author = author
        if logo_file and logo_file.filename:
            upload_folder = Path(Config.LOGO_IMAGES_FOLDER)
            upload_folder.mkdir(parents=True, exist_ok=True)

            # Remove old logo
            old_logo_path = upload_folder / category.logo_url
            if old_logo_path.exists():
                os.remove(old_logo_path)

            # Save new logo
            filename = secure_filename(logo_file.filename)
            logo_path = upload_folder / filename
            logo_file.save(logo_path)

            category.logo_url = filename
        
        db.session.commit()
    return category

#----- Delete -----#   
def delete_category(category_id):
    category = Categories.query.get_or_404(category_id)
    if not category:
        return False, "Category does not exist."
    if category.posts: 
        return False, "Cannot delete because there are still related posts."

    db.session.delete(category)
    db.session.commit()
    return True, "Category deleted."

#----- Get posts in category -----#   
def get_category_posts(category_id):
    posts = Posts.query.filter_by(categories_id=category_id).all()
    return posts