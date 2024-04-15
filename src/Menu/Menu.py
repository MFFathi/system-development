from tkinter import *
from tkinter import ttk
from FoodCategories.FoodCategories import FoodCategories
from FoodItems.FoodItems import FoodItems

class Menu():
    
    def __init__(self,credentials, branch, database,root):
        
        menu_label = ttk.Label(root,text="Menu",font=("Arial", 28))

        food_categories_button = ttk.Button(root,text="Food Categories",command=lambda:FoodCategories(widgets,credentials,branch,database,root),width=50)
        food_items_button = ttk.Button(root,text="Food Items",command=lambda:FoodItems(widgets,credentials,branch,database,root),width=50)
        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,database,root),width=50) 
        

        menu_label.pack()
        food_categories_button.pack()
        food_items_button.pack()
        back_button.pack()
        
        widgets = [menu_label,
                   food_categories_button,
                   food_items_button,
                   back_button]

    def back(self,widgets,credentials,branch,database,root):
        
        for widget in widgets:
             widget.pack_forget()
             
        if credentials[3] == "Admin":
            from AdminGUI.AdminGUI import ADMIN
            ADMIN(credentials,branch,database,root) 
        elif credentials[3] == "Manager":
            from ManagerGUI.ManagerGUI import MANAGER
            MANAGER(credentials,branch,database,root)
        elif credentials[3] == "Director":
            from DirectorGUI.DirectorGUI import DIRECTOR
            DIRECTOR(credentials,branch,database,root) 
        elif credentials[3] == "Chef":
            from ChefGUI.ChefGUI import CHEF
            CHEF(credentials,branch,database,root)
        elif credentials[3] == "Staff":
            from StaffGUI.StaffGUI import STAFF
            STAFF(credentials,branch,database,root)