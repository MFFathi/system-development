from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox

class STAFF():
       
      def __init__(self, widgets, credentials,branch,root):
            for x in widgets:
               x.pack_forget()
               
            firstName = credentials[0]
            role = credentials[3]
            
            #Label Creation:
            system_name= ttk.Label(text="Horizon Restaurant Management System " + branch, font=("Arial",18))
            welcome_message = ttk.Label(root,text="Welcome " + firstName)
            user_role = ttk.Label(root,text="User Role: " + role)
            
            #System Name Label:        
            system_name.pack()   
            
            #Displays Labels:
            user_role.pack()
            welcome_message.pack()
               
            #Button Creation:
            inventory_button = ttk.Button(root,text="Inventory", command=lambda : self.inventory(widgets,credentials,branch,root),width=50)
            
            kitchen_button = ttk.Button(root,text="Kitchen", command=lambda : self.kitchen(widgets,credentials,branch,root),width=50)
            
            order_button = ttk.Button(root,text="Order", command=lambda : self.order(widgets,credentials,branch,root),width=50)
            
            #Logout Button:
            logout_button = ttk.Button(root,text="Logout", command=lambda : self.logout(widgets,branch,root), width=50)
               
            #Displays Buttons Alphabetically:
            inventory_button.pack()
            kitchen_button.pack()
            order_button.pack()
            logout_button.pack()
            
            #Packs the widgets into a list to be passed onto the next class/function that may be called: 
            widgets = [inventory_button, 
                     kitchen_button, 
                     order_button,
                     logout_button,
                     system_name,
                     welcome_message,
                     user_role]
         
      #The Functions Below Call The Relevant Class Based On The Button That Was Clicked On As Well As Remove The Widgets On The Current Page:
      def inventory(self,widgets,credentials,branch,database,root):
            for x in widgets:
               x.pack_forget() 
            from Inventory.Inventory import Inventory
            Inventory(credentials,branch,database,root)
            
      def kitchen(self,widgets,credentials,branch,database,root):
            for x in widgets:
               x.pack_forget() 
            from Kitchen.Kitchen import Kitchen
            Kitchen(credentials,branch,database,root)
            
      def order(self,widgets,credentials,branch,database,root):
            for x in widgets:
               x.pack_forget() 
            from Order.Order import Order
            Order(credentials,branch,database,root)

      def logout(self,widgets,branch,root):
               from Login.Login import Login
               Login(widgets,branch,root)