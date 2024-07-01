from tkinter import messagebox

from ttkbootstrap import Frame, LabelFrame, Label, Entry, Button, END, SUCCESS

from BusinessLogicLayer.user_business import UserBusiness


class SigninFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.user_business = UserBusiness()

        self.grid_columnconfigure(0, weight=1)

        self.header = LabelFrame(self, text="Create Your Account")
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.header.grid_columnconfigure(1, weight=1)

        self.firstname_label = Label(self.header, text="First Name : ")
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.lastname_label = Label(self.header, text="Last Name : ")
        self.lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.lastname_entry = Entry(self.header)
        self.lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.username_label = Label(self.header, text="Username : ")
        self.username_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.username_entry = Entry(self.header)
        self.username_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.password_label = Label(self.header, text="Password : ")
        self.password_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.password_entry = Entry(self.header)
        self.password_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.save_button = Button(self.header, text="Save", command=self.save_button_clicked, bootstyle=SUCCESS)
        self.save_button.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.back_to_login_page_button = Button(self, text="Back To Login Page",
                                                command=self.back_to_login_page_button_clicked)
        self.back_to_login_page_button.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="ew")

    def back_to_login_page_button_clicked(self):
        self.firstname_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.view.switch("login")

    def save_button_clicked(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business.signin(firstname, lastname, username, password)
        save_message = result[0]
        error_message = result[1]

        if error_message:
            messagebox.showerror(title="Error", message=error_message)
        else:
            messagebox.showinfo(title="Info", message=save_message)
