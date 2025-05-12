
from datetime import datetime
from app.models.category import Categories
from app.models.post import Posts
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
            user = Users(
                id=1,
                name='Admin',
                email='admin@email.com',
                password='pbkdf2:sha256:1000000$j73phBAC$46592241d998f37088bb32bcd524dc49726d5d659bab21f911d6adf2c00cb296'
            )
            category1 = Categories(
                id=1,
                category_name='Programming Language', 
                logo_url='test',
                author=user
            )            
            category2 = Categories(
                id=2,
                category_name='Tools',
                logo_url='test',
                author=user
            )            
            category3 = Categories(
                id=3,
                category_name='Design Principles',
                logo_url='test',
                author=user     
            )     
            category4 = Categories(
                id=4,
                category_name='Architectual Patterns',
                logo_url='test',
                author=user     
            )            
            post1 = Posts(
                title='Python',
                subtitle='Test',
                date= time_str,
                img_url='Test',
                body='Test',
                author=user,
                categories=category1
            )  
            post2 = Posts(
                title='Java',
                subtitle='Test',
                date= time_str,
                img_url='Test',
                body='Test',
                author=user,
                categories=category1)        
            post3 = Posts(
                title='Github',
                subtitle='Test',
                date= time_str,
                img_url='Test',
                body='test',
                author=user,
                categories=category2) 
            post4 = Posts(
                title='Github2',
                subtitle='Test',
                date= time_str,
                img_url='Test',
                body='test',
                author=user,
                categories=category2)
            db.session.add_all([user, category1, category2, category3, category4, post1, post2, post3, post4])
            db.session.commit()
            print("✅ Seed data created successfully!")
        else:
            print("ℹ️ Seed data already exists.")
    except Exception as e:
        print(f"❌ Error seeding data: {e}")