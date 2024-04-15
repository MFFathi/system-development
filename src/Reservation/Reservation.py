from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox
import ADMIN
import DIRECTOR
import MANAGER
import CHEF
import STAFF

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
            
        

    def back(self,widgets,credentials,branch,database):
        
        for x in widgets:
             x.pack_forget()
             
        if credentials[3] == "Admin":
            ADMIN(credentials,branch,database) 
        elif credentials[3] == "Manager":
            MANAGER(credentials,branch,database)
        elif credentials[3] == "Director":
            DIRECTOR(credentials,branch,database) 
        elif credentials[3] == "Chef":
            CHEF(credentials,branch,database)
        elif credentials[3] == "Staff":
            STAFF(credentials,branch,database) 