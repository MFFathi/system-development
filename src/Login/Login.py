
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from Branch import Branch
from VerifyLogin.verifyLogin import verifyLogin

class Login():

        #Calls The Verify Login Class To Confirm The Credentials:
        def getLogin(self,username_entry, password_entry, widgets,branch,root):
            
                #verify = VerifyLogin()
                entered_username = username_entry.get()
                entered_password = password_entry.get()
                #verifyLogin.verify(entered_username, entered_password,widgets,branch)
                verifyLogin.verify(entered_username, entered_password,widgets,branch,root)
        
        def validated(correct,widgets,root): #If A User's Login Details Are Correct Then The Login Widgets Are Removed
            if correct == TRUE:    
                for x in widgets:
                     x.pack_forget()
                 
        def __init__(self, widgets, branch,root):
            
            for x in widgets:
                x.pack_forget() 

            #Displays The Name Of The System And The Branch That Was Chosen:
            system_name= ttk.Label(text="Horizon Restaurant Management System " + branch, font=("Arial",18))

            username_text = ttk.Label(text="Username:")
            password_text = ttk.Label(text="Password:")
    
            username_entry = ttk.Entry(root)
            password_entry = ttk.Entry(root,show="*")
           
            system_name.pack()
            username_text.pack()
            username_entry.pack()
    
            password_text.pack()
            password_entry.pack()
            login_button = ttk.Button(root, text="Login",command=lambda:self.getLogin(username_entry,password_entry,widgets,branch,root))
            back_button = ttk.Button(root,text="Back",command=lambda:self.backToBranches(widgets),width=40)
            
            login_button.pack()   
            back_button.pack(side=BOTTOM)
            
            #Packs the widgets into a list to be passed onto the next class/function that may be called:
            widgets = [system_name,username_text,password_text,username_entry,password_entry,login_button,back_button]
            
        #Returns To The Branch Selection Page:
        def backToBranches(self,widgets):
            for x in widgets:
                 x.pack_forget()
            Branch.Branch()
            