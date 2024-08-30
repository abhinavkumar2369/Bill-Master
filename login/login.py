from tkinter import *
from tkinter import ttk , messagebox
import os
# import pickle
from PIL import Image, ImageTk
from pymongo import MongoClient
import bcrypt

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# # Added for testing
# current_dir = os.getcwd()
# file_path = os.path.join(current_dir, 'data/credential.dat')
# file = open(file_path,"wb")
# file.write(pickle.dumps({"username":"admin","password":"admin"}))
# file.close()

current_window_name = "login"

class Login:
    def __init__(self):
        
        # Current Directory
        current_dir = os.getcwd()
        
        # Creating an instance of Tk class
        self.window = Tk()
        
        # Window configuration
        self.window.title("Sign In - Bill Master")
        self.window.geometry("600x500")
        self.window.configure(background="#ffffff")
        self.window.resizable(False,False)
        
        # self.window.resizable(False, False)
        self.window.configure(bg="#ffffff")
        
        
        logo = PhotoImage(file=os.path.join(current_dir,'images/application_logo.png'))
        self.window.iconphoto(False, logo)

        # Set the logo as the application icon
        self.window.iconphoto(False, logo)
        
        # --------- Login Label --------- #
        self.label = Label(self.window, text="Sign In", font=("Arial", 36,"bold"),fg="red",bg="#e0ffe6",pady=15)
        self.label.pack(fill=BOTH)
        
        
        # ------------ Frame ------------ #
        self.frame = Frame(self.window, bg="#ffffff")
        self.frame.pack(pady=(60,20))
        
        
        # -------------------------------------
        
        
        # User Image
        image_user_path = os.path.join(current_dir,'images/user_icon.png')
        image_user = Image.open(image_user_path)
        image_user = image_user.resize((40, 40))
        self.image_user = ImageTk.PhotoImage(image_user)
        
        
        # Username Label
        self.username_label = Label(self.frame, text="  Username", font=("Arial", 14),background="#ffffff",image=self.image_user,compound=LEFT)
        self.username_label.grid(row=0,column=0,padx=(0,80),pady=(0,40))
        
        
        # Username Entry
        self.username = Entry(self.frame, font=("Arial", 14),background="#f3f3f3",relief="groove")
        self.username.grid(row=0,column=2,pady=(0,40))
        
        
        # -----------------------------------
        
        
        # Password Image
        password_image_path = os.path.join(current_dir,'images/password_icon.png')
        password_image = Image.open(password_image_path)
        password_image = password_image.resize((40, 40))
        self.password_image = ImageTk.PhotoImage(password_image)
        
        
        # Password Label
        self.password_label = Label(self.frame,text="  Password", font=("Arial",14),background="#ffffff",image=self.password_image,compound=LEFT)
        self.password_label.grid(row=1,column=0,padx=(0,80),pady=(0,25))
        
        
        # Password Entry
        self.password = Entry(self.frame,font=("Arial", 14),background="#f3f3f3",relief="groove",show="*")
        self.password.grid(row=1,column=2,pady=(0,25))


        # -----------------------------------


        # Login Button
        style = ttk.Style()
        style.configure('TButton', font=("Arial", 14, "bold"),relief="rigid" )
        
        self.action_button = Button(self.window, text=" Login ", command=self.login, cursor="hand2",relief="ridge",font=("Arial", 14, "bold"),bg="#3d43f5",fg="white")
        self.action_button.pack(pady=(0,30))
        
        # Register Frame
        self.frame = Frame(self.window, bg="#ffffff")
        self.frame.pack()
        
        # Register Label
        self.register_label = Label(self.frame, text="Don't have an account?", font=("Arial", 12),background="#ffffff",padx=10,pady=30)
        self.register_label.grid(row=0,column=0)
        
        # Register Button
        self.change_button = ttk.Button(self.frame, text="Sign Up", style='TButton', command=self.change_window, cursor="hand2")
        self.change_button.grid(row=0,column=1)

        # MongoDB connection
        uri = "mongodb+srv://dbLogin:6LE0L?9Ad=(|@usercredentials.dgn1y.mongodb.net/?retryWrites=true&w=majority&appName=UserCredentials"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["bill_master"]
        self.users = self.db["users"]

    def login(self):
        username = self.username.get()
        password = self.password.get()

        user = self.users.find_one({"username": username, "password": password})
        if user:
            # print(user)
            user_id = user["_id"]
            messagebox.showinfo("Success", "Login successful!")
            
        else:
            messagebox.showerror("Error", "Invalid Username or password")

    def register(self):
        username = self.username.get()
        password = self.password.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required")
            return

        existing_user = self.users.find_one({"username": username})
        if existing_user:
            messagebox.showerror("Error", "Username already exists")
            return

        new_user = {
            "username": username,
            "password": password
        }
        self.users.insert_one(new_user)
        user = self.users.find_one(new_user)
        messagebox.showinfo("Success", "Account created successfully!")
        user_id = user["_id"]
        # return user_id

    
    def change_window(self):
        global current_window_name
    
        if current_window_name == "login":
            current_window_name = "register"
            self.window.title("Sign Up - Bill Master")
            self.label.config(text="Create an Account")
            self.register_label.config(text="Already have an account?")
            self.change_button.config(text="Sign In", command=self.change_window)
            self.action_button.config(text="Register", command=self.register)
    
        else:
            current_window_name = "login"
            self.window.title("Login - Bill Master")
            self.label.config(text="LOGIN")
            self.register_label.config(text="Don't have an account?")
            self.change_button.config(text="Sign Up", command=self.change_window)
            self.action_button.config(text="Login", command=self.login)
        


# Ensure High DPI awareness on Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

a = Login().window.mainloop()
print(a)