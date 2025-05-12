from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.forms.forms import RegisterForm, LoginForm
from app.services.user_service import create_user, login_service
user_bp = Blueprint('user', __name__)


@user_bp.route("/register", methods=["GET", "POST"])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user(
            form.name.data, 
            form.email.data, 
            form.password.data)
        return redirect(url_for('blog.index'))
    else:
        print(form.errors)
    return render_template('user_templates/register.html', form=form)


@user_bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = login_service(form.email.data, form.password.data)
            if user:
                login_user(user)
                return redirect(url_for('user.secrets')) 
            else:
                flash("That email does not exist, please try again.")
    return render_template('user_templates/login.html', form=form, logged_in=current_user.is_authenticated)

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog.index'))

@user_bp.route('/secrets')
@login_required
def secrets():
    return render_template("user_templates/secrets.html", logged_in=True)

