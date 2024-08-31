from tkinter import *
from tkinter import ttk , messagebox
import os
from PIL import Image, ImageTk
from pymongo import MongoClient
import bcrypt

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Ensure High DPI awareness on Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class Register:
    def __init__(self):
        
        # Current Directory
        current_dir = os.getcwd()
        
        # Creating an instance of Tk class
        self.window = Tk()
        
        # Window configuration
        self.window.title("Register - Bill Master")
        self.window.geometry("700x600")
        self.window.configure(background="#ffffff")
        self.window.resizable(False,False)
        
        # self.window.resizable(False, False)
        self.window.configure(bg="#ffffff")
        
        # Load the image using PIL and convert it to a Tkinter-compatible PhotoImage
        logo_path = os.path.join(current_dir, 'images/application_logo.png')
        image = Image.open(logo_path)
        logo = ImageTk.PhotoImage(image)
        
        # Set the logo as the application icon
        self.window.iconphoto(False, logo)
        
        # --------- Login Label --------- #
        self.label = Label(self.window, text="Sign Up", font=("Arial", 36,"bold"),fg="red",bg="#e0ffe6",pady=15)
        self.label.pack(fill=BOTH)
        
        # -------------------------------------
        
        self.is_logged_in = False
        self.user_id = None
        self.name = None
        self.turn = 1
        self.is_cancelled = True
        
        
        # ------------ Frame ------------ #
        
        self.frame = Frame(self.window, bg="#ffffff")
        self.frame.pack(pady=(45,20))
        
        
        
        # ----------- Name --------------
        
        name_image_path = os.path.join(current_dir,'images/name.png')
        name_image = Image.open(name_image_path)
        name_image = name_image.resize((40, 40))
        self.name_image = ImageTk.PhotoImage(name_image)
        
        self.name = Label(self.frame, text="  Name", font=("Arial", 14),background="#ffffff",image=self.name_image,compound=LEFT)
        self.name.grid(row=0,column=0,padx=(0,80),pady=(15,25))
        
        self.name_entry = Entry(self.frame, font=("Arial", 14),background="#f3f3f3",relief="groove")
        self.name_entry.grid(row=0,column=1,pady=(20,25))
        
        
        
        # ----------- UserName --------------
        
        # User Image
        image_user_path = os.path.join(current_dir,'images/user_icon.png')
        image_user = Image.open(image_user_path)
        image_user = image_user.resize((40, 40))
        self.image_user = ImageTk.PhotoImage(image_user)
        
        self.username_label = Label(self.frame, text="  Username", font=("Arial", 14),background="#ffffff",image=self.image_user,compound=LEFT)
        self.username_label.grid(row=1,column=0,padx=(0,80),pady=(0,25))
        
        self.username = Entry(self.frame, font=("Arial", 14),background="#f3f3f3",relief="groove")
        self.username.grid(row=1,column=1,pady=(0,25))
        
        
        # ------------ Password --------------
        
        password_image_path = os.path.join(current_dir,'images/password_icon.png')
        password_image = Image.open(password_image_path)
        password_image = password_image.resize((40, 40))
        self.password_image = ImageTk.PhotoImage(password_image)
        
        # Password Label
        self.password_label = Label(self.frame,text="  Password", font=("Arial",14),background="#ffffff",image=self.password_image,compound=LEFT)
        self.password_label.grid(row=2,column=0,padx=(0,80),pady=(0,25))
        
        # Password Entry
        self.password = Entry(self.frame,font=("Arial", 14),background="#f3f3f3",relief="groove",show="*")
        self.password.grid(row=2,column=1,pady=(0,25))


        # Password Label
        self.confirm_password_label = Label(self.frame,text=" Confirm Password", font=("Arial",14),background="#ffffff",)
        self.confirm_password_label.grid(row=3,column=0,padx=(0,80),pady=(0,25))
        
        # Password Entry
        self.confirm_password = Entry(self.frame,font=("Arial", 14),background="#f3f3f3",relief="groove",show="*")
        self.confirm_password.grid(row=3,column=1,pady=(0,25))

        # ------------ Regiter ----------

        style = ttk.Style()
        style.configure('TButton', font=("Arial", 14, "bold"),relief="rigid" )
        
        self.register_button = Button(self.window, text=" Register ", command=self.register, cursor="hand2",relief="ridge",font=("Arial", 14, "bold"),bg="#3d43f5",fg="white")
        self.register_button.pack(pady=(0,0))
        
        # Register Frame
        self.frame = Frame(self.window, bg="#ffffff")
        self.frame.pack(padx=(70,0),pady=(10,0))
        
        # Register Label
        self.login_label = Label(self.frame, text="Ops!!  You Already have an account ?   ", font=("Arial", 12),background="#ffffff",padx=10,pady=30)
        self.login_label.grid(row=0,column=0)
        
        # Register Button
        self.login_button = ttk.Button(self.frame, text="Login", style='TButton', command=self.login, cursor="hand2")
        self.login_button.grid(row=0,column=1)

    
    def login(self):
        self.turn = 0
        self.is_cancelled = False
        self.window.destroy()
            
    def register(self):
        # MongoDB connection
        uri = "mongodb+srv://dbLogin:6LE0L?9Ad=(|@usercredentials.dgn1y.mongodb.net/?retryWrites=true&w=majority&appName=UserCredentials"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["user_credentials"]
        self.users = self.db["auth"]
        
        username = self.username.get()
        password = self.password.get()
        
        name = self.name_entry.get()
        confirm_password = self.confirm_password.get()
    
        if not name or not username:
            if not password or not confirm_password:
                messagebox.showerror("Error", "All Enteries are required")
                return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long")
            return
        
        existing_user = self.users.find_one({"username": username})
        if existing_user:
            messagebox.showerror("Error", "Username already exists")
            return
        
        password = password.encode("utf-8")
        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        
        new_user = {
            "name": name,
            "username": username,
            "password": hashed_password,
        }
        self.users.insert_one(new_user)
        user = self.users.find_one(new_user)
        messagebox.showinfo("Success", "Account created successfully!")
        
        self.user_id = str(user["_id"])
        self.name = user["name"]
        self.is_logged_in = True
        
        self.window.destroy()
