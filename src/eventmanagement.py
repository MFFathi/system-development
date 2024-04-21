from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox
'''
class Events():
    
    def __init__(self,credentials,branch,database,root):
        
        events_label = ttk.Label(root,text="Events",font=("Arial", 28))

        create_event_button = ttk.Button(root,text="Create Event",width=50)
        read_events_button = ttk.Button(root,text="Read Events",width=50)
        update_event_button = ttk.Button(root,text="Update Event",width=50)
        delete_event_button = ttk.Button(root,text="Delete Event",width=50)
        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,database,root),width=50) 

        events_label.pack()
        create_event_button.pack()
        read_events_button.pack()
        update_event_button.pack()
        delete_event_button.pack()
        back_button.pack()
        
        widgets = [events_label,
                   create_event_button,
                   read_events_button,
                   update_event_button,
                   delete_event_button,
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
'''
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
from datetime import datetime

class EventManagementPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Event Management")
        self.geometry("600x600")  

        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="Francis",
            password="@Deadmaul/951*",
            database="horizon_restaurant_bristol"
        )
        self.cursor = self.connection.cursor()

        self.create_widgets()

    def create_widgets(self):
        eventmanagement_frame = ttk.Frame(self)
        eventmanagement_frame.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style(eventmanagement_frame)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="white")
        # This is the entry section for Event Name- 22066867
        label_name = tk.Label(eventmanagement_frame, text="Event Name", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_name.pack(anchor=tk.N, pady=5)
        entry_name = tk.Entry(eventmanagement_frame, bd=0, width=30)
        entry_name.pack(anchor=tk.N, pady=5)
        # This is the entry section for Event Description- 22066867
        label_description = tk.Label(eventmanagement_frame, text="Event Description", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_description.pack(anchor=tk.N, pady=5)
        entry_description = tk.Entry(eventmanagement_frame, bd=0, width=30)
        entry_description.pack(anchor=tk.N, pady=5)
        # This is the entry section for Date of Event- 22066867
        label_date = tk.Label(eventmanagement_frame, text="Date of Event (YYYY-MM-DD)", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_date.pack(anchor=tk.N, pady=5)
        entry_date = tk.Entry(eventmanagement_frame, bd=0, width=30)
        entry_date.pack(anchor=tk.N, pady=5)
        # This is the entry section for the Start Time- 2206686
        label_start_time = tk.Label(eventmanagement_frame, text="Start Time (HH:MM)", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_start_time.pack(anchor=tk.N, pady=5)
        entry_start_time = tk.Entry(eventmanagement_frame, bd=0, width=30)
        entry_start_time.pack(anchor=tk.N, pady=5)
        # This is the entry section for End Time- 22066867 
        label_end_time = tk.Label(eventmanagement_frame, text="End Time (HH:MM)", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_end_time.pack(anchor=tk.N, pady=5)
        entry_end_time = tk.Entry(eventmanagement_frame, bd=0, width=30)
        entry_end_time.pack(anchor=tk.N, pady=5)

        label_type = tk.Label(eventmanagement_frame, text="Event Type", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_type.pack(anchor=tk.N, pady=5)
        type_options = ["Birthday", "Anniversary", "Work Party"]
        combo_type = ttk.Combobox(eventmanagement_frame, values=type_options)
        combo_type.pack(anchor=tk.N, pady=5)
        # This is the entry section for the Phone Number- 22066867
        label_phone = tk.Label(eventmanagement_frame, text="Phone Number", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_phone.pack(anchor=tk.N, pady=5)
        entry_phone = tk.Entry(eventmanagement_frame, bd=0, width=30)
        entry_phone.pack(anchor=tk.N, pady=5)
        # This is the entry section for the email- 22066867
        label_email = tk.Label(eventmanagement_frame, text="Email", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_email.pack(anchor=tk.N, pady=5)
        entry_email = tk.Entry(eventmanagement_frame, bd=0, width=30)
        entry_email.pack(anchor=tk.N, pady=5)
        # This is the entry section for Address- 22066867
        label_address = tk.Label(eventmanagement_frame, text="Address", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_address.pack(anchor=tk.N, pady=5)
        entry_address = tk.Entry(eventmanagement_frame, bd=0, width=30)
        entry_address.pack(anchor=tk.N, pady=5)
        # This is the combobox for Event Status- 22066867
        label_status = tk.Label(eventmanagement_frame, text="Event Status", font=('Consolas', 10, 'bold'), fg="black", background="white")
        label_status.pack(anchor=tk.N, pady=5)
        status_options = ["Accept", "No Action taken yet", "Finished", "Cancelled", "Reject"]
        combo_status = ttk.Combobox(eventmanagement_frame, values=status_options)
        combo_status.pack(anchor=tk.N, pady=5)
        # This is the button to submit- 22066867
        submit_button = tk.Button(eventmanagement_frame, text="Submit", command=lambda: self.submit_button_clicked(entry_name, entry_description, entry_date, entry_start_time, entry_end_time, combo_type, entry_phone, entry_email, entry_address, combo_status), background="#FF0000", fg="white", font=('Consolas', 10, 'bold'), width=6, height=2, bd=0, cursor="hand2")
        submit_button.pack(ipadx=20, ipady=20, padx=10, pady=10)
        # This is the button to view and modify the Event Status- 22066867
        view_modify_button = tk.Button(eventmanagement_frame, text="View and Modify Status", command=self.view_modify_status, background="#0000FF", fg="white", font=('Consolas', 10, 'bold'), width=25, height=2, bd=0, cursor="hand2")
        view_modify_button.pack(ipadx=20, ipady=20, padx=10, pady=10)
        # This is to store Treeview values by EventID- 22066867
        self.events_dict = {}

    def submit_button_clicked(self, entry_name, entry_description, entry_date, entry_start_time, entry_end_time, combo_type, entry_phone, entry_email, entry_address, combo_status):
        print("Debugging: Starting using the submit_button_clicked method")
        # This is to retrieve values from entry fields- 22066867
        name = entry_name.get()
        description = entry_description.get()
        date_str = entry_date.get()
        start_time = entry_start_time.get()
        end_time = entry_end_time.get()
        event_type = combo_type.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        status = combo_status.get()
        # This is to validate if all the fields are filled- 22066867
        if not name or not description or not date_str or not start_time or not end_time or not event_type or not phone or not email or not address or not status:
            messagebox.showerror("Error", "All fields must be filled.")
            return
        # This is to validate the date format- 22066867
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format, it must be in this format YYYY-MM-DD.")
            return
        # This is to validate the time format- 22066867
        try:
            datetime.strptime(start_time, "%H:%M")
            datetime.strptime(end_time, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format, it must be in this format HH:MM.")
            return
        # This is to check if the date entered is after the current date- 22066867
        current_date = datetime.now().date()
        if date <= current_date:
            messagebox.showerror("Error", "Date of Event must be after the current date.")
            return
        # This is to insert the data into events table- 22066867
        query = "INSERT INTO events (EventName, EventDescription, date, start_time, end_time, type, phone_number, email, address, EventStatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, description, date, start_time, end_time, event_type, phone, email, address, status)

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            messagebox.showinfo("Success", "Data has been inserted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def view_modify_status(self):
        view_events_window = tk.Toplevel(self)
        view_events_window.title("View and Modify Status of Events")
        view_events_window.geometry("800x400") 
        events_treeview = ttk.Treeview(view_events_window, columns=("EventName", "EventDescription", "date", "start_time", "end_time", "type", "phone_number", "email", "address", "EventStatus"))
        events_treeview.heading("EventName", text="Event Name")
        events_treeview.heading("EventDescription", text="Event Description")
        events_treeview.heading("date", text="Date of Event")
        events_treeview.heading("start_time", text="Start Time")
        events_treeview.heading("end_time", text="End Time")
        events_treeview.heading("type", text="Event Type")
        events_treeview.heading("phone_number", text="Phone Number")
        events_treeview.heading("email", text="Email")
        events_treeview.heading("address", text="Address")
        events_treeview.heading("EventStatus", text="Event Status")

        events_treeview.pack(padx=10, pady=10)

        modify_status_button = tk.Button(view_events_window, text="Modify Status", command=lambda: self.modify_event_status(events_treeview), background="#0000FF", fg="white", font=('Consolas', 10, 'bold'), width=15, height=2, bd=0, cursor="hand2")
        modify_status_button.pack(pady=10)

        query = "SELECT EventName, EventDescription, date, start_time, end_time, type, phone_number, email, address, EventStatus, id FROM events"
        self.cursor.execute(query)
        events = self.cursor.fetchall()

        for event in events:
            if not events_treeview.exists(event[0]):
                events_treeview.insert("", "end", values=event)

                self.events_dict[event[0]] = event

    def modify_event_status(self, events_treeview):
        selected_item = events_treeview.selection()

        if not selected_item:
            messagebox.showerror("Error", "Please select an event.")
            return

        for i in events_treeview.selection():
            event_id = events_treeview.item(i)['values'][10]

        current_status_query = "SELECT EventStatus FROM events WHERE id = %s"
        self.cursor.execute(current_status_query, (event_id,))
        current_status = self.cursor.fetchone()[0]

        # This is to create a Combobox for selecting the new status- 22066867
        statusChange = Tk()
        statusChange.title("Change Event Stauts")
        statusChange.geometry("250x250")
        status_label = ttk.Label(statusChange,text="Change Status")
        status_label.pack()
        status_options = ["Accept", "No Action taken yet", "Finished", "Cancelled", "Reject"]
        new_status_combo = ttk.Combobox(statusChange, values=status_options)
        new_status_combo.current(status_options.index(current_status))
        new_status_combo.pack()
        confirm_button = ttk.Button(statusChange,text="Confirm Modification",command=lambda:self.confirm_modification(new_status_combo,event_id,events_treeview,statusChange))
        confirm_button.pack()

        #self.wait_window(new_status_combo)

        # This is to get the selected status- 22066867
        new_status = new_status_combo.get()

        # To validate the entered status- 22066867
        allowed_statuses = ["Accept", "No Action taken yet", "Finished", "Cancelled", "Reject"]

        if new_status not in allowed_statuses:
            messagebox.showerror("Error", "Invalid status. Please enter one of the following: Accept, No Action taken yet, Finished, Cancelled, Reject.")
            return
        # In case the user cancels- 22066867
        if not new_status:
            return  

    def confirm_modification(self,new_status_combo,event_id,events_treeview,statusChange):
        print("New = ",new_status_combo.get())
        update_status_query = "UPDATE events SET EventStatus = %s WHERE id = %s"
        self.cursor.execute(update_status_query, (new_status_combo.get(), event_id))
        self.connection.commit()

        #self.events_dict[event_id] = (event_id, self.events_dict[event_id][1], self.events_dict[event_id][2], self.events_dict[event_id][3], new_status)

        events_treeview.delete(*events_treeview.get_children())

        for event_id, values in self.events_dict.items():
            events_treeview.insert("", "end", iid=values[0], tags=(values[0],), values=values[1:])

        messagebox.showinfo("Success", "Status has been updated successfully.")
        statusChange.destroy()
        self.modify_event_status(events_treeview)

    def validate_email(self, email):
        # This is to check if "@" sign is present in the email address- 22066867
        if "@" not in email:
            return False
        else:
            return True

if __name__ == "__main__":
    app = EventManagementPage()
    app.mainloop()
