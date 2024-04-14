from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox
import Inventory

today = datetime.today().date()
viewFoodCategories = None
foodCategoriesTable = None
foodItemsInCategory = None

root = Tk()

import mysql.connector 

#DATABASES TO CONNECT TO:
birmingham_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_birmingham"
    )


bristol_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_bristol"
    )

cardiff_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_cardiff"
    )

glasgow_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_glasgow"
    )

london_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_london"
    )

manchester_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_manchester"
    )

nottingham_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_nottingham"
    )

class CutleryInventory():
    
    def __init__(self,widgets,credentials,branch,database):
        for x in widgets:
             x.pack_forget()
        
        cutlery_inventory_label = ttk.Label(root,text="Cutlery Inventory",font=("Arial",28))  
        create_cutlery_inventory_button = ttk.Button(root,text="Create Cutlery Inventory",width=50)
        read_cutlery_inventory_button = ttk.Button(root,text="Read Cutlery Inventory",width=50)
        update_cutlery_inventory_button = ttk.Button(root,text="Update Cutlery Inventory",width=50)
        delete_cutlery_inventory_button = ttk.Button(root,text="Delete Cutlery Inventory",width=50)
        back_button = ttk.Button(root,text="Back",command=lambda:self.backToInventory(widgets,credentials,branch,database),width=50)
        
        cutlery_inventory_label.pack()
        create_cutlery_inventory_button.pack()
        read_cutlery_inventory_button.pack()
        update_cutlery_inventory_button.pack()
        delete_cutlery_inventory_button.pack()
        back_button.pack()

        widgets = [cutlery_inventory_label,
                   create_cutlery_inventory_button,
                   read_cutlery_inventory_button,
                   update_cutlery_inventory_button,
                   delete_cutlery_inventory_button,back_button]
        
    def backToInventory(self,widgets,credentials,branch,database):
        
        for x in widgets:
             x.pack_forget()
             
        Inventory(credentials,branch,database)