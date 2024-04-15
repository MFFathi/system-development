from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from UserManagement.UserSQL import UserSQL
from Login.LoginGUI import LoginGUI

"""
The purpose of this file is to display the relevant information to the user regarding user management i.e. buttons, labels and tables.
It will also take in input from the user and send it to hte UserSQL file to peform the necessary CRUD operations.
"""
class UserGUI():
    
    def __init__(self,credentials, branch, root):
        self.credentials = credentials
        self.root = root
        self.branch = branch
    
        user_management_label = ttk.Label(root,text="User Management",font=("Arial", 28))
        
        create_account_button = ttk.Button(root,text="Add User",command=lambda: self.addUser(widgets),width=50)
        read_account_button = ttk.Button(root,text="View Users",command=lambda: self.viewUsers(widgets,"view"),width=50)
        update_account_button = ttk.Button(root,text="Update User",command=lambda: self.viewUsers(widgets,"update"),width=50)
        delete_account_button = ttk.Button(root,text="Delete User",command=lambda: self.viewUsers(widgets,"delete"),width=50)
        back_button = ttk.Button(root,text="Back",command=lambda: self.back(widgets),width=50)
      
        user_management_label.pack()
        create_account_button.pack()
        read_account_button.pack()
        update_account_button.pack()
        delete_account_button.pack()
        back_button.pack()
        
        widgets = [user_management_label, read_account_button, create_account_button, update_account_button, delete_account_button, back_button]
        
#ADD USER
    def addUser(self,widgets):
        for x in widgets:
                 x.pack_forget()   
                 
        first_name_entry = ttk.Entry()
        last_name_entry = ttk.Entry()
        user_name_entry = ttk.Entry()
        password_entry = ttk.Entry(show="*")
        
        
        first_name_label = ttk.Label(text="First name")
        last_name_label = ttk.Label(text="Last name")
        user_name_label = ttk.Label(text="Username")
        password_label = ttk.Label(text="Password")
        
        submit_button = ttk.Button(self.root,text="Submit",command=lambda:submit(fields), width=20)        
        back_button = ttk.Button(self.root,text="Back",command=lambda:self.goBackToUserManagement(widgets),width=40)
        
        first_name_label.pack()
        first_name_entry.pack()
        
        last_name_label.pack()
        last_name_entry.pack()
        
        user_name_label.pack()
        user_name_entry.pack()
        
        password_label.pack()
        password_entry.pack()
        
        roleEntry = StringVar()
        roleEntry.set("Role")
                
        #List of user roles:
        roles = ["Admin", "Director", "Manager", "Chef", "Staff"]
        
        #Drop down menu for user roles
        drop = OptionMenu(self.root, roleEntry, *roles)
        drop.pack()
        
        submit_button.pack()
        back_button.pack(side=BOTTOM)
        
        fields = [first_name_entry, last_name_entry, user_name_entry, password_entry, roleEntry]
        
        widgets = [first_name_label, last_name_label, user_name_label, password_label, first_name_entry, last_name_entry, user_name_entry, password_entry, submit_button, drop, back_button]
        
        def submit(fields):
            
            valid = True
            userExists = False
                
            for x in fields:
                if x.get() == "":
                    messagebox.showerror("Error", "Please Complete All Fileds")
                    valid = False
                    break
                elif fields[4].get() == "Role":
                    messagebox.showerror("Error", "Please Select User Role")
                    valid = False
                    break
                elif len(fields[3].get()) < 4:
                    messagebox.showerror("Error", "Password Should Be At Least 4 Characters Long")
                    valid = False
                    break
                elif len(fields[2].get()) < 4:
                    messagebox.showerror("Error", "Username Should Be At Least 4 Characters Long")
                    valid = False
                    break
                
            usernames = UserSQL.username_in_use(self.branch)
            
            for username in usernames:
                if fields[2].get() == username[0]:
                    messagebox.showerror("Error", "Username Already In Use")
                    userExists = True
                    break
             
            if valid == True and userExists == False: 
                UserSQL.createUser(self.branch,fields)
                messagebox.showinfo("Account Created", "Account Successfully Created")
                for x in widgets:
                        x.pack_forget()
                UserGUI(self.credentials,self.branch,self.root)
            

#VIEW USER:
    def viewUsers(self, widgets,operation):
        
        for x in widgets:
            x.pack_forget()
        
        #Creates the table containing the list of users for the system:
        table = ttk.Treeview(self.root,columns=('first_name', 'last_name', 'username', 'password', 'role', 'id'), show='headings')
        table.heading('first_name', text = "First Name")
        table.heading('last_name', text = "Last Name")
        table.heading('username', text = "Username")
        table.heading('password', text = "Password")
        table.heading('role', text = "Role")
        table.heading('id', text="ID")
        
        table.pack(fill='both',expand=TRUE)   
        
        if operation == "view":
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToUserManagement(widgets),width=20)
            back_button.pack()
            widgets = [table, back_button]
            
        elif operation == "update":
            update_button = ttk.Button(self.root,text="Update",command=lambda:self.updateUser(widgets,table))
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToUserManagement(widgets))
    
            update_button.pack()
            back_button.pack()
            widgets = [table, update_button, back_button]
            
        elif operation == "delete":
            delete_button = ttk.Button(self.root,text="Delete",command=lambda:self.deleteUser(widgets,table))  
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToUserManagement(widgets)) 
            
            delete_button.pack()
            back_button.pack()
            widgets = [table, delete_button, back_button]  
                    
                    
        viewAccountList = UserSQL.getUsers(self.branch)
        
        #Searches through the individual information about each user from the users list i.e. first name[0], last name[1], username[2], password[3], role[4] and inserts it into the table:
        for x in viewAccountList:
            first_name=  x[0]
            last_name = x[1]
            username = x[2]
            password = x[3] 
            role = x[4]
            row_id = x[5]
            data = (first_name,last_name,username,password,role,row_id)
            table.insert(parent = '', index=0, values= data)


#UPDATE USER:
    def updateUser(self,widgets,table):
        
        userInfo = []
        for i in table.selection():
            a = tuple((table.item(i)['values']))
            if a[0] != " ":
                userInfo.append(table.item(i)['values'])
                
                #Asks for confirmation for the selected user to be updated:
                yes_no = messagebox.askyesno("Update This User?", "Are You Sure You Want To Make Changes To This User?")
                if (yes_no) == False: 
                    self.viewUsers(widgets,"update")
                else:
                    for x in widgets:
                        x.pack_forget()
                        
                    first_name_entry = ttk.Entry()
                    last_name_entry = ttk.Entry() 
                    username_entry = ttk.Entry()
                    password_entry = ttk.Entry(show="*")
                    role_entry = ttk.Entry()
                    
                    #Fills in existing information about the selected user:
                    first_name_entry.insert(0, userInfo[0][0])
                    last_name_entry.insert(0, userInfo[0][1])
                    username_entry.insert(0, userInfo[0][2])
                    password_entry.insert(0, userInfo[0][3])
                    role_entry.insert(0, userInfo[0][4])
                    row_id =  userInfo[0][5]
                    
                    first_name_label = ttk.Label(text="First name")
                    last_name_label = ttk.Label(text="Last name")
                    username_label = ttk.Label(text="Username")
                    password_label = ttk.Label(text="Password")
                
                    submit_button = ttk.Button(self.root,text="Submit",command=lambda: submitChanges(fields, widgets), width=20)        
                    exit_button = ttk.Button(self.root,text="Exit",command=lambda: self.viewUsers(widgets,"update"),width=20)
                
                    first_name_label.pack()
                    first_name_entry.pack()
                
                    last_name_label.pack()
                    last_name_entry.pack()
                
                    username_label.pack()
                    username_entry.pack()
                
                    password_label.pack()
                    password_entry.pack()
                
                    roleEntry = StringVar()
                    roleEntry.set(userInfo[0][4])
                            
                    #List of user roles:
                    roles = ["Admin", "Director", "Manager", "Chef", "Staff"]
                    
                    #Drop down menu for user roles
                    drop = OptionMenu(self.root, roleEntry, *roles)
                    drop.pack()
                
                    submit_button.pack()
                    exit_button.pack()
                    
                    fields = [first_name_entry,last_name_entry,username_entry,password_entry,roleEntry,row_id]
                
                    widgets = [first_name_label, last_name_label,username_label,password_label,first_name_entry,last_name_entry,username_entry,password_entry,drop,submit_button,exit_button]
                                
                    #Finalises changes made to the selected user on the SQL server:
                    def submitChanges(fields, widgets):
                        for x in fields:
                                if x.get() == "" or fields[4].get() == "Role":
                                    messagebox.showerror("Incomplete Fields", "Please Complete All Fileds")
                                    break
                            
                                else:
                                    UserSQL.updateUser(self.branch,fields)
                                    messagebox.showinfo("User Updated", "User Has Been Updated")
                                    adminCredentials = UserSQL.check_admin_updated(self.credentials,self.branch) #Makes any changes to Admin in real time
                                    self.credentials = adminCredentials
                                    self.viewUsers(widgets,"update")
                                    break
                        
                        
#DELETE USER: 
    def deleteUser(self, widgets,table):

        userInfo = []
        for i in table.selection():
            a = tuple((table.item(i)['values']))
            if a[0] != " ":
                userInfo.append(table.item(i)['values'])
                #Asks for confirmation for the selected user to be deleted:
                yes_no = messagebox.askyesno("Delete User?", "Are You Sure You Want To Delete This User?")           
                if yes_no:
                        UserSQL.deleteUser(userInfo,self.branch)
                        messagebox.showinfo("Account Deleted", "Account Successfully Deleted")
                        if UserSQL.check_admin_deleted(self.credentials, self.branch) == True:
                            LoginGUI(widgets,self.branch,self.root)
                        else:
                            self.viewUsers(widgets,"delete")
                else:
                    self.viewUsers(widgets,"delete")
            
                
#GO BACK TO USER MANAGEMENT PAGE
    #Takes user back to the usermanagement page. Applies to create,read,update and delete
    def goBackToUserManagement(self, widgets):
                for x in widgets:
                    x.pack_forget() 
                UserGUI(self.credentials,self.branch,self.root)


#GO BACK TO USER HOME PAGE
    #Allows the user to go back to their home page
    def back(self,widgets):
        if self.credentials[3] == "Admin":
            from AdminGUI.AdminGUI import ADMIN
            ADMIN(widgets,self.credentials, self.branch,self.root) 