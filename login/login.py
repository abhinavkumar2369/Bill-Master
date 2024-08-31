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
        
        self.is_logged_in = False
        self.name = None
        self.user_id = None
        self.turn = 0
        self.is_cancelled = True
        
        
        logo = PhotoImage(file=os.path.join(current_dir,'images/application_logo.png'))
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
        self.register_button = ttk.Button(self.frame, text="Sign Up", style='TButton', command=self.register, cursor="hand2")
        self.register_button.grid(row=0,column=1)

        # MongoDB connection
        uri = "mongodb+srv://dbLogin:6LE0L?9Ad=(|@usercredentials.dgn1y.mongodb.net/?retryWrites=true&w=majority&appName=UserCredentials"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["user_credentials"]
        self.users = self.db["auth"]

    def login(self):
        username = self.username.get()
        password = self.password.get()

        user = self.users.find_one({"username": username})
        
        if user:
            hashed_password = user['password']
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                messagebox.showinfo("Success", "Login successful!")
                self.is_logged_in = True
                self.user_id = user["_id"]
                self.name = user["name"]
                self.window.destroy()
        else:
            messagebox.showerror("Error", "Invalid Username or password")

    def register(self):
        self.turn = 1
        self.is_cancelled = False
        
        self.window.destroy()