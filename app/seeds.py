
from datetime import datetime
from app.models.category import Categories
from app.models.post import ImagesPost, Posts
from app.models.roles import Role
from app.models.user import Users
from app.extensions import db

def seed_data():
    current_time = datetime.now()
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    has_users = Users.query.first() is not None
    has_posts = Posts.query.first() is not None
    has_categories = Categories.query.first() is not None
    
    try:
        if not has_users and not has_posts and not has_categories:
            roles1 = Role(id=1, name="admin", permissions="admin")           
            roles2 = Role(id=2, name="editor", permissions="editor")          
            roles3 = Role(id=3, name="viewer", permissions="viewer")
            user = Users(
                id=1,
                name='ADMIN',
                email='ADMIN@gmail.com', #ADMIN@gmail.com123
                password='pbkdf2:sha256:1000000$tJxO7kem$b1f9b758dde49495da561ecf06a319762ff9e22d1ab63c5c7f499e3b35789747',
                roles = [roles1]
            )
            category1 = Categories(id=1, category_name='Programming Language',  logo_url='programming-logo.png', author=user)            
            category2 = Categories(id=2, category_name='Website Programming', logo_url='logo-app.png', author=user)            
            category3 = Categories(id=3, category_name='Database', logo_url='cloud-database.png', author=user)     
            category4 = Categories(id=4, category_name='Data Science', logo_url='data-science.png', author=user)              
            category5 = Categories(id=5, category_name='Tools', logo_url='tools.png', author=user)                   
            category6 = Categories(id=6, category_name='Design Principles', logo_url='prototype.png', author=user)            
            post1 = Posts(title='Python', subtitle='Python', date= time_str, body='Python', author=user, categories=category1)  
            post2 = Posts(title='Flask', subtitle='Flask', date= time_str, body='Flask', author=user, categories=category2)        
            post3 = Posts(title='SQLite', subtitle='SQLite', date= time_str, body='SQLite', author=user, categories=category3) 
            post4 = Posts(title='PostgreSQL', subtitle='PostgreSQL', date= time_str, body='PostgreSQL', author=user, categories=category3)            
            post5 = Posts(title='Github', subtitle='Github', date= time_str, body='Github', author=user, categories=category5)            
            post6 = Posts(title='Anaconda', subtitle='Anaconda', date= time_str, body='Anaconda', author=user, categories=category4)            
            post7 = Posts(title='Pandas Library', subtitle='Pandas Library', date= time_str, body='Pandas Library', author=user, categories=category4)            
            post8 = Posts(title='NumPy Library', subtitle='NumPy Library', date= time_str, body='NumPy Library', author=user, categories=category4)            
            post9 = Posts(title='Matplotlib', subtitle='Matplotlib', date= time_str, body='Matplotlib', author=user, categories=category4)            
            post10 = Posts(title='Jupyter Notebook', subtitle='Jupyter Notebook', date= time_str, body='Jupyter Notebook', author=user, categories=category5)
            img1 = ImagesPost(filename="Python-Programming-Language.png", post=post1)
            img2 = ImagesPost(filename="pgsql.png", post=post4)
            img3 = ImagesPost(filename="github.jpeg", post=post5)
            img4 = ImagesPost(filename="anaconda.jpg", post=post6)
            img5 = ImagesPost(filename="Pandas-Library-of-Python.jpeg", post=post7)
            img6 = ImagesPost(filename="NumPy.jpeg", post=post8)
            img7 = ImagesPost(filename="matplotlib.jpeg", post=post9)
            img8 = ImagesPost(filename="JupyterLab.jpeg", post=post10)
            img9 = ImagesPost(filename="Flask.png", post=post2)
            img10 = ImagesPost(filename="sqlite.jpg", post=post3)
            db.session.add_all([user, 
                                category1, category2, category3, category4, category5, category6, 
                                post1, post2, post3, post4, post5, post6, post7, post8, post9, post10,
                                img1, img2, img3, img4, img5, img6, img7, img8, img9, img10,
                                roles1, roles2, roles3])
            db.session.commit()
            print("✅ Seed data created successfully!")
        else:
            print("ℹ️ Seed data already exists.")
    except Exception as e:
        print(f"❌ Error seeding data: {e}")