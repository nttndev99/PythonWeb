from flask import Blueprint, jsonify, render_template, request
from app.services.codemirror_service import process_code

codemirror_bp = Blueprint('codemirror', __name__)


@codemirror_bp.route('/codemirror')
def editor():
    return render_template('code_mirror_templates/editor.html')


@codemirror_bp.route("/run", methods=["POST"])
def run_code():
    data = request.json
    code = data.get("code", "")
    result = process_code(code)
    return jsonify({"result": result})