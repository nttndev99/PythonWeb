import os

USERNAME = "postgres"
PASSWORD = "123456789"
HOST = "localhost"
PORT = "5432"
DB_NAME = "learn_blog_app"
   
class Config:
    # Flask-WTF
    SECRET_KEY = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"  
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # # SQLlite
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance', 'learn_blog.db')}"
    
    # Flask - PostgreSQL
    #SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOGO_IMAGES_FOLDER = 'app/static/assets/logo'  
    POSTS_IMAGES_FOLDER = 'app/static/assets/post_images'  
    
    # Session FILE CSV
    SESSION_TYPE = 'filesystem'
