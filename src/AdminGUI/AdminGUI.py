from tkinter import *
from tkinter import ttk
from tkcalendar import *

class ADMIN():
    
     def __init__(self, widgets, credentials,branch,root):

          for x in widgets:
               x.pack_forget()

          firstName = credentials[0]
          role = credentials[3]

          #Label Creation:
          system_name= ttk.Label(text="Horizon Restaurant Management System " + branch, font=("Arial",18))
          welcome_message = ttk.Label(root,text="Welcome " + firstName)
          user_role = ttk.Label(root,text="User Role: " + role)

          #BUTTON CREATION:
          #Account Management Button:
          account_management_button = ttk.Button(root,text="Account Management", command=lambda : self.accountManagement(widgets,credentials, branch, root), width=50)
          #Menu Button:
          menu_button = ttk.Button(root,text="Menu", command=lambda : self.menu(widgets,credentials,branch, root), width=50)
          #Report Button:
          reports_button = ttk.Button(root,text="Reports", command=lambda : self.reports(widgets,credentials,branch, root), width=50)
          #Kitchen Button:
          kitchen_button = ttk.Button(root,text="Kitchen", command=lambda : self.kitchen(widgets,credentials,branch, root), width=50)
          #Discounts Button:
          discounts_button = ttk.Button(root,text="Discounts", command=lambda : self.discounts(widgets, credentials,branch, root), width=50)
          #Events Button:
          events_button = ttk.Button(root,text="Events", command=lambda : self.events(widgets,credentials,branch, root), width=50)
          #Inventory Button:
          inventory_button = ttk.Button(root,text="Inventory", command=lambda : self.inventory(widgets,credentials,branch, root), width=50)
          #Reservations Button:
          reservation_button = ttk.Button(root,text="Reservations", command=lambda : self.reservations(widgets,credentials,branch, root), width=50)
          #Order Button:
          order_button = ttk.Button(root,text="Order", command=lambda : self.order(widgets,credentials,branch, root), width=50)
          #Logout Button:
          logout_button = ttk.Button(root,text="Logout", command=lambda : self.logout(widgets,branch,root), width=50)

          #System Name Label:        
          system_name.pack()
          #Dispays And Orders Labels:
          user_role.pack()
          welcome_message.pack()

          #Displays Buttons Alphabetically:
          account_management_button.pack()
          discounts_button.pack()
          events_button.pack()
          inventory_button.pack()
          kitchen_button.pack()
          menu_button.pack()
          order_button.pack()
          reports_button.pack()
          reservation_button.pack()
          logout_button.pack()
          
          #Packs the widgets into a list to be passed onto the next class/function that may be called: 
          widgets = [system_name,
                    account_management_button, 
                    discounts_button,
                    events_button,
                    inventory_button,
                    kitchen_button,
                    menu_button,
                    order_button,
                    reports_button,
                    reservation_button,
                    logout_button,
                    welcome_message,
                    user_role]  
          
     #The Functions Below Call The Relevant Class Based On The Button That Was Clicked On As Well As Remove The Widgets On The Current Page:
     def accountManagement(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget() 
          #from UserManagement.UserManagement import UserManagement
          #UserManagement(credentials,branch,root) 
          from UserManagement.UserGUI import UserGUI
          UserGUI(credentials,branch,root)
          
     def reservations(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget() 
          from Reservation.Reservation import Reservation
          Reservation(widgets,credentials,branch,root)
          
     def menu(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget() 
          from Menu.Menu import Menu
          Menu(widgets,credentials,branch,root)
          
     def reports(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget() 
          from Reports.Reports import Reports
          Reports(credentials,branch,root)
          
     def kitchen(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget()
          from Kitchen.Kitchen import Kitchen 
          Kitchen(credentials,branch,root)
          
     def discounts(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget()
          from Discounts.Discounts import Discounts 
          Discounts(credentials,branch,root)
          
     def events(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget() 
          from Events.Events import Events
          Events(widgets,credentials,branch,root)
          
     def inventory(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget() 
          from Inventory.Inventory import Inventory
          Inventory(widgets,credentials,branch,root)
          
     def order(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget()
          from Order.OrderGUI import OrderGUI
          OrderGUI(credentials,branch,root)

     def logout(self,widgets,branch,root):
               from Login.Login import Login
               Login(widgets,branch,root)