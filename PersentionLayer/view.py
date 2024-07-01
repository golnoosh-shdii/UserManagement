from .edit_information import EditInformationFrame
from .home import HomeFrame
from .login import LoginFrame
from .sign_in import SigninFrame
from .user_management import UserManagement
from .window import Page


class MainView:
    def __init__(self):
        self.window = Page()

        self.frames = {}

        self.add_frames("edit", EditInformationFrame(self, self.window))
        self.add_frames("signin", SigninFrame(self, self.window))
        self.add_frames("user_management", UserManagement(self, self.window))
        self.add_frames("home", HomeFrame(self, self.window))
        self.add_frames("login", LoginFrame(self, self.window))

        self.window.show()

    def add_frames(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        self.frames[name].tkraise()
        return self.frames[name]
