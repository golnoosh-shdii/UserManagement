from DataAccessLayer.user_data_access import UserDataAccess


class UserBusiness:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return None, "Invalid Request."

        user = self.user_data_access.get_user(username, password)

        if user:
            if user.active == 0:
                return None, "Your account deactive."
            else:
                return user, None
        else:
            return None, "Invalid Username or Password."

    def get_users(self, current_user):
        if current_user.role_id != "Admin":
            return None, "Invalid Access"

        if current_user.active == 0:
            return None, "Your account deactive."

        users = self.user_data_access.get_users(current_user.id)
        return users, None

    def activate(self, current_user, user_id):
        if current_user.role_id != "Admin":
            return "Invalid Access"

        if current_user.active == 0:
            return "Your account deactive."

        self.user_data_access.update_status(user_id, 1)

        return None

    def deactive(self, current_user, user_id):
        if current_user.role_id != "Admin":
            return "Invalid Access"

        if current_user.active == 0:
            return "Your account deactive."

        self.user_data_access.update_status(user_id, 0)

        return None

    def signin(self, firstname, lastname, username, password):
        usernames = self.user_data_access.return_all_username()

        if len(firstname) < 3 or len(lastname) < 3 or len(username) < 3 or len(password) < 3:
            return None, "Fill in the blank fields"
        else:
            for all_username in usernames:
                if username == all_username:
                    return None, "Duplicate Username"
                else:
                    self.user_data_access.create_account(firstname, lastname, username, password)
                    return "Your Data Saved", None

    def edit_info(self, current_user, firstname, lastname, username):
        usernames = self.user_data_access.return_all_username()

        if current_user.active == 0:
            return None, "Your Account Deactivate"
        if len(firstname) < 3 or len(lastname) < 3 or len(username) < 3:
            return None, "Fill in the blank fields"
        else:
            for all_username in usernames:
                if username == all_username:
                    return None, "Duplicate Username"
                else:
                    self.user_data_access.edit(firstname, lastname, username, current_user.id)
                    return "Your Data Changed", None
