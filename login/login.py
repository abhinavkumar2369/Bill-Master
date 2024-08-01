from tkinter import *
from tkinter import ttk , messagebox
import os
import pickle
from PIL import Image, ImageTk


# Added for testing
current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'data/credential.dat')
file = open(file_path,"wb")
file.write(pickle.dumps({"username":"admin","password":"admin"}))
file.close()



class Login:
    def __init__(self):
        
        # Current Directory
        current_dir = os.getcwd()
        
        # Creating an instance of Tk class
        self.window = Tk()
        
        # Window configuration
        self.window.title("Login - Bill Master")
        self.window.geometry("600x450")
        self.window.configure(background="#ffffff")
        
        # self.window.resizable(False, False)
        self.window.configure(bg="#ffffff")
        
        
        logo = PhotoImage(file=os.path.join(current_dir,'images/application_logo.png'))
        self.window.iconphoto(False, logo)

        # Set the logo as the application icon
        self.window.iconphoto(False, logo)
        
        # --------- Login Label --------- #
        self.label = Label(self.window, text="LOGIN", font=("Arial", 36,"bold"),fg="red",bg="#e0ffe6",pady=15)
        self.label.pack(fill=BOTH)
        
        
        # ------------ Frame ------------ #
        self.frame = Frame(self.window, bg="#ffffff")
        self.frame.pack(pady=(70,30))
        
        
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
        self.password_label.grid(row=1,column=0,padx=(0,80),pady=(0,40))
        
        
        # Password Entry
        self.password = Entry(self.frame,font=("Arial", 14),background="#f3f3f3",relief="groove",show="*")
        self.password.grid(row=1,column=2,pady=(0,40))


        # -----------------------------------


        # Login Button
        style = ttk.Style()
        style.configure('TButton', font=("Arial", 16, "bold"),relief="rigid")
        
        self.login_button = ttk.Button(self.window, text=" Login ", style='TButton', command=self.login, cursor="hand2")
        self.login_button.pack(pady=(0,30))

        
        
    def login(self):
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'data/credential.dat')
        file = open(file_path,"rb")
        try:
            file_data = pickle.load(file)
            if self.username.get() == file_data["username"] and self.password.get() == file_data["password"]:
                messagebox.showinfo("Login Success", "You have successfully logged in!")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password! \n Please try again.")
            print(file_data)
        except:
            file.close()
            
        
        


# Ensure High DPI awareness on Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


login = Login()
login.window.mainloop()