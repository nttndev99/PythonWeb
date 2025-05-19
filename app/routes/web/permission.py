from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_required, current_user
from functools import wraps

from app.forms.forms import UserRoleForm
from app.models.user import Users
from app.services.permission_service import RoleService, UserService

admin_bp = Blueprint('admin', __name__)

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated or not current_user.has_permission(permission):
                abort(403)
            return f(*args, **kwargs)
        return wrapped
    return decorator

@admin_bp.route('/users-list')
@login_required
@permission_required('admin')
def user_list():
    users = Users.query.all()
    return render_template('permission_teamplates/user-list.html', users=users, logged_in=True)

@admin_bp.route('/assign-roles/<int:user_id>/roles', methods=['GET', 'POST'])
@login_required
@permission_required('admin')  # only admin 
def assign_roles(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        abort(404)

    all_roles = RoleService.get_all_roles()
    
    filtered_roles = [r for r in all_roles if r.name.lower() != 'admin']
    print("Filtered roles:", [r.name for r in filtered_roles])

    form = UserRoleForm()
    form.roles.choices = [(str(role.id), role.name) for role in filtered_roles]

    if request.method == 'GET':
        form.roles.data = [str(role.id) for role in user.roles if role.name.lower() != 'admin']

    if form.validate_on_submit():
        selected_role_ids = form.roles.data  
        UserService.assign_roles_to_user(user, selected_role_ids)
        flash(f'Roles updated for user {user.name}', 'success')
        return redirect(url_for('admin.user_list', user_id=user.id))

    return render_template('permission_teamplates/assign-roles.html', form=form, user=user)




