from tkinter import *
from tkinter import ttk
from tkcalendar import *

class MANAGER():    

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
            
        #Dispays And Orders Labels:
        user_role.pack()
        welcome_message.pack()
     
        #Menu Button:
        menu_button = ttk.Button(root,text="Menu", command=lambda : self.menu(widgets,credentials,branch,root), width=50)
        
        #Report Button:
        reports_button = ttk.Button(root,text="Reports", command=lambda : self.reports(widgets,credentials,branch,root),width=50)

        #Discounts Button:
        discounts_button = ttk.Button(root,text="Discounts", command=lambda : self.discounts(widgets,credentials,branch,root),width=50)
        
        #Events Button:
        events_button = ttk.Button(root,text="Events", command=lambda : self.events(widgets,credentials,branch,root), width=50)
        
        #Reservations Button:
        reservation_button = ttk.Button(root,text="Reservations", command=lambda : self.reservations(widgets,credentials,branch,root), width=50)

        #Logout Button:
        logout_button = ttk.Button(root,text="Logout", command=lambda : self.logout(widgets,branch,root), width=50)

                                                                          
        #Displays Buttons Alphabetically:
        discounts_button.pack()
        events_button.pack()
        menu_button.pack()
        reports_button.pack()
        reservation_button.pack()
        logout_button.pack()
        
        #Packs the widgets into a list to be passed onto the next class/function that may be called:
        widgets = [discounts_button,
                 events_button,
                 menu_button,
                 reports_button,
                 reservation_button,
                 logout_button,
                 system_name,
                 welcome_message,
                 user_role]

    #The Functions Below Call The Relevant Class Based On The Button That Was Clicked On As Well As Remove The Widgets On The Current Page:
    def menu(self,widgets,credentials,branch,database,root):
         for x in widgets:
                x.pack_forget() 
         Menu(credentials,branch,database,root)
         
    def reports(self,widgets,credentials,branch,database,root):
         for x in widgets:
                x.pack_forget() 
         from Reports.Reports import Reports
         Reports(credentials,branch,database,root)
         
    def discounts(self,widgets,credentials,branch,database,root):
         for x in widgets:
                x.pack_forget() 
         from Discounts.Discounts import Discounts
         Discounts(credentials,branch,database,root)
         
    def events(self,widgets,credentials,branch,database,root):
         for x in widgets:
                x.pack_forget() 
         from Events.Events import Events
         Events(credentials,branch,database,root)
         
    def reservations(self,widgets,credentials,branch,database,root):
         for x in widgets:
                x.pack_forget() 
         from Reservation.Reservation import Reservation
         Reservation(credentials,branch,database,root)

    def logout(self,widgets,branch,root):
            from LoginGUI.LoginGUI import LoginGUI
            LoginGUI(widgets,branch,root)     