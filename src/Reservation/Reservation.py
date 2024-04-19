from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import date
from tkinter import messagebox
from Reservation.BranchReservation import BranchReservation

'''
today = datetime.today().date()
viewFoodCategories = None
foodCategoriesTable = None
foodItemsInCategory = None

root = Tk()

import mysql.connector 

#DATABASES TO CONNECT TO:
birmingham_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_birmingham"
    )


bristol_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_bristol"
    )

cardiff_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_cardiff"
    )

glasgow_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_glasgow"
    )

london_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_london"
    )

manchester_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_manchester"
    )

nottingham_db = mysql.connector.connect(
    host = "localhost",
    user="Francis",
    password="@Deadmaul/951*",
    database="horizon_restaurant_nottingham"
    )

class Reservation():
    
    def __init__(self,credentials,branch,database):

        reservation_label = ttk.Label(root,text="Reservation",font=("Arial", 28))
        reservation_label.pack()
        
        create_reservation_button = ttk.Button(root,text="Create Reservation",command=lambda: self.createReservation(widgets,credentials, branch, database),width=50)
        read_reservation_button = ttk.Button(root,text="Read Reservation",command=lambda: self.readReservation(widgets, database, credentials, branch),width=50)
        update_reservation_button = ttk.Button(root,text="Update Reservation",command=lambda: self.updateReservation(widgets,credentials,branch, database),width=50)
        delete_reservation_button = ttk.Button(root,text="Delete Reservation",command=lambda: self.deleteReservation(widgets,credentials,branch, database),width=50)
        back_button = ttk.Button(root,text="Back",command=lambda: self.back(widgets,credentials,branch,database),width=50)
      

        create_reservation_button.pack()
        read_reservation_button.pack()
        update_reservation_button.pack()
        delete_reservation_button.pack()
        
        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,database),width=50) 

        back_button.pack()
        
        widgets = [reservation_label,
                   create_reservation_button,
                   read_reservation_button,
                   update_reservation_button,
                   delete_reservation_button,
                   back_button]

    
    def createReservation(self,widgets, credentials, branch, database):
        for x in widgets:
            x.pack_forget()
        
        self.cal = Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day, mindate=today, date_pattern="yyyy-mm-dd")
        self.cal.pack()
        numbers = list(range(1,11))
        no_ppl = tk.StringVar()
        no_ppllabel = tk.Label(root, text="Select Number of Guests")
        no_ppllabel.pack()
        dropdown = ttk.Combobox(root, textvariable=no_ppl, values=numbers, state="readonly")
        dropdown.pack()
        dropdown.set(numbers[0])
        customer_label = tk.Label(root, text="Customer Name")
        customer_label.pack()
        customer = tk.Entry(root)
        customer.pack()
        email_label = tk.Label(root, text='Email')
        email_label.pack()
        email = tk.Entry(root)
        email.pack()
  
        

        def goBackToReservation(widgets,credentials, branch, database):
            for x in widgets:
                x.pack_forget() 
            Reservation(credentials,branch,database)
        
        def submitReserv():
            customer_name = customer.get()
            customer_email = email.get()
            number_of_ppl = no_ppl.get()
            reservdate = self.cal.get_date()
            
            query = ("INSERT INTO reservations (customer_name, email, number_of_people, reservation_date) VALUES (%s, %s, %s, %s)")
            database.execute(query, (customer_name, customer_email, number_of_ppl, reservdate))
                    #Commits Changes To Relevant Database Based On The Branch That The User Is Making Changes To:
            if (branch == "Birmingham"):
                birmingham_db.commit()
                 
            elif(branch == "Bristol"):
                bristol_db.commit()
                 
            elif(branch == "Cardiff"):
                cardiff_db.commit()
            
            elif(branch == "Glasgow"):
                    glasgow_db.commit()                 

            elif(branch == "London"):
                    london_db.commit()
            
            elif(branch == "Manchester"):
                    manchester_db.commit()
            
            elif(branch == "Nottingham"):
                    nottingham_db.commit()
            
            messagebox.showinfo("Confirmation", "Reservation Successful")
        create_btn = tk.Button(root, text="Confirm", command=submitReserv)
        create_btn.pack(pady=15)
        

        back_button = ttk.Button(root,text="Back",command=lambda: goBackToReservation(widgets, credentials, branch, database),width=20)

        back_button.pack()
        
        
        widgets = [create_btn,
                   no_ppllabel,
                   self.cal,
                   customer_label,
                   email_label,
                   dropdown,
                   customer,
                   email,
                   back_button
                   ]
            
    def readReservation(self, widgets, database, credentials, branch):
        for x in widgets:
            x.pack_forget()
            
        database.execute("SELECT customer_id, customer_name, reservation_date, number_of_people, email FROM reservations")
        viewReservs = database.fetchall()

        
        table = ttk.Treeview(root,columns=("customer_id", "customer_name", "reserv_date", "noppl", "email"), show='headings')
        table.heading('customer_id', text = 'Customer ID')
        table.heading('customer_name', text = 'Customer Name')
        table.heading('reserv_date', text = 'Reservation Date')
        table.heading('noppl', text = 'Number of People')
        table.heading('email', text = 'Email')
        
        table.pack(fill='both', expand=TRUE)
        
        for x in viewReservs:
            customer_id = x[0]
            customer_name = x[1]
            reserv_date = x[2]
            noppl = x[3]
            email = x[4]
            data = (customer_id, customer_name, reserv_date, noppl, email)
            table.insert(parent = '', index=0, values = data)

        back_button = ttk.Button(root,text="Back",command=lambda: goBackToReservation(widgets, credentials, branch, database),width=20)

        back_button.pack()
        
        widgets = [back_button,
                   table
                   ]
        
        def goBackToReservation(widgets,credentials, branch, database):
            for x in widgets:
                x.pack_forget() 
            Reservation(credentials,branch,database)
        

    def updateReservation(self,widgets, credentials, branch, database):
        for x in widgets:
            x.pack_forget()
            
        database.execute("SELECT customer_id, customer_name, reservation_date, number_of_people, email FROM reservations")
        viewReservs = database.fetchall()

        
        self.table = ttk.Treeview(root,columns=("customer_id", "customer_name", "reserv_date", "noppl", "email"), show='headings')
        self.table.heading('customer_id', text = 'Customer ID')
        self.table.heading('customer_name', text = 'Customer Name')
        self.table.heading('reserv_date', text = 'Reservation Date')
        self.table.heading('noppl', text = 'Number of People')
        self.table.heading('email', text = 'Email')
        
        self.table.pack(fill='both', expand=TRUE)
        
        for x in viewReservs:
            customer_id = x[0]
            customer_name = x[1]
            reserv_date = x[2]
            noppl = x[3]
            email = x[4]
            data = (customer_id, customer_name, reserv_date, noppl, email)
            self.table.insert(parent = '', index=0, values = data)
        cal = Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day, mindate=today, date_pattern="yyyy-mm-dd")
        cal.pack()
        nmber = list(range(1,11)) 
        slct = tk.StringVar()
        slctlbl = tk.Label(root, text="Updated Number of Guests")
        slctlbl.pack()
        drop = ttk.Combobox(root, textvariable=slct, values=nmber, state='readonly')
        drop.pack(side='top')
        drop.set(nmber[0])
        newcustomerlbl = tk.Label(root, text="New Customer Name")
        newcustomerlbl.pack()
        newcustomer = tk.Entry(root)
        newcustomer.pack()
        email_lbl = tk.Label(root, text="New Email")
        email_lbl.pack()
        newemail = tk.Entry(root)
        newemail.pack()
        update_button = ttk.Button(root, text="Update", command=lambda: update_selected_row(database, branch, credentials, widgets), width=20)
        update_button.pack()
        back_button = ttk.Button(root,text="Back",command=lambda: goBackToReservation(widgets, credentials, branch, database),width=20)
        back_button.pack()


        def goBackToReservation(widgets,credentials, branch, database):
            for x in widgets:
                x.pack_forget() 
            Reservation(credentials,branch,database)
        
        def update_selected_row(database, branch, credentials, widgets):
            select_item = self.table.selection()
            if not select_item:
                messagebox.showwarning("Warning", "Please select a row to update.")
                return
            values = self.table.item(select_item, 'values')
            customer_id = values[0]
            
            newdate = cal.get_date()
            new_number_of_ppl = slct.get()
            new_customer_name = newcustomer.get()
            newcustomer_email = newemail.get()
            
            if not all([new_number_of_ppl, new_customer_name, newcustomer_email]):
                messagebox.showwarning("Warning", "Please fill in all fields.")
                return
            
            update_query = "UPDATE reservations SET customer_name=%s, reservation_date=%s, number_of_people=%s, email=%s WHERE customer_id=%s"
            database.execute(update_query, (new_customer_name, newdate, new_number_of_ppl, newcustomer_email, customer_id))
            


        
            if (branch == "Birmingham"):
                birmingham_db.commit()
                    
            elif(branch == "Bristol"):
                bristol_db.commit()
                    
            elif(branch == "Cardiff"):
                cardiff_db.commit()
            
            elif(branch == "Glasgow"):
                glasgow_db.commit()                 

            elif(branch == "London"):
                london_db.commit()
            
            elif(branch == "Manchester"):
                manchester_db.commit()
            
            elif(branch == "Nottingham"):
                nottingham_db.commit()
        
            self.table.item(select_item, values=(customer_id, new_customer_name, newdate, new_number_of_ppl, newcustomer_email))
        

        
        widgets = [back_button,
                   update_button,
                   self.table,
                   slctlbl,
                   drop,
                   newcustomer,
                   newcustomerlbl,
                   newemail,
                   email_lbl,
                   cal
                   ]
        


            
    def deleteReservation(self,widgets, credentials, branch, database):
        for x in widgets:
            x.pack_forget()
            
        for x in widgets:
            x.pack_forget()
            
        database.execute("SELECT customer_id, customer_name, reservation_date, number_of_people, email FROM reservations")
        viewReservs = database.fetchall()

        
        self.table = ttk.Treeview(root,columns=("customer_id", "customer_name", "reserv_date", "noppl", "email"), show='headings')
        self.table.heading('customer_id', text = 'Customer ID')
        self.table.heading('customer_name', text = 'Customer Name')
        self.table.heading('reserv_date', text = 'Reservation Date')
        self.table.heading('noppl', text = 'Number of People')
        self.table.heading('email', text = 'Email')
        
        self.table.pack(fill='both', expand=TRUE)
        
        for x in viewReservs:
            customer_id = x[0]
            customer_name = x[1]
            reserv_date = x[2]
            noppl = x[3]
            email = x[4]
            data = (customer_id, customer_name, reserv_date, noppl, email)
            self.table.insert(parent = '', index=0, values = data)
        delete_button = ttk.Button(root, text="Delete", command=lambda: delete_selected_row(database, branch, credentials, widgets), width=20)
        delete_button.pack()

        back_button = ttk.Button(root,text="Back",command=lambda: goBackToReservation(widgets, credentials, branch, database),width=20)
        back_button.pack()
        
        widgets = [back_button,
                   self.table,
                   delete_button
                   ]
        def delete_selected_row(database, branch, credentials, widgets):
            select_item = self.table.selection()
            if not select_item:
                messagebox.showwarning("Warning", "Please select a row to delete.")
                return
            values = self.table.item(select_item, 'values')
            customer_id = values[0]
            
            deletequery = "DELETE FROM reservations WHERE customer_id = (%s)"
            database.execute(deletequery, (customer_id,))
            if (branch == "Birmingham"):
                birmingham_db.commit()
                 
            elif(branch == "Bristol"):
                bristol_db.commit()
                 
            elif(branch == "Cardiff"):
                cardiff_db.commit()
            
            elif(branch == "Glasgow"):
                glasgow_db.commit()                 

            elif(branch == "London"):
                london_db.commit()
            
            elif(branch == "Manchester"):
                manchester_db.commit()
            
            elif(branch == "Nottingham"):
                nottingham_db.commit()
                
            self.table.delete(select_item)
            
            messagebox.showinfo("Success", "Selected reservation deleted succesfully")
            

    # Get the selected row's values")
        
        def goBackToReservation(widgets,credentials, branch, database):
            for x in widgets:
                x.pack_forget() 
            Reservation(credentials,branch,database)
            
        

    
            '''

# GUI class for table reservations
class TableReservation:
    
    def __init__(self, widgets,credentials,branch,root):
        self.root = root
        self.credentials = credentials
        self.branch = branch
        self.foodReservationsTable = ttk.Treeview(self.root,columns=('customer_name', 'reservation_time','end_time','guest_num','table_id'), show='headings')
        
        for x in widgets:
            x.pack_forget()
            
        reservations_label = ttk.Label(self.root,text="Reservations",font=("Arial",28))
        reservations_label.pack()
        
        add_reservation_button = ttk.Button(self.root,text="Add Reservation",command=lambda:self.addReservation(widgets),width=50)
        view_reservations_button = ttk.Button(self.root,text="View Reservations",command=lambda:self.viewReservations(widgets,"view"),width=50)
        update_reservation_button = ttk.Button(self.root,text="Update Reservation",command=lambda:self.viewReservations(widgets,"update"),width=50)
        cancel_reservation_button = ttk.Button(self.root,text="Cancel Reservation",command=lambda:self.viewReservations(widgets,"cancel"),width=50)
        back_button = ttk.Button(self.root,text="Back",command=lambda:self.back(widgets),width=50)
        
        add_reservation_button.pack()
        view_reservations_button.pack()
        update_reservation_button.pack()
        cancel_reservation_button.pack()
        back_button.pack()

        widgets = [reservations_label,add_reservation_button,view_reservations_button,update_reservation_button,cancel_reservation_button,back_button]        
        
    def addReservation(self,widgets):
        
        def exit(widgets,fields):
            for x in fields:
                if x.get() != "":
                    confirm_exit = messagebox.askyesno("Exit?","Are You Sure You Want To Exit?")
                    if confirm_exit:
                        TableReservation(widgets,self.credentials,self.branch,self.root)
                        break
                else:
                    TableReservation(widgets,self.credentials,self.branch,self.root)
                    break
        
        # Function to reserve a table
        def reserve_table(fields):
            
            valid = True
            allFilled = True
            validText = True
            validTimes = True
            
            customer_name_entry = fields[0].get()
            start_time_entry = fields[1].get()
            finish_time_entry = fields[2].get()
            seats_entry = fields[3].get()
            table_entry = fields[4].get()
            calendar_entry = fields[5].get_date()
            
            fields = [customer_name_entry,start_time_entry,finish_time_entry,seats_entry,table_entry,calendar_entry]
            
            for x in fields:
                if x == "":
                    messagebox.showerror("Incomplete Fields","Please Fill In All Fields")
                    allFilled = False
                    break
                
                
            if allFilled == True:
                
                if not customer_name_entry.replace(" ", "").isalpha():
                    validText = False
                    messagebox.showerror("Invalid Customer Name","Customer Name Can Only Contain Letters")
                
                if not table_entry.isnumeric():
                    validText = False
                    messagebox.showerror("Invalid Table Number", "Table Number Must Be A Valid Integer.")
                    
                elif not seats_entry.isnumeric():
                    validText = False
                    messagebox.showerror("Invalid Seats Input", "Number Of Seats Must Be A Valid Integer.")
                    
                            
                '''
                else:
                    for x in fields:
                        print(x)
                    messagebox.showinfo("Success", "Table Reserved Successfully.")
                '''

           
            #else:
                #messagebox.showerror("Error", "Table is not available at the selected date and time.")
            
        for x in widgets:
            x.pack_forget()
            
        todays_date = date.today()
        
        reservation_label = ttk.Label(self.root, text="Table Reservation", font=("Arial", 20))
        reservation_label.pack()
  
        customer_name_label = ttk.Label(self.root,text="Customer Name:")
        customer_name_label.pack()
        
        customer_name_entry = ttk.Entry(self.root)
        customer_name_entry.pack()
        
        start_time_label = ttk.Label(self.root,text="Start Time:")
        start_time_label.pack()
        
        start_time_entry = ttk.Entry(self.root)
        start_time_entry.pack()
        
        finish_time_label = ttk.Label(self.root,text="Finish Time:")
        finish_time_label.pack()
        
        finish_time_entry = ttk.Entry(self.root)
        finish_time_entry.pack()
        
        seats_label = ttk.Label(self.root,text="Guest Number:")
        seats_label.pack()
        
        seats_entry = ttk.Entry(self.root)
        seats_entry.pack()

        table_label = ttk.Label(self.root, text="Table Number:")
        table_label.pack()
        table_entry = ttk.Entry(self.root)
        table_entry.pack()


        date_label = ttk.Label(self.root, text="Reservation Date:")
        date_label.pack()
        calendar = Calendar(self.root, selectmode="day", year=todays_date.year, month=todays_date.month, day=todays_date.day)
        calendar.pack()

        reserve_button = ttk.Button(self.root, text="Reserve", command=lambda:reserve_table(fields))
        reserve_button.pack()
        
        exit_button = ttk.Button(self.root,text="Exit",command=lambda:exit(widgets,fields))
        exit_button.pack()
        
        fields = [customer_name_entry,start_time_entry,finish_time_entry,seats_entry,table_entry,calendar]
        
        widgets = [customer_name_entry,customer_name_label,start_time_entry,start_time_label,finish_time_entry,finish_time_label,seats_entry,seats_label,reservation_label,table_label,table_entry,date_label,calendar,reserve_button,exit_button]
        
    def viewReservations(self, widgets, operation):
        for x in widgets:
            x.pack_forget()
            
        for i in self.foodReservationsTable.get_children():
            self.foodReservationsTable.delete(i)
            
        #'customer_name', 'reservation_time','end_time','guest_num','table_id'
        self.foodReservationsTable.heading('customer_name',text="Customer Name")
        self.foodReservationsTable.heading('reservation_time',text="Start Time")
        self.foodReservationsTable.heading('end_time',text="Finsih Time")
        self.foodReservationsTable.heading('guest_num',text="Seats")
        self.foodReservationsTable.heading('table_id',text="Table Number")
        
        self.foodReservationsTable.pack(fill="both",expand=True)
        
        if operation == "view":
            back_button = ttk.Button(self.root,text="Back",command=lambda:TableReservation(widgets,self.credentials,self.branch,self.root))
            back_button.pack()
            widgets = [self.foodReservationsTable,back_button]
        
        elif operation =="update":
            update_button = ttk.Button(self.root,text="Update",)
            update_button.pack()
            back_button = ttk.Button(self.root,text="Back",command=lambda:TableReservation(widgets,self.credentials,self.branch,self.root))
            back_button.pack()
            widgets = [self.foodReservationsTable,back_button,update_button]
            
        elif operation == "cancel":
            delete_button = ttk.Button(self.root,text="Cancel")
            delete_button.pack()
            back_button = ttk.Button(self.root,text="Back",command=lambda:TableReservation(widgets,self.credentials,self.branch,self.root))
            back_button.pack()
            widgets = [self.foodReservationsTable,back_button,delete_button]
        
                    
    def back(self,widgets):
             
        if self.credentials[3] == "Admin":
            from Admin.Admin import Admin
            Admin(widgets,self.credentials,self.branch,self.root) 
        elif self.credentials[3] == "Manager":
            from Manager.Manager import Manager
            Manager(widgets,self.credentials,self.branch,self.root)
        elif self.credentials[3] == "Director":
            from Director.Director import Director
            Director(widgets,self.credentials,self.branch,self.root) 
        elif self.credentials[3] == "Chef":
            from Chef.Chef import Chef
            Chef(widgets,self.credentials,self.branch,self.root)
        elif self.credentials[3] == "Staff":
            from Staff.Staff import Staff
            Staff(widgets,self.credentials,self.branch,self.root) 

