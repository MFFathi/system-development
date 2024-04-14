from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox
import Inventory

class FoodInventory():
    
    def __init__(self,widgets,credentials,branch,database,root):
        for x in widgets:
             x.pack_forget()
        
        food_inventory_label = ttk.Label(root,text="Food Inventory",font=("Arial",28))  
        create_food_inventory_button = ttk.Button(root,text="Create Food Inventory",width=50)
        read_food_inventory_button = ttk.Button(root,text="Read Food Inventory",width=50)
        update_food_inventory_button = ttk.Button(root,text="Update Food Inventory",width=50)
        delete_food_inventory_button = ttk.Button(root,text="Delete Food Inventory",width=50)
        back_button = ttk.Button(root,text="Back",command=lambda:self.backToInventory(widgets,credentials,branch,database,root),width=50)
        
        food_inventory_label.pack()
        create_food_inventory_button.pack()
        read_food_inventory_button.pack()
        update_food_inventory_button.pack()
        delete_food_inventory_button.pack()
        back_button.pack()

        widgets = [food_inventory_label,
                   create_food_inventory_button,
                   read_food_inventory_button,
                   update_food_inventory_button,
                   delete_food_inventory_button,back_button]
        
    def backToInventory(self,widgets,credentials,branch,database,root):
        
        for x in widgets:
             x.pack_forget()
             
        Inventory(credentials,branch,database,root)