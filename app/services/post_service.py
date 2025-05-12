from app.models.post import Posts
from app.extensions import db
from bleach import clean

#----- Get id of the post -----#
def get_post_by_id(post_id):
    return Posts.query.get_or_404(post_id)

#----- Get all posts -----#
def get_all_posts():
    result = db.session.execute(db.select(Posts))
    posts = result.scalars().all()
    return posts

#----- Create posts -----#
def create_new_post(title, subtitle, datetime_str, img_url, body, author, categories):
    safe_body = clean(body)  # cleanify the body content (CKEditor)
    new_post = Posts(
        title=title, 
        subtitle=subtitle, 
        date=datetime_str,
        img_url=img_url,
        body=safe_body,
        author=author,
        categories=categories)
    db.session.add(new_post)
    db.session.commit()
    
#----- Update post -----#  
def update_post(post_id, title, subtitle, datetime_str, img_url, body, author, categories):
    post = Posts.query.get(post_id)
    if post:
        post.title = title
        post.subtitle = subtitle
        post.date = datetime_str
        post.img_url = img_url
        post.body = body
        post.author=author
        post.categories=categories
        db.session.commit()
        
#----- Delete post -----#   
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()



