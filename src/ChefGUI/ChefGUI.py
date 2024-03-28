from tkinter import *
from tkinter import ttk
from tkcalendar import *

class CHEF():
    
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
          
        #Menu Button:
        menu_button = ttk.Button(root,text="Menu", command= lambda : self.menu(widgets,credentials,branch,root), width=50)
        
        #Kitchen Button:
        kitchen_button = ttk.Button(root,text="Kitchen", command=lambda : self.kitchen(widgets,credentials,branch, root), width=50)

        #Logout Button:
        logout_button = ttk.Button(root,text="Logout", command=lambda : self.logout(widgets,branch,root), width=50)
          
        #Displays Buttons Alphabetically:
        menu_button.pack()
        kitchen_button.pack()
        logout_button.pack()
        
        #Packs the widgets into a list to be passed onto the next class/function that may be called: 
        widgets = [menu_button,
                 logout_button,
                 system_name,
                 welcome_message,
                 kitchen_button,
                 user_role]
        
    #The Functions Below Call The Relevant Class Based On The Button That Was Clicked On As Well As Remove The Widgets On The Current Page:
    def menu(self,widgets,credentials,branch,database,root):
         for x in widgets:
            x.pack_forget() 
         Menu(credentials,branch,database,root)
         
    def kitchen(self,widgets,credentials,branch,root):
          for x in widgets:
                    x.pack_forget()
          from Kitchen.Kitchen import Kitchen 
          Kitchen(credentials,branch,root)
        
    def logout(self,widgets,branch,root):
            from Login.Login import Login
            Login(widgets,branch,root)       