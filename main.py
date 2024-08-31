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
mongo_uri = "mongodb+srv://<username>:<password>@<cluster-address>/<dbname>?<options>"
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
