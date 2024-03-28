from tkinter import *
from tkinter import ttk
from tkcalendar import *

class DIRECTOR():

    def __init__(self, widgets,credentials,branch,root):
        
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
        
        #Displays Labels Alphabetically:
        user_role.pack()
        welcome_message.pack()
          
        #Reports Button:
        reports_button = ttk.Button(root,text="Reports", command=lambda : self.reports(widgets,credentials,branch,root), width=50)
        
        #Logout Button:
        logout_button = ttk.Button(root,text="Logout", command=lambda : self.logout(widgets,branch,root), width=50)
          
        #Displays Buttons Alphabetically:
        reports_button.pack()
        logout_button.pack()
        
        #Packs the widgets into a list to be passed onto the next class/function that may be called:
        widgets = [reports_button,
                 logout_button,
                 system_name,
                 welcome_message,
                 user_role]
        
    #The Functions Below Call The Relevant Class Based On The Button That Was Clicked On As Well As Remove The Widgets On The Current Page: 
    def reports(self,widgets,credentials,branch,database,root):
         for x in widgets:
            x.pack_forget() 
         from Reports.Reports import Reports
         Reports(credentials,branch,database,root)
        
    def logout(self,widgets,branch,root):
            from Login.Login import Login
            Login(widgets,branch,root)  