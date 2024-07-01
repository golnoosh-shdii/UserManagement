from tkinter import Frame, LabelFrame, Label, Entry, Button, END, messagebox

from BusinessLogicLayer.user_business import UserBusiness


class EditInformationFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.current_user = None

        self.view = view

        self.user_business = UserBusiness()

        self.grid_columnconfigure(0, weight=1)

        self.header = LabelFrame(self, text="Edit Your Information")
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.header.grid_columnconfigure(1, weight=1)

        self.new_firstname_label = Label(self.header, text="New First Name :")
        self.new_firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.new_firstname_entry = Entry(self.header)
        self.new_firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.new_lastname_label = Label(self.header, text="New Last Name :")
        self.new_lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_lastname_entry = Entry(self.header)
        self.new_lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.new_username_label = Label(self.header, text="New Username  :")
        self.new_username_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_username_entry = Entry(self.header)
        self.new_username_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.save_button = Button(self.header, text="Save", command=self.save_button_clicked)
        self.save_button.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.back_to_home_page_button = Button(self, text="Back To Home Page",command= self.back_to_home_page_button_clicked)
        self.back_to_home_page_button.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="ew")

    def set_current_user_for_edit_information_frame(self,current_user):
        self.current_user = current_user
    def save_button_clicked(self):
        new_firstname = self.new_firstname_entry.get()
        new_lastname = self.new_lastname_entry.get()
        new_username = self.new_username_entry.get()

        result = self.user_business.edit_info(self.current_user, new_firstname, new_lastname, new_username)
        save_message = result[0]
        error_message = result[1]

        if error_message:
            messagebox.showerror(title="Error", message=error_message)
        else:
            messagebox.showinfo(title="Info", message=save_message)

    def back_to_home_page_button_clicked(self):
        self.new_firstname_entry.delete(0, END)
        self.new_lastname_entry.delete(0, END)
        self.new_username_entry.delete(0, END)

        self.view.switch("home")
