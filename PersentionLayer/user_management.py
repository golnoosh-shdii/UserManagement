from tkinter import messagebox
from tkinter.ttk import Treeview

from ttkbootstrap import SUCCESS, DANGER, INFO, Frame, Label, Button, END

from BusinessLogicLayer.user_business import UserBusiness


class UserManagement(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.treeview_items = []

        self.user_business = UserBusiness()

        self.current_user = None

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="User Management Page")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.active_button = Button(self, text="Activate", command=self.active_button_clicked, bootstyle=SUCCESS)
        self.active_button.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="e")

        self.deactive_button = Button(self, text="Deactivate", command=self.deactive_button_clicked, bootstyle=DANGER)
        self.deactive_button.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="w")

        self.back_to_home = Button(self, text="Back to home page", command=self.back_to_home, bootstyle=INFO)
        self.back_to_home.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")

        self.columns = ("first_name", "last_name", "username", "status", "role")

        self.table = Treeview(self, columns=self.columns)

        self.table.heading(column="#0", text="NO")
        self.table.heading(column="first_name", text="First Name")
        self.table.heading(column="last_name", text="Last Name")
        self.table.heading(column="username", text="Username")
        self.table.heading(column="status", text="Status")
        self.table.heading(column="role", text="Role")

        self.table.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")

    def load_data(self, current_user):
        for item in self.treeview_items:
            self.table.delete(item)
        self.treeview_items.clear()

        self.current_user = current_user
        result = self.user_business.get_users(self.current_user)
        user = result[0]
        error_message = result[1]

        if error_message:
            messagebox.showerror(message=error_message, title="Error")
        else:
            row_number = 1
            for item in user:
                items = self.table.insert("", END, iid=item.id, text=str(row_number), values=(
                    item.firstname,
                    item.lastname,
                    item.username,
                    "Active" if item.active == 1 else "Deactivate",
                    item.role_id
                ))
                row_number += 1
                self.treeview_items.append(items)

            self.table.column("#0", width=180, anchor="w")
            for column in self.columns:
                self.table.column(column, width=200, anchor="center")

    def active_button_clicked(self):
        for user_id in self.table.selection():
            error_message = self.user_business.activate(self.current_user, user_id)

            if error_message:
                messagebox.showerror(title="Error", message=error_message)
            else:
                self.load_data(self.current_user)

    def deactive_button_clicked(self):
        for user_id in self.table.selection():
            error_message = self.user_business.deactive(self.current_user, user_id)

            if error_message:
                messagebox.showerror(title="Error", message=error_message)
            else:
                self.load_data(self.current_user)

    def back_to_home(self):
        self.view.switch("home")
