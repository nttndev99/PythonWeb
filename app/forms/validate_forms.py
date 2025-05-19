from wtforms.validators import ValidationError
from email_validator import validate_email, EmailNotValidError
import phonenumbers
import re

def validate_email_field(form, field):
    try:
        field.data = validate_email(field.data).email  
    except EmailNotValidError as e:
        raise ValidationError(f"Invalid Email: {e}")
    
    
def validate_phone(form, field):
    try:
        phone = phonenumbers.parse(field.data, "VN")  
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Invalid Phone.")
    except:
        raise ValidationError("Invalid Phone.")
    
    
def validate_password(form, field):
    password = field.data
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least 1 uppercase letter.")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least 1 lowercase letter.")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least 1 digit.")
    if not re.search(r"[!@#$%^&*()_+=-]", password):
        raise ValidationError("Password must contain at least 1 special character.")