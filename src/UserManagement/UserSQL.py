from Databases.Databases import Databases
'''
The purpose of this file is to make any changes to the users table in the database.
'''

class UserSQL():
    
#CREATE USER:
    def createUser(branch, fields):
                
        first_name = fields[0].get()
        last_name = fields[1].get()
        username = fields[2].get()
        password = fields[3].get()
        role = fields[4].get()
        
        sql = "INSERT INTO users (first_name, last_name, username, password, role) VALUES (%s, %s, %s, %s, %s)"
        val = (first_name, last_name, username, password, role)                     
        
        #Commits Changes To Relevant Database Based On The Branch That The User Is Making Changes To:
        if (branch == "Birmingham"):
            try:
                with Databases.birmingham_db.cursor() as database:
                    database.execute(sql,val)
                    Databases.birmingham_db.commit()
            finally:  
                    pass         
        
        elif(branch == "Bristol"):
            try:
                with Databases.bristol_db.cursor() as database:
                    database.execute(sql,val)
                    Databases.bristol_db.commit()
            finally: 
                    pass                             

        elif(branch == "Cardiff"):
            try:
                with Databases.cardiff_db.cursor() as database:
                    database.execute(sql,val)
                    Databases.cardiff_db.commit()
            finally:  
                    pass         

        elif(branch == "Glasgow"):
            try:
                with Databases.glasgow_db.cursor() as database:
                    database.execute(sql,val)
                    Databases.glasgow_db.commit()
            finally:  
                    pass         

        elif(branch == "London"):
            try:
                with Databases.london_db.cursor() as database:
                    database.execute(sql,val)
                    Databases.london_db.commit()
            finally: 
                    pass         
                
        
        elif(branch == "Manchester"):
            try:
                with Databases.manchester_db.cursor() as database:
                    database.execute(sql,val)
                    Databases.manchester_db.commit()
            finally:  
                    pass         
                
        
        elif(branch == "Nottingham"):
            try:
                with Databases.nottingham_db.cursor() as database:
                    database.execute(sql,val)
                    Databases.nottingham_db.commit()
            finally:  
                    pass       
                    
                    
#GET USERS:
    def getUsers(branch):
        
        if branch == "Birmingham":
            database = Databases.birmingham_db.cursor()
        
        elif branch == "Bristol":
            database = Databases.bristol_db.cursor()
            
        elif branch == "Cardiff":
            database = Databases.cardiff_db.cursor()
            
        elif branch == "Glasgow":
            database = Databases.glasgow_db.cursor()
            
        elif branch == "London":
            database = Databases.london_db.cursor()
            
        elif branch == "Manchester":
            database = Databases.manchester_db.cursor()
            
        elif branch == "Nottingham":
            database = Databases.nottingham_db.cursor()
        
        database.execute("SELECT first_name, last_name, username, password, role, id FROM users ORDER BY last_name DESC")
        viewAccountList = database.fetchall()
        
        return viewAccountList
    
#USER ALREADY EXISTS:
    def username_in_use(branch):
        
        if branch == "Birmingham":
            database = Databases.birmingham_db.cursor()
        
        elif branch == "Bristol":
            database = Databases.bristol_db.cursor()
            
        elif branch == "Cardiff":
            database = Databases.cardiff_db.cursor()
            
        elif branch == "Glasgow":
            database = Databases.glasgow_db.cursor()
            
        elif branch == "London":
            database = Databases.london_db.cursor()
            
        elif branch == "Manchester":
            database = Databases.manchester_db.cursor()
            
        elif branch == "Nottingham":
            database = Databases.nottingham_db.cursor()
        
        database.execute("SELECT username FROM users")
        usernamesList = database.fetchall()
        
        return usernamesList
                           

#UPDATE ACCOUNT:
    def updateUser(branch, fields):
                   
        first_name = fields[0].get()
        last_name = fields[1].get()
        username = fields[2].get()
        password = fields[3].get()
        role = fields[4].get()
        row_id = fields[5]
                
        database = Databases.getDatabase(branch).cursor()

        firstnameSQL = "UPDATE users SET first_name = %s WHERE id = %s"
        val = (first_name,row_id)
        database.execute(firstnameSQL,val)

        lastnameSQL = "UPDATE users SET last_name = %s WHERE id = %s"
        val = (last_name,row_id)
        database.execute(lastnameSQL,val)

        usernameSQL = "UPDATE users SET username = %s WHERE id = %s"
        val = (username,row_id)
        database.execute(usernameSQL,val)

        passwordSQL = "UPDATE users SET password = %s WHERE id = %s"
        val = (password,row_id)
        database.execute(passwordSQL,val)

        roleSQL = "UPDATE users SET role = %s WHERE id = %s"
        val = (role,row_id)
        database.execute(roleSQL,val)
        
        #Commits Changes To Relevant Database Based On The Branch That The User Is Making Changes To:
        if (branch == "Birmingham"):
            Databases.birmingham_db.commit()
            
        elif(branch == "Bristol"):
            Databases.bristol_db.commit()
        
        elif(branch == "Cardiff"):
            Databases.cardiff_db.commit()
          
        elif(branch == "Glasgow"):
            Databases.glasgow_db.commit()
 
        elif(branch == "London"):
            Databases.london_db.commit()

        elif(branch == "Manchester"):
            Databases.manchester_db.commit()
        
        elif(branch == "Nottingham"):
            Databases.nottingham_db.commit()
            

#DELETE ACCOUNT: 
    def deleteUser(userInfo,branch):
        
        sql = "DELETE FROM users WHERE id = %s"
        row_id = (userInfo[0][5], )
        
        #Commits Changes To Relevant Database Based On The Branch That The User Is Making Changes To:
        if (branch == "Birmingham"):
            try:
                with Databases.birmingham_db.cursor() as database:
                    database.execute(sql,row_id)
                    Databases.birmingham_db.commit()
            finally:  
                    pass         
        
        
        elif(branch == "Bristol"):
            try:
                with Databases.bristol_db.cursor() as database:
                    database.execute(sql,row_id)
                    Databases.bristol_db.commit()
            finally: 
                    pass      
                                       

        elif(branch == "Cardiff"):
            try:
                with Databases.cardiff_db.cursor() as database:
                    database.execute(sql,row_id)
                    Databases.cardiff_db.commit()
            finally:  
                    pass         


        elif(branch == "Glasgow"):
            try:
                with Databases.glasgow_db.cursor() as database:
                    database.execute(sql,row_id)
                    Databases.glasgow_db.commit()
            finally:  
                    pass 
                        

        elif(branch == "London"):
            try:
                with Databases.london_db.cursor() as database:
                    database.execute(sql,row_id)
                    Databases.london_db.commit()
            finally: 
                    pass         
                
        
        elif(branch == "Manchester"):
            try:
                with Databases.manchester_db.cursor() as database:
                    database.execute(sql,row_id)
                    Databases.manchester_db.commit()
            finally:  
                    pass         
                
        
        elif(branch == "Nottingham"):
            try:
                with Databases.nottingham_db.cursor() as database:
                    database.execute(sql,row_id)
                    Databases.nottingham_db.commit()
            finally:  
                    pass     
  
 
#Checks if an admin's first name has been updated:
    def check_admin_updated(credentials, branch):
        first_name = credentials[0]
        username = credentials[1]
        password = credentials[2]
        role = credentials[3]
                    
        accounts = UserSQL.getUsers(branch)
        
        admin_upated = False
        
        accountsList = []
            
        for x in accounts:
            accountsList.append(x)
        
        #Where: first_name[0], last_name[1], username[2], password[3], role[4], id[5]
        
        #Updates admin's first name in real time, if changed:    
        for x in accountsList:
            first = x[0] #Looks for the first name
            if (username == x[2]) and (password == x[3]):#Looks for the admin's password to match 
                #Admin's first name has been changed
                    if (first_name != x[0]): 
                        newCredentials = (first, username,password,role)
                        admin_upated = True
                        
        if admin_upated == True:
            return newCredentials
        else:
            return credentials

#If admin deletes their own account, they will be logged out of the system:
    def check_admin_deleted(credentials,branch):
        
        username = credentials[1]
        password = credentials[2]
        role = credentials[3]
        deleted = True
        
        accounts = UserSQL.getUsers(branch)
    
        accountsList = []
            
        for x in accounts:
            accountsList.append(x)
        
        #Where: first_name[0], last_name[1], username[2], password[3], role[4], id[5]
        for x in accountsList:
            if (username == x[2]) and (password == x[3]) and (role == "Admin"): 
                deleted = False
                
        return deleted