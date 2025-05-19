from app.routes.web.post import post_bp
from app.routes.web.blog import blog_bp
from app.routes.web.category import category_bp
from app.routes.web.search import search_bp
from app.routes.web.user import user_bp
from app.routes.web.tools import tools_bp
from app.routes.web.codemirror import codemirror_bp
from app.routes.web.data_analysis import data_analysis_bp
from app.routes.web.permission import admin_bp

from app.routes.api.blog_api import blog_api_bp

def register_routes(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(tools_bp)
    app.register_blueprint(codemirror_bp)
    app.register_blueprint(data_analysis_bp)
    
    app.register_blueprint(blog_api_bp, url_prefix='/api')