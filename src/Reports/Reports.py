from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox

class Reports():
    
    def __init__(self,credentials,branch,database,root):

        report_label = ttk.Label(root,text="Reports",font=("Arial", 28))        

        create_report_button = ttk.Button(root,text="Create Report",width=50)
        read_report_button = ttk.Button(root,text="Read Reports",width=50)
        update_report_button = ttk.Button(root,text="Update Report",width=50)
        delete_report_button = ttk.Button(root,text="Delete Report",width=50)
        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,database),width=50) 
        
        report_label.pack()
        create_report_button.pack()
        read_report_button.pack()
        update_report_button.pack()
        delete_report_button.pack()
        back_button.pack()
        
        widgets = [report_label,
                   create_report_button,
                   read_report_button,
                   update_report_button,
                   delete_report_button,
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