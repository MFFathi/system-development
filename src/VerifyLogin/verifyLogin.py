from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from AdminGUI.AdminGUI import ADMIN
from DirectorGUI.DirectorGUI import DIRECTOR
from ManagerGUI.ManagerGUI import MANAGER
from ChefGUI.ChefGUI import CHEF
from StaffGUI.StaffGUI import STAFF
from Databases.Databases import Databases

'''
The purpose of this file is to verify the login details entered by a user in an attempt to log into the system.
'''

class verifyLogin():
    
        def verify(entered_username,entered_password,widgets,branch,root):    

            valid = FALSE 
                        
            #Selects The Relevant Database Based On The Chosen Branch:
            if (branch == "Birmingham"):
                database = Databases.birmingham_db.cursor()
                 
            elif(branch == "Bristol"):
                database = Databases.bristol_db.cursor()
                 
            elif(branch == "Cardiff"):
                database = Databases.cardiff_db.cursor()
            
            elif(branch == "Glasgow"):
                database = Databases.glasgow_db.cursor() 

            elif(branch == "London"):
                database = Databases.london_db.cursor()
                 
            elif(branch == "Manchester"):
                database = Databases.manchester_db.cursor()
                 
            elif(branch == "Nottingham"):
                database = Databases.nottingham_db.cursor()
            

            #Aquires The First Name, Username, Password And Role Of Each User Of The System:
            database.execute("SELECT first_name, username, password, role FROM users")
            accounts = database.fetchall()
        
            #accountsList ordered: (firstname[0], username[1], password[2], role[3]) For Each User From The User Table Of The Horizon Restaurant Management System
            accountsList = []
                
            for x in accounts:
                accountsList.append(x)
                
            for x in accountsList:
                if (entered_username == x[1]):#Looks To See If There Is An Account With The Respective Username
                    if(entered_password == x[2]):#If The Username Of An Account Is Correct, It Looks To See If The Password Is Correct
                             userCredentials = (x) #Appends The First Name, Username, Password And Role Respectively Into A Tuple If Login Credentials Are Correct
                             valid = TRUE #Sets The Boolean Used To TRUE If The Account Details Are Correct.
                             #If The User Is An Admin Then The Admin Class Is Called

                             if(userCredentials[3] == 'Admin'):
                                ADMIN(widgets,userCredentials,branch,root) 
                                
                             #If The User Is A Manager Then The Manager Class Is Called
                             elif(userCredentials[3] == 'Manager'):
                                    MANAGER(widgets,userCredentials,branch,root)
                             #If The User Is A Director:
                             elif(userCredentials[3] == 'Director'):
                                    DIRECTOR(widgets,userCredentials,branch,root)
                             #If The User Is A Chef:
                             elif(userCredentials[3] == 'Chef'):
                                    CHEF(widgets,userCredentials,branch,root)
                                    
                            #If The User Is A Staff:
                             elif(userCredentials[3] == 'Staff'):
                                    STAFF(widgets,userCredentials,branch,root)
                                    
            return valid
            

  
 