from tkinter import *
from tkinter import ttk

class Login:
    def __init__(self):
        
        # Creating an instance of Tk class
        self.window = Tk()
        
        # Window configuration
        self.window.title("Login")
        self.window.geometry("600x400")
        self.window.configure(back="#ffffff")
        self.window.resizable(False, False)
        self.window.configure(bg="#ffffff")
        
        
        # Login Label
        self.label = Label(self.window, text="LOGIN", font=("Arial", 36,"bold"),fg="#333333",bg="#ffffff")
        self.label.pack(pady=(20,25),fill=BOTH)
        
        
        self.frame = Frame(self.window, bg="#ffffff")
        self.frame.pack(pady=(20,40))
        
        
        # Username Label
        self.username_label = Label(self.frame, text="Username", font=("Arial", 14))
        self.username_label.grid(row=0,column=0,padx=(0,80),pady=(0,40))
        
        
        # Username Entry
        self.username = Entry(self.frame, font=("Arial", 14),borderwidth=2)
        self.username.grid(row=0,column=1,pady=(0,40))
        
        
        # Password Label
        self.password_label = Label(self.frame,text="Password", font=("Arial",14))
        self.password_label.grid(row=1,column=0,padx=(0,80),pady=(0,40))
        
        
        # Password Entry
        self.password = Entry(self.frame,font=("Arial", 14))
        self.password.grid(row=1,column=1,pady=(0,40))


        # Login Button
        style = ttk.Style()
        style.configure('TButton', font=("Arial", 16, "bold"),relief="rigid")
        
        self.login_button = ttk.Button(self.window, text=" Login ", style='TButton', command=self.login)
        self.login_button.pack(pady=(0,30))

        
    def login(self):
        print("Username:", self.username.get())
        print("Password:", self.password.get())


# Ensure High DPI awareness on Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


login = Login()
login.window.mainloop()