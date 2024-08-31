from tkinter import *
import tkinter as tk


# --------- Login Class ----------
from login.login import Login
from register.register import Register
from application.app import BillGeneratorApp


# Ensure High DPI awareness on Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# Mongo URI
mongo_uri = "mongodb+srv://dbLogin:6LE0L?9Ad=(|@usercredentials.dgn1y.mongodb.net/?retryWrites=true&w=majority&appName=UserCredentials"
is_logged_in = False
is_cancelled = False
turn = 0


while True:
    if turn == 0:
        login = Login()
        login.window.mainloop()
        turn = login.turn
        is_logged_in = login.is_logged_in
        is_cancelled = login.is_cancelled
    
    if is_logged_in:
        db_name = "bill_data"
        user_id = str(login.user_id)
        name = login.name
        window = tk.Tk()
        main_app = BillGeneratorApp(window, mongo_uri, db_name, user_id , name)
        window.mainloop()
        break

    if is_cancelled:
        break
    
    if turn == 1:
        register = Register()
        register.window.mainloop()
        turn = register.turn
        is_cancelled = register.is_cancelled
        is_logged_in = register.is_logged_in
        
    if is_logged_in:
        db_name = "bill_data"
        user_id = str(register.user_id)
        name = register.name
        window = tk.Tk()
        main_app = BillGeneratorApp(window, mongo_uri, db_name, user_id , name)
        window.mainloop()
        break
    
    if is_cancelled:
        break
        
    

# user_id = str(login.user_id)
# username = login.username_value


# from tkinter import *
# import tkinter as tk

# # Importing necessary classes
# from login.login import Login
# from register.register import Register
# from application.app import BillGeneratorApp

# # Ensure High DPI awareness on Windows
# try:
#     from ctypes import windll
#     windll.shcore.SetProcessDpiAwareness(1)
# except:
#     pass

# class AppController:
#     def __init__(self):
#         self.is_logged_in = False
#         self.turn = 0
        
#         # Initialize the Login and Register windows
#         self.login = Login(self)
#         self.register = Register(self)
#         self.current_window = self.login.window  # Start with the login window

#     def start(self):
#         # Start the Tkinter main loop
#         self.current_window.mainloop()

#     def show_login(self):
#         self.turn = 0
#         self.current_window.withdraw()  # Hide current window
#         self.current_window = self.login.window  # Switch to login window
#         self.current_window.deiconify()  # Show the login window

#     def show_register(self):
#         self.turn = 1
#         self.current_window.withdraw()  # Hide current window
#         self.current_window = self.register.window  # Switch to register window
#         self.current_window.deiconify()  # Show the register window

#     def on_login_success(self):
#         self.is_logged_in = True
#         self.current_window.destroy()  # Close current window
#         # Transition to the main application
#         BillGeneratorApp()

# if __name__ == "__main__":
#     controller = AppController()
#     controller.start()
