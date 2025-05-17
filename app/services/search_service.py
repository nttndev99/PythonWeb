from sqlalchemy import false, or_
from app.models.category import Categories
from app.models.post import Posts
from sqlalchemy.orm import joinedload


def search_posts(query):
    if not query:
        return Posts.query.filter(false())
    return Posts.query.join(Categories).options(joinedload(Posts.categories)).filter(
        or_(
            Posts.title.ilike(f"%{query}%"),
            Categories.category_name.ilike(f"%{query}%")
        )
    )
    

