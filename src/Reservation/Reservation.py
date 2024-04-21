import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import date

class TableReservation:
    
    def __init__(self, widgets, credentials, branch, root):
        self.root = root
        self.credentials = credentials
        self.branch = branch
        self.foodReservationsTable = ttk.Treeview(self.root, columns=('customer_name', 'reservation_time', 'end_time', 'guest_num', 'table_id'), show='headings')
        
        for x in widgets:
            x.pack_forget()
            
        reservations_label = ttk.Label(self.root, text="Reservations", font=("Arial", 28))
        reservations_label.pack()
        
        add_reservation_button = ttk.Button(self.root, text="Add Reservation", command=lambda:self.addReservation(widgets), width=50)
        view_reservations_button = ttk.Button(self.root, text="View Reservations", command=lambda:self.viewReservations(widgets, "view"), width=50)
        update_reservation_button = ttk.Button(self.root, text="Update Reservation", command=lambda:self.viewReservations(widgets, "update"), width=50)
        cancel_reservation_button = ttk.Button(self.root, text="Cancel Reservation", command=lambda:self.viewReservations(widgets, "cancel"), width=50)
        back_button = ttk.Button(self.root, text="Back", command=lambda:self.back(widgets), width=50)
        
        add_reservation_button.pack()
        view_reservations_button.pack()
        update_reservation_button.pack()
        cancel_reservation_button.pack()
        back_button.pack()

        widgets = [reservations_label, add_reservation_button, view_reservations_button, update_reservation_button, cancel_reservation_button, back_button]        
        
    def addReservation(self, widgets):
        
        def exit(widgets, fields):
            for x in fields:
                if x.get() != "":
                    confirm_exit = messagebox.askyesno("Exit?", "Are You Sure You Want To Exit?")
                    if confirm_exit:
                        TableReservation(widgets, self.credentials, self.branch, self.root)
                        break
                else:
                    TableReservation(widgets, self.credentials, self.branch, self.root)
                    break
        
        # Function to reserve a table
        def reserve_table(fields):
            
            valid = True
            allFilled = True
            validText = True
            validTimes = True
            
            customer_name_entry = fields[0].get()
            start_time_entry = start_time_combobox.get()
            finish_time_entry = finish_time_combobox.get()
            seats_entry = fields[3].get()
            table_entry = fields[4].get()
            calendar_entry = fields[5].get_date()
            
            fields = [customer_name_entry, start_time_entry, finish_time_entry, seats_entry, table_entry, calendar_entry]
            
            for x in fields:
                if x == "":
                    messagebox.showerror("Incomplete Fields", "Please Fill In All Fields")
                    allFilled = False
                    break
                
            if allFilled:
                if not customer_name_entry.replace(" ", "").isalpha():
                    validText = False
                    messagebox.showerror("Invalid Customer Name", "Customer Name Can Only Contain Letters")
                
                if not table_entry.isnumeric():
                    validText = False
                    messagebox.showerror("Invalid Table Number", "Table Number Must Be A Valid Integer.")
                    
                elif not seats_entry.isnumeric():
                    validText = False
                    messagebox.showerror("Invalid Seats Input", "Number Of Seats Must Be A Valid Integer.")
                    
                # Reservation validation and submission logic goes here...
                if valid:
                    messagebox.showinfo("Success", "Table Reserved Successfully.")
                    
        for x in widgets:
            x.pack_forget()
            
        todays_date = date.today()
        
        reservation_label = ttk.Label(self.root, text="Table Reservation", font=("Arial", 20))
        reservation_label.pack()
  
        customer_name_label = ttk.Label(self.root, text="Customer Name:")
        customer_name_label.pack()
        
        customer_name_entry = ttk.Entry(self.root)
        customer_name_entry.pack()
        
        start_time_label = ttk.Label(self.root, text="Start Time:")
        start_time_label.pack()
        
        # List of time options in 24-hour clock format
        start_times = [f"{hour:02d}:00" for hour in range(0, 24)]
        start_time_combobox = ttk.Combobox(self.root, values=start_times, state="readonly")
        start_time_combobox.pack()
        
        finish_time_label = ttk.Label(self.root, text="Finish Time:")
        finish_time_label.pack()
        
        # List of time options in 24-hour clock format
        finish_times = [f"{hour:02d}:00" for hour in range(0, 24)]
        finish_time_combobox = ttk.Combobox(self.root, values=finish_times, state="readonly")
        finish_time_combobox.pack()
        
        seats_label = ttk.Label(self.root, text="Guest Number:")
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

        reserve_button = ttk.Button(self.root, text="Reserve", command=lambda: reserve_table(fields))
        reserve_button.pack()
        
        exit_button = ttk.Button(self.root, text="Exit", command=lambda: exit(widgets, fields))
        exit_button.pack()
        
        fields = [customer_name_entry, start_time_combobox, finish_time_combobox, seats_entry, table_entry, calendar]
        
        widgets = [customer_name_entry, customer_name_label, start_time_combobox, start_time_label, finish_time_combobox, finish_time_label, seats_entry, seats_label, reservation_label, table_label, table_entry, date_label, calendar, reserve_button, exit_button]
        
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
            back_button = ttk.Button(self.root, text="Back", command=lambda:TableReservation(widgets,self.credentials,self.branch,self.root))
            back_button.pack()
            widgets = [self.foodReservationsTable,back_button]
        
        elif operation =="update":
            update_button = ttk.Button(self.root, text="Update",)
            update_button.pack()
            back_button = ttk.Button(self.root, text="Back", command=lambda:TableReservation(widgets,self.credentials,self.branch,self.root))
            back_button.pack()
            widgets = [self.foodReservationsTable,update_button,back_button]
            
        else:
            cancel_button = ttk.Button(self.root, text="Cancel Reservation",)
            cancel_button.pack()
            back_button = ttk.Button(self.root, text="Back", command=lambda:TableReservation(widgets,self.credentials,self.branch,self.root))
            back_button.pack()
            widgets = [self.foodReservationsTable,cancel_button,back_button]
        
        # Here you would fetch and display reservation data from your database
        
    def back(self, widgets):
        for x in widgets:
            x.pack_forget()
        TableReservation(widgets,self.credentials,self.branch,self.root)

root = tk.Tk()
root.title("Restaurant Reservation System")
root.geometry("600x400")

widgets = []

# Sample credentials and branch info
credentials = {"username":"user","password":"pass"}
branch = {"name":"My Restaurant","location":"My City"}

TableReservation(widgets, credentials, branch, root)

root.mainloop()
