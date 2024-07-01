from tkinter import messagebox

from ttkbootstrap import Frame, Label, Entry, Button, END, LabelFrame, SUCCESS, INFO

from BusinessLogicLayer.user_business import UserBusiness


class LoginFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)
        self.user_business = UserBusiness()
        self.view = view
        self.grid_columnconfigure(0, weight=1)

        self.header = LabelFrame(self, text="Login with You Account", )
        self.header.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.header.grid_columnconfigure(1, weight=1)

        self.username_label = Label(self.header, text="Username : ")
        self.username_label.grid(row=0, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_entry = Entry(self.header)
        self.username_entry.grid(row=0, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self.header, text="Password : ")
        self.password_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.password_entry = Entry(self.header, show="*")
        self.password_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.login_button = Button(self.header, text="Login", command=self.login, bootstyle=INFO)
        self.login_button.grid(row=2, column=1, padx=(0, 20), pady=(0, 10), sticky="ew")

        self.sign_in_button = Button(self.header, text="Sign in", command=self.sign_in, bootstyle=SUCCESS)
        self.sign_in_button.grid(row=3, column=1, padx=(0, 20), pady=(0, 10), sticky="ew")

    def sign_in(self):
        self.view.switch("signin")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        result = self.user_business.login(username, password)
        user = result[0]
        error_message = result[1]

        if error_message:
            messagebox.showerror(title="Error", message=error_message)
        else:
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            home_frame = self.view.switch("home")
            home_frame.set_current_user(user)
