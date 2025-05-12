from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user
from app.forms.forms import  CreateCategoryForm
from app.services.paginated_service import get_paginated_categories
from app.services.post_service import *
from app.services.category_service import create_new_category, delete_category, get_category_by_id, get_category_posts, update_category

from functools import wraps
from flask import abort
category_bp = Blueprint('category', __name__)


#Create admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)        
    return decorated_function


@category_bp.route('/all_categories')
def all_categories():
    page = request.args.get("page", 1, type=int)
    data = get_paginated_categories(page=page, per_page=8)
    return render_template("category_templates/all_categories.html", **data)


@category_bp.route("/new-category", methods=["GET", "POST"])
@admin_only
def add_new_category():
    form = CreateCategoryForm()
    if form.validate_on_submit():
        create_new_category(
            form.category_name.data, 
            form.logo_url.data, 
            current_user)
        return redirect(url_for('blog.index'))
    else:
        print(form.errors)
    return render_template('category_templates/make-category.html', form=form)


@category_bp.route('/update-category/<int:category_id>', methods=['GET', 'POST'])
def update(category_id):
    form = CreateCategoryForm()
    category = get_category_by_id(category_id)
    if not category:
        return redirect(url_for('blog.index'))
    if request.method == 'GET':
        form.category_name.data = category.category_name
        form.logo_url.data = category.logo_url
        current_user
    if form.validate_on_submit():
        update_category(category_id, form.category_name.data, form.logo_url.data, current_user)
        return redirect(url_for('blog.index'))
    return render_template('category_templates/make-category.html', form=form, is_update=True)


@category_bp.route('/delete/<int:category_id>')
@admin_only
def delete(category_id):
    delete_category(category_id)
    return redirect(url_for('blog.index'))


@category_bp.route('/category/<int:category_id>')
def category_posts(category_id):    
    categories = get_category_by_id(category_id)
    posts = get_category_posts(category_id)
    count_posts = len(posts)
    return render_template('category_templates/category_posts.html', categories=categories, posts=posts, count_posts=count_posts)

