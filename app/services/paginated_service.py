
from sqlalchemy import select
from app.models.post import Posts
from app.models.category import Categories
from app.extensions import db
from app.services.search_service import search_posts


def get_pagination_data(page: int, total_pages: int, max_visible_pages: int = 6):
    if total_pages <= max_visible_pages:
        return list(range(1, total_pages + 1))
    side = (max_visible_pages - 4) // 2  
    start = max(2, page - side)
    end = min(total_pages - 1, page + side)

    if start <= 2:
        start = 2
        end = start + max_visible_pages - 4
    elif end >= total_pages - 1:
        end = total_pages - 1
        start = end - max_visible_pages + 4
        if start < 2:
            start = 2
    pages = [1]
    if start > 2:
        pages.append("...")
    pages += list(range(start, end + 1))
    if end < total_pages - 1:
        pages.append("...")
    pages.append(total_pages)
    return pages

def get_paginated_posts(page=1, per_page=10):
    offset_val = (page - 1) * per_page

    stmt = db.select(Posts).offset(offset_val).limit(per_page)
    result = db.session.execute(stmt)
    posts = result.scalars().all()

    total = db.session.execute(db.select(db.func.count()).select_from(Posts)).scalar()
    total_pages = (total + per_page - 1) // per_page

    pages = get_pagination_data(page, total_pages)

    return {
        "posts": posts,
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "pages": pages,  
    }
    
def get_paginated_categories(page=1, per_page=10):
    offset_val = (page - 1) * per_page

    stmt = db.select(Categories).offset(offset_val).limit(per_page)
    result = db.session.execute(stmt)
    all_categories = result.scalars().all()

    total = db.session.execute(db.select(db.func.count()).select_from(Categories)).scalar()
    total_pages = (total + per_page - 1) // per_page

    pages = get_pagination_data(page, total_pages)

    return {
        "all_categories": all_categories,
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "pages": pages,  
    }

def get_paginated_search(page=1, per_page=10, results_search=None):
    offset_val = (page - 1) * per_page

    stmt = results_search.offset(offset_val).limit(per_page)
    all_categories_posts = stmt.all()

    total = results_search.order_by(None).count()  
    total_pages = (total + per_page - 1) // per_page

    pages = get_pagination_data(page, total_pages)

    return {
        "all_categories_posts": all_categories_posts,
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "pages": pages,  
    }
   
def get_paginated_category_posts(page=1, per_page=10, results_search=None):
    offset_val = (page - 1) * per_page

    stmt = results_search.offset(offset_val).limit(per_page)
    all_categories_posts = stmt.all()

    total = results_search.order_by(None).count()  
    total_pages = (total + per_page - 1) // per_page

    pages = get_pagination_data(page, total_pages)

    return {
        "all_categories_posts": all_categories_posts,
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "pages": pages,  
    } 
    
