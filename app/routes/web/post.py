from datetime import datetime
from flask import Blueprint,  flash, redirect, render_template, request, url_for
from flask_login import current_user
from app.forms.forms import CommentForm, CreatePostForm
from app.models.category import Categories
from app.services.paginated_service import get_paginated_posts
from app.services.post_service import *
from app.services.comment_service import create_comment
from functools import wraps
from flask import abort
post_bp = Blueprint('post', __name__)



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
  
@post_bp.route('/all_posts')
def all_posts():
    page = request.args.get("page", 1, type=int)
    data = get_paginated_posts(page=page, per_page=6)
    return render_template("post_templates/all_posts.html", **data)

@post_bp.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = get_post_by_id(post_id)
    current_time = datetime.now()
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    # Add the CommentForm to the route
    comment_form = CommentForm()
    # Only allow logged-in users to comment on posts
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("user.login"))
        create_comment(
            text=comment_form.comment_text.data,
            date=time_str,
            comment_author=current_user,
            parent_post=requested_post
        )
    if requested_post is None:
        return render_template("404.html"), 404
    return render_template("post_templates/post.html", post=requested_post, urrent_user=current_user, form=comment_form)

@post_bp.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()

    current_time = datetime.now()
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    author = current_user
    form.categories.choices = [(c.id, c.category_name) for c in Categories.query.all()]
    

    if form.validate_on_submit():
        categories = Categories.query.get(form.categories.data)
        create_new_post(
            form.title.data, 
            form.subtitle.data, 
            time_str,
            form.body.data,
            author,
            categories,
            images=form.images.data
        )
        flash("Create success!", "success")
        return redirect(url_for('post.all_posts'))
    else:
        print(form.errors)
    return render_template('post_templates/make-post.html', form=form)


@post_bp.route('/update-post/<int:post_id>', methods=['GET', 'POST'])
def update_posts(post_id):
    post = get_post_by_id(post_id)
    if not post:
        return redirect(url_for('post.all_posts'))

    form = CreatePostForm(obj=post)
    form.categories.choices = [(c.id, c.category_name) for c in Categories.query.all()]

    form.title.data = post.title
    form.subtitle.data = post.subtitle
    form.body.data = post.body
    form.categories.data = post.categories.id if post.categories else None
    if request.method == 'GET':
        for image in post.images:
            form.old_images.append_entry({'id': image.id, 'delete': False})

    if form.validate_on_submit():
        update_post(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    current_user,
                    Categories.query.get(form.categories.data),
                    post,
                    form)
        return redirect(url_for('post.all_posts'))
    else:
        print("Form errors:", form.errors) 

    return render_template('post_templates/make-post.html', form=form, post=post, is_update=True)


@post_bp.route('/delete-post/<int:post_id>', methods=['POST'])
@admin_only
def delete_post_route(post_id):
    success, message = delete_post(post_id)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('post.all_posts'))





