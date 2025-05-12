from flask import Blueprint, jsonify, request
from app.models.post import Posts
from app.extensions import db   
blog_api_bp = Blueprint('blog_api', __name__)


@blog_api_bp.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Posts).order_by(Posts.title))
    all_posts = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_posts])


@blog_api_bp.route("/search")
def get_cafe_at_location():
    query_title = request.args.get("title")
    result = db.session.execute(db.select(Posts).where(Posts.title == query_title))
    all_posts = result.scalars().all()
    if all_posts:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_posts])
    else:
        return jsonify(error={"Not Found": "Error 404"}), 404
 

@blog_api_bp.route("/add", methods=["POST"])
def post_new_cafe():
    new_posts = Posts(
        title=request.form.get("title"),
        subtitle=request.form.get("subtitle"),
        body=request.form.get("body"),
    )
    db.session.add(new_posts)
    db.session.commit()
    return jsonify(response={"success": "Successfully."})


@blog_api_bp.route("/update-title/<int:post_id>", methods=["PATCH"])
def patch_new_title(post_id):
    new_title = request.args.get("new_title")
    post = db.session.get(Posts, post_id)
    if post:
        if new_title:
            post.title = new_title
            db.session.commit()
            return jsonify(response={"success": "Successfully"}), 200
        else:
            return jsonify(error={"Bad Request": "Please provide a 'new_price' in the query parameters."}), 400
    else:
        return jsonify(error={"Not Found": f"Sorry, a cafe with the id '{post_id}' was not found in the database."}), 404
    
    
@blog_api_bp.route("/delete/<int:post_id>", methods=["DELETE"])
def delete(post_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        try:
            post = db.session.get(Posts, post_id)  
            if post:
                db.session.delete(post)
                db.session.commit()
                return jsonify(response={"success": "Successfully deleted "}), 200
            else:
                return jsonify(error={"Not Found": f"Sorry, a cafe with the id '{post_id}' was not found in the database."}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify(error={"Internal Server Error": f"An unexpected error occurred: {str(e)}"}), 500
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
