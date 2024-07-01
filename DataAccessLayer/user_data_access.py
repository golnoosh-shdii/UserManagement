import sqlite3

from CommanLayer.user import User


class UserDataAccess:
    def __init__(self):
        self.database_name = "usermanagment.db"

    def get_user(self, username, password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
             SELECT id,
                firstname,
                lastname,
                username,
                active,
                role_id
             FROM user
             WHERE username= ?
             AND   password = ?""", [username, password]).fetchone()

        if data:
            user = User(data[0], data[1], data[2], data[3], None, data[4], data[5])
            return user
        else:
            return None

    def get_users(self, current_user_id):
        users = []
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
            Select  id
            ,       firstname
            ,       lastname
            ,       username
            ,       active
            ,       role_id
            From    User
            Where   id  !=  ?""", [current_user_id]).fetchall()

            for item in data:
                user = User(item[0], item[1], item[2], item[3], None, item[4], item[5])
                users.append(user)

            return users

    def update_status(self, user_id, active):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            Update  User
            Set     active  =   ?
            Where   id      =   ?""", [active, user_id])

            connection.commit()

    def create_account(self, firstname, lastname, username, password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            INSERT INTO user (
                     firstname,
                     lastname,
                     username,
                     password,
                     active,
                     role_id
                 )
                 VALUES (
                     '{firstname}',
                     '{lastname}',
                     '{username}',
                     '{password}',
                     '{0}',
                     '{"Default User"}'
                            );""")
            connection.commit()

    def return_all_username(self):
        usernames = []

        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                        SELECT id,
                            firstname,
                            lastname,
                            username,
                            active,
                            role_id
                        FROM user""").fetchall()
            for item in data:
                usernames.append(item[3])
            return usernames

    def edit(self, firstname, lastname, username,current_user_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                        UPDATE user
                        SET    firstname = ?,
                               lastname  = ?,
                               username  = ?
                        WHERE  id        = ?       """, [firstname, lastname, username,current_user_id])
            connection.commit()
