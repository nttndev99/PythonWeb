from flask import Blueprint,render_template, request
from app.services.post_service import *
from app.services.smtplib_service import send_email
blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    data_card = get_posts_index()
    return render_template("blog_templates/index.html", data_card=data_card)

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