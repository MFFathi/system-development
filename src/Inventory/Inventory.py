from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox
from FoodInventory import FoodInventory
from DrinkInventory import DrinkInventory
from CutleryInventory import CutleryInventory

class Inventory():
    
    def __init__(self,credentials,branch,database,root):
        
        inventory_label = ttk.Label(root,text="Inventory",font=("Arial", 28))

        food_inventory_button = ttk.Button(root,text="Food Inventory",command=lambda:FoodInventory(widgets,credentials,branch,database,root),width=50)
        drink_inventory_button = ttk.Button(root,text="Drink Inventory",command=lambda:DrinkInventory(widgets,credentials,branch,database,root),width=50)
        cutlery_inventory_button = ttk.Button(root,text="Cutlery Inventory",command=lambda:CutleryInventory(widgets,credentials,branch,database,root),width=50)
        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,database,root),width=50) 
        
        inventory_label.pack()
        food_inventory_button.pack()
        drink_inventory_button.pack()
        cutlery_inventory_button.pack()
        back_button.pack()
        
        widgets = [inventory_label,
                   food_inventory_button,
                   drink_inventory_button,
                   cutlery_inventory_button,
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