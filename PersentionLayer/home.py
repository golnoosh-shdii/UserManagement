
from ttkbootstrap import SUCCESS, DANGER, Frame, Label, Button


class HomeFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.user_management_button = None

        self.current_user = None

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Wellcame")
        self.header.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.edit_button = Button(self, text="Edit Information", command=self.edit_button_clicked, bootstyle=SUCCESS)
        self.edit_button.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

        self.logout_button = Button(self, text="Logout", command=self.logout, bootstyle=DANGER)
        self.logout_button.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

    def logout(self):
        self.view.switch("login")

    def set_current_user(self, user):
        self.current_user = user
        self.header.config(text=f"Welcome, {user.firstname} {user.lastname}")

        if self.current_user.role_id == "Admin":
            if not self.user_management_button:
                self.user_management_button = Button(self, text="User Management", command=self.show_user_management)
                self.user_management_button.grid(row=1, column=0, pady=10, padx=10, sticky="ew")
        else:
            if self.user_management_button:
                self.user_management_button.destroy()
                self.user_management_button = None

    def show_user_management(self):
        user_management_frame = self.view.switch("user_management")
        user_management_frame.load_data(self.current_user)

    def edit_button_clicked(self):
        edit_informaion_frame = self.view.switch("edit")
        edit_informaion_frame.set_current_user_for_edit_information_frame(self.current_user)
