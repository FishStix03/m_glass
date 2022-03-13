import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import db_connector
import prim_func
import session
import session_functions


class window:

    __vital_int = 0
    __image_file_path = "N/A"

    def __init__(self, root):
        style = ttk.Style()
        print(style.theme_names())
        #style.theme_use("clam")
        
        frame = Frame(root)
        frame.grid()
        self.welcome_widgets(frame)

        #some god awful alignment
        Grid.columnconfigure(root, 0, weight=5)

    def welcome_widgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        
        window.__vital_int = 0
        session.session_id = 0
        frame.welcome_label = ttk.Label(frame, text="Welcome")
        frame.login_page_button = ttk.Button(frame, text="Login", command=lambda frame=frame : self.make_login_page(frame))
        frame.signup_page_button = ttk.Button(frame, text="Sign Up", command=lambda frame=frame : self.make_signup_page(frame))

        frame.welcome_label.grid(row=0, sticky="nsew")
        frame.login_page_button.grid(row=1, sticky="nsew")
        frame.signup_page_button.grid(row=2, sticky="nsew")

    def make_login_page(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        #create label with error message if necessary
        if window.__vital_int==-1:
            frame.error_label = ttk.Label(frame, text="Incorrect Password")
        elif window.__vital_int==-2:
            frame.error_label = ttk.Label(frame, text="Incorrect Username")
        else:
            frame.error_label = ttk.Label(frame, text="   ")

        frame.login_label = ttk.Label(frame, text="Login")
        frame.username_entry = ttk.Entry(frame)
        frame.username_entry.insert(0, "Username")
        frame.password_entry = ttk.Entry(frame)
        frame.password_entry.insert(0, "Password")
        frame.login_button = ttk.Button(frame, text="Login", command=lambda frame=frame : self.win_login(frame))
        frame.welcome_page_button = ttk.Button(frame, text="Back", command=lambda frame=frame : self.welcome_widgets(frame))

        frame.login_label.grid(row=0)
        frame.username_entry.grid(row=1)
        frame.password_entry.grid(row=2)
        frame.error_label.grid(row=3)
        frame.login_button.grid(row=4)
        frame.welcome_page_button.grid(row=5)

    def win_login(self, frame):
        username = str(frame.username_entry.get())
        pw = str(frame.password_entry.get())
        db = db_connector.get_db()
        window.__vital_int = prim_func.login(username, pw, "not_key.txt", db)
        print(window.__vital_int)
        if window.__vital_int > 0:
            session.session_id = window.__vital_int
            self.begin_session(frame)
        else:
            self.make_login_page(frame)

    def make_signup_page(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        
        #create label with error message if necessary
        if window.__vital_int==-1:
            frame.error_label = ttk.Label(frame, text="Passwords don't match")
        elif window.__vital_int==-2:
            frame.error_label = ttk.Label(frame, text="Password must be between 6 and 30 characters long")
        elif window.__vital_int==-3:
            frame.error_label = ttk.Label(frame, text="Invalid character(s) in password")
        elif window.__vital_int==-4:
            frame.error_label = ttk.Label(frame, text="Username must be between 6 and 30 characters long")
        elif window.__vital_int==-5:
            frame.error_label = ttk.Label(frame, text="Invalid character(s) in username")
        elif window.__vital_int==-6:
            frame.error_label = ttk.Label(frame, text="Username already exists")
        else:
            frame.error_label = ttk.Label(frame, text="   ")

        frame.signup_label = ttk.Label(frame, text="Signup")
        frame.username_entry = ttk.Entry(frame)
        frame.username_entry.insert(0, "Username")
        frame.password_entry = ttk.Entry(frame)
        frame.password_entry.insert(0, "Password")
        frame.re_password_entry = ttk.Entry(frame)
        frame.re_password_entry.insert(0, "Re-Enter Password")
        frame.signup_button = ttk.Button(frame, text="Sign Up", command=lambda frame=frame : self.win_signup(frame))
        frame.welcome_page_button = ttk.Button(frame, text="Back", command=lambda frame=frame : self.welcome_widgets(frame))

        frame.signup_label.grid(row=0)
        frame.username_entry.grid(row=1)
        frame.password_entry.grid(row=2)
        frame.re_password_entry.grid(row=3)
        frame.error_label.grid(row=4)
        frame.signup_button.grid(row=5)
        frame.welcome_page_button.grid(row=6)

    def win_signup(self, frame):
        username = str(frame.username_entry.get())
        pw = str(frame.password_entry.get())
        re_pw = str(frame.re_password_entry.get())
        db = db_connector.get_db()
        window.__vital_int = prim_func.signup(username, pw, re_pw, "not_key.txt", db)
        print(window.__vital_int)
        if window.__vital_int > 0:
            session.session_id = window.__vital_int
            self.begin_session(frame)
        else:
            self.make_signup_page(frame)
    
    def begin_session(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        frame.session_label1 = ttk.Label(frame, text="Welcome to Memory Glass")
        frame.contacts_button = ttk.Button(frame, text="Go to contacts page", command=lambda frame=frame : self.contacts_page(frame))
        frame.run_button = ttk.Button(frame, text="Run Memory Glass", command=self.run_app)
        frame.logout_button = ttk.Button(frame, text="Logout", command=lambda frame=frame : self.welcome_widgets(frame))

        frame.session_label1.grid(row=0)
        frame.contacts_button.grid(row=1)
        frame.run_button.grid(row=2)
        frame.logout_button.grid(row=3)

    def contacts_page(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        
        frame.contact_page_label = ttk.Label(frame, text="Contacts")
        frame.create_contact_button = ttk.Button(frame, text="Create contact", command=lambda frame=frame : self.contact_create_page(frame))
        frame.back_button = ttk.Button(frame, text="Back", command=lambda frame=frame : self.begin_session(frame))
        
        frame.contact_page_label.grid(row=0)
        frame.create_contact_button.grid(row=1, column=0)
        frame.back_button.grid(row=1, column=1)

        contacts_list = session_functions.retrieve_all_contacts(session.session_id, db_connector.get_db())
        counter = 2
        for x in contacts_list:
            frame.contact = ttk.Label(frame, text=x)
            frame.delete_button = ttk.Button(frame, text="Delete", command=lambda index=counter-2, frame=frame : self.delete_contact(index, frame))
            frame.contact.grid(row=counter, column=0)
            frame.delete_button.grid(row=counter, column=1)
            counter+=1

    def delete_contact(self, index, frame):
        contacts_list = session_functions.retrieve_all_contacts(session.session_id, db_connector.get_db())
        contact_name = contacts_list[index]
        session_functions.delete_contact(contact_name, session.session_id, db_connector.get_db())
        self.contacts_page(frame)


    def contact_create_page(self, frame): #still needs error handling
        for widget in frame.winfo_children():
            widget.destroy()

        #check for errors
        if window.__vital_int == -2:
            frame.error_label = ttk.Label(frame, text="Name Must be between 2 and 30 characters")
            window.__vital_int = session.session_id
        elif window.__vital_int == -1:
            frame.error_label = ttk.Label(frame, text="Something went wrong!")
            window.__vital_int = session.session_id
        else:
            frame.error_label = ttk.Label(frame, text=" ")

        frame.contact_create_page_label = ttk.Label(frame, text="Create new contact")
        frame.contact_name_entry = ttk.Entry(frame)
        frame.upload_image = ttk.Button(frame, text="Upload image", command=self.image_file_upload)
        frame.create_button = ttk.Button(frame, text="Create Contact", command=lambda frame=frame : self.win_create_contact(frame))
        frame.create_back_button = ttk.Button(frame, text="Back", command=lambda frame=frame : self.contacts_page(frame))

        frame.contact_create_page_label.grid(row=0)
        frame.contact_name_entry.grid(row=1)
        frame.upload_image.grid(row=2)
        frame.create_button.grid(row=3)
        frame.create_back_button.grid(row=4)
        frame.error_label.grid(row=5)

    def win_create_contact(self, frame):
        name = str(frame.contact_name_entry.get())
        if len(name) < 2 or len(name) > 30:
            window.__vital_int = -2
            self.contact_create_page(frame)
        db = db_connector.get_db()
        window.__vital_int = session_functions.create_contact(name, window.__image_file_path, session.session_id, db)
        if window.__vital_int == 0:
            window.__vital_int = session.session_id
            self.contacts_page(frame)
        else:
            window.__vital_int = -1
            self.contact_create_page(frame)

    
    def image_file_upload(self):
        window.__image_file_path = filedialog.askopenfilename()
        print(window.__image_file_path)
    
    def run_app(self):
        contact_names = session_functions.retrieve_all_contacts(session.session_id, db_connector.get_db())
        face_encodings = session_functions.retrieve_face_encodings(session.session_id, db_connector.get_db())
        session_functions.facial_recog_app(face_encodings, contact_names)


root = Tk()
root.geometry("400x200")
root.title("Memory Glass")
window(root)
root.mainloop()
