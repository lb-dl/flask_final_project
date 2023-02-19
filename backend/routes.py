from flask.views import MethodView

from api.users_api import get_all_users, get_one_user, create_user, update_user, delete_user


class Users(MethodView):
    """
    The class represents a group of endpoints dealing with users
    """

    def get(self, user_id=None):
        """
        Get users
        """
        if not user_id:
            return get_all_users()
        return get_one_user(user_id)

    def post(self):
        """
        create a user
        """
        return create_user()

    def patch(self, user_id):
        """
        Update an existing user
        """
        return update_user(user_id)

    def delete(self, user_id):
        """
         Delete an existing user
        """
        return delete_user(user_id)