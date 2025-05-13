import os

from flask import request
from app.models.post import ImagesPost, Posts
from app.extensions import db
from bleach import clean
from werkzeug.utils import secure_filename
from pathlib import Path
from app.config import Config

#----- Get id of the post -----#
def get_post_by_id(post_id):
    return Posts.query.get_or_404(post_id)

#----- Get all posts -----#
def get_all_posts():
    result = db.session.execute(db.select(Posts))
    posts = result.scalars().all()
    return posts


#----- Create posts -----#
def create_new_post(title, subtitle, datetime_str, body, author, categories, images):
    safe_body = clean(body)  # cleanify the body content (CKEditor)
    new_post = Posts(
        title=title, 
        subtitle=subtitle, 
        date=datetime_str,
        body=safe_body,
        author=author,
        categories=categories)
    db.session.add(new_post)
    db.session.flush()
    for image in images:
        if image:
            upload_folder = Path(Config.POSTS_IMAGES_FOLDER) 
            upload_folder.mkdir(parents=True, exist_ok=True)
            
            filename = secure_filename(image.filename)
            filepath = upload_folder / filename
            image.save(filepath)

            img = ImagesPost(filename=filename, post=new_post)
            db.session.add(img)
    db.session.commit()
    return new_post

#----- Update post -----#  
def update_post(datetime_str, author, categories, post, form):
    # Delete old images
    for img_form in form.old_images.entries:
        image_id = img_form.form.id.data
        delete_image = img_form.delete.data
        
        print(image_id)
        print(delete_image)
        
        if delete_image:            
            image = ImagesPost.query.get(image_id)
            if image:
                upload_folder = Path(Config.POSTS_IMAGES_FOLDER) 
                upload_folder.mkdir(parents=True, exist_ok=True)
                
                filename = secure_filename(image.filename)
                filepath = upload_folder / filename
                
                if os.path.exists(filepath):
                    os.remove(filepath)
                    
                db.session.delete(image)

    # Update posts
    post.title = form.title.data
    post.subtitle = form.subtitle.data
    post.body = form.body.data
    post.date = datetime_str
    post.author = author
    post.categories = categories

    # Upload new images
    upload_folder = Path(Config.POSTS_IMAGES_FOLDER)
    upload_folder.mkdir(parents=True, exist_ok=True)

    for image in request.files.getlist(form.images.name):
        if image and image.filename:
            filename = secure_filename(image.filename)
            filepath = upload_folder / filename
            image.save(filepath)
            db.session.add(ImagesPost(filename=filename, post=post))

    db.session.commit()
    
    
    
#----- Delete post -----#   
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()



