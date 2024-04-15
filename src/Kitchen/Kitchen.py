from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox

class Kitchen():
    
    def __init__(self,credentials,branch,database,root):
        
        kitchen_label = ttk.Label(root,text="Kitchen",font=("Arial", 28))

        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,database,root),width=50) 

        kitchen_label.pack()
        back_button.pack()
        
        widgets = [kitchen_label, 
                   back_button]

    def back(self,widgets,credentials,branch,database,root):
        
        for x in widgets:
             x.pack_forget()
             
        if credentials[3] == "Admin":
            from ADMIN.AdminGUI import ADMIN
            ADMIN(credentials,branch,database,root) 
        elif credentials[3] == "Manager":
            from MANAGER.ManagerGUI import MANAGER
            MANAGER(credentials,branch,database,root)
        elif credentials[3] == "Director":
            from DIRECTOR.DirectorGUI import DIRECTOR
            DIRECTOR(credentials,branch,database,root) 
        elif credentials[3] == "Chef":
            from CHEF.ChefGUI import CHEF
            CHEF(credentials,branch,database,root)
        elif credentials[3] == "Staff":
            from STAFF.StaffGUI import STAFF
            STAFF(credentials,branch,database,root) 