from app.models.roles import Role
from app.models.user import Users
from app.extensions import db


class RoleService:
    @staticmethod
    def get_all_roles():
        return Role.query.all()

    @staticmethod
    def get_roles_by_ids(role_ids):
        return Role.query.filter(Role.id.in_(role_ids)).all()

class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        return Users.query.get(user_id)

    @staticmethod
    def assign_roles_to_user(user, role_ids: list[str]):
    # Get all roles by id
        roles = Role.query.filter(Role.id.in_(role_ids)).all()

        # Detect if there is an "admin" role in the list
        for r in roles:
            if r.name.lower() == 'admin':
                # Log or raise Exception if serious
                print(f"⚠️ Attempt to assign 'admin' role to user {user.id} was blocked.")
                roles.remove(r)

        user.roles = roles
        db.session.commit()
