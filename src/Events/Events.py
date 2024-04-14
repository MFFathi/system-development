from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox

class Events():
    
    def __init__(self,credentials,branch,database,root):
        
        events_label = ttk.Label(root,text="Events",font=("Arial", 28))

        create_event_button = ttk.Button(root,text="Create Event",width=50)
        read_events_button = ttk.Button(root,text="Read Events",width=50)
        update_event_button = ttk.Button(root,text="Update Event",width=50)
        delete_event_button = ttk.Button(root,text="Delete Event",width=50)
        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,database,root),width=50) 

        events_label.pack()
        create_event_button.pack()
        read_events_button.pack()
        update_event_button.pack()
        delete_event_button.pack()
        back_button.pack()
        
        widgets = [events_label,
                   create_event_button,
                   read_events_button,
                   update_event_button,
                   delete_event_button,
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