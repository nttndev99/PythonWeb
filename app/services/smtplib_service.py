
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS_ADMIN = "nttndev99@gmail.com"
EMAIL_PASSWORD_ADMIN = "iohqiqvqrgrrtyug"

#----- Send email -----#
def send_email(name, email, phone, message):
    try:
        if name and email and phone and message is not None:
            body  = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            
            msg = MIMEMultipart()
            msg['Subject'] = "Contact Message"
            msg['From'] = email
            msg['To'] = EMAIL_ADDRESS_ADMIN
            
            text_part   = MIMEText(body , _charset='utf-8')
            msg.attach(text_part) 

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
                connection.starttls()
                connection.login(EMAIL_ADDRESS_ADMIN, EMAIL_PASSWORD_ADMIN)
                connection.sendmail(email, EMAIL_ADDRESS_ADMIN, msg.as_string())
        else:
            print(f"None data {e}")
    except Exception as e:
        print(f"Error data {e}")


