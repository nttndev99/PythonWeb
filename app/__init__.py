import os
from flask import Flask
import psycopg2
from app.models.user import Users
from app.routes import register_routes
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor

from app.config import DB_NAME, HOST, PASSWORD, PORT, USERNAME, Config  
from app.extensions import db, login_manager
from app.seeds import seed_data

from flask_session import Session


# DB PGSQL
def create_database_if_not_exists():
    try:
        conn = psycopg2.connect(
            user=USERNAME,
            password=PASSWORD, 
            host=HOST, 
            port=PORT
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
        exists = cur.fetchone()
        if not exists:
            cur.execute(f"CREATE DATABASE {DB_NAME}")
            print(f" Database '{DB_NAME}' created.")
        else:
            print(f"ℹ Database '{DB_NAME}' already exists.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f" Error creating database: {e}")
        
    
        
def create_app():
    # Create database postgre
    create_database_if_not_exists()
    
    # Default
    app = Flask(__name__)
    app.config.from_object(Config)
    register_routes(app) #Blueprints
    
    # Lib
    CKEditor(app)
    Bootstrap(app)
    os.makedirs(os.path.join(Config.basedir, 'instance'), exist_ok=True)
    
    # Login initialization
    login_manager.init_app(app) 
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))
    
    # SQLAIchemy object initialization
    db.init_app(app)
    
    # Create table - model SQLAIchemy
    with app.app_context():
        try:
            from app.models import post, category, user, comment
            db.create_all()  
            seed_data() # Seed data
            print("Database and tables created successfully!")
        except Exception as e:
            print(f"Error: {e}")

    # Session FILE CSV
    Session(app)

    
    
    return app


