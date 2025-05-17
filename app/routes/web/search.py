from flask import Blueprint,  flash, redirect, render_template, request, url_for
from app.services.paginated_service import get_paginated_search
from app.services.post_service import *
from app.services.search_service import search_posts
search_bp = Blueprint('search', __name__)

@search_bp.route("/search")
def search_category_post():
    query = request.args.get("q", "").strip()
    results_search = search_posts(query)
    page = request.args.get("page", 1, type=int)
    data = get_paginated_search(page=page, per_page=4, results_search=results_search)
    total = data["total"]

    if not query:
        flash("Please enter a search term.")
        return redirect(request.referrer or url_for("post.search"))
    
    if total == 1:
        return redirect(url_for("post.show_post", post_id=results_search[0].id))
    
    elif total > 1:
        flash(f"Found {total} results. Please refine your search.")
        return render_template("search_templates/more_results.html", query=query, count_posts=total, **data)
    
    elif total < 1:
        flash("No results found.")
        return render_template("search_templates/more_results.html", posts=results_search, query=query, is_empty=True, **data)
    
    else:
        return redirect(request.referrer or url_for("post.search_category_post"))
    
    
    
    
  
