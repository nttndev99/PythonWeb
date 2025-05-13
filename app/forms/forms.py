from wtforms import BooleanField, FieldList, FormField, HiddenField, MultipleFileField, PasswordField, SelectField, StringField, TextAreaField, ValidationError
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from app.config import Config
from flask_wtf.file import FileField, FileAllowed

class CreateCategoryForm(FlaskForm):
    category_name = StringField("Category Name", validators=[DataRequired()])
    logo_file = FileField("Logo", validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'])])
    submit = SubmitField("Submit") 

class DeleteImageForm(Form):
    id = HiddenField()
    delete = BooleanField("Delete")  
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    images = MultipleFileField("Images", validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], "Only images allowed")])
    categories = SelectField("Categories", coerce=int, validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    old_images = FieldList(FormField(DeleteImageForm), min_entries=0)
    submit = SubmitField("Submit Post")  
    
    
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")
     
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    
class CommentForm(FlaskForm):
    comment_text = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")