from flask import Blueprint,render_template, request
from app.services.post_service import *
from app.services.category_service import get_all_categories
from app.services.smtplib_service import send_email
blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    all_posts = get_all_posts()
    all_categories = get_all_categories()
    return render_template("blog_templates/index.html", all_posts=all_posts, all_categories=all_categories)

@blog_bp.route('/about')
def about():
    return render_template("blog_templates/about.html")

@blog_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            message = request.form["message"]
            print(name, email, phone, message)
            # send email
            data = request.form
            send_email(data["name"], data["email"], data["phone"], data["message"])
            return render_template("blog_templates/contact.html", msg_sent=True)
    else:   
        return render_template("blog_templates/contact.html", msg_sent=False)