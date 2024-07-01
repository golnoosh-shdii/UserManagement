class User:
    def __init__(self,id, firstname,lastname,username,password,active,role_id):
        self.id = id
        self.firstname=firstname
        self.lastname=lastname
        self.username= username
        self.password=password
        self.active = active
        self.role_id=role_id
