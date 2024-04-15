from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox

class Discounts():
    
    def __init__(self,credentials,branch,database,root):
        
        
        discounts_label = ttk.Label(root,text="Discounts",font=("Arial", 28))

        create_discount_button = ttk.Button(root,text="Create Discount",width=50)
        read_discount_button = ttk.Button(root,text="Read Discounts",width=50)
        update_discount_button = ttk.Button(root,text="Update Discount",width=50)
        delete_discount_button = ttk.Button(root,text="Delete Discount",width=50)
        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,database,root),width=50) 

        discounts_label.pack()
        create_discount_button.pack()
        read_discount_button.pack()
        update_discount_button.pack()
        delete_discount_button.pack()
        back_button.pack()
        
        widgets = [discounts_label,
                   create_discount_button,
                   read_discount_button,
                   update_discount_button,
                   delete_discount_button,
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