
from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox
from Discounts.utils import validate_description
from Databases.Databases import Databases
from Discounts.DiscountSQL import Discount

class Discounts():
    
    def __init__(self,credentials,branch,root):
        
        self.credentials = credentials
        self.branch = branch
        self.root = root
        
        discounts_label = ttk.Label(root,text="Discounts",font=("Arial", 28))

        create_discount_button = ttk.Button(root,text="Add Discount",command=lambda:self.addDiscount(widgets),width=50)
        read_discount_button = ttk.Button(root,text="View Discounts",command=lambda:self.viewDiscounts(widgets,"view"),width=50)
        update_discount_button = ttk.Button(root,text="Update Discount",command=lambda:self.viewDiscounts(widgets,"update"),width=50)
        delete_discount_button = ttk.Button(root,text="Delete Discount",command=lambda:self.viewDiscounts(widgets,"delete"),width=50)
        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets),width=50) 

        discounts_label.pack()
        create_discount_button.pack()
        read_discount_button.pack()
        update_discount_button.pack()
        delete_discount_button.pack()
        back_button.pack()
        
        widgets = [discounts_label, create_discount_button, read_discount_button, update_discount_button, delete_discount_button,back_button]
        
    def addDiscount(self,widgets):
        for widget in widgets:
            widget.pack_forget()

        description_label = ttk.Label(self.root, text="Description:")
        description_entry = ttk.Entry(self.root, width=50)
        multiplier_label = ttk.Label(self.root, text="Multiplier:")
        multiplier_entry = ttk.Entry(self.root, width=50)

        submit_button = ttk.Button(self.root, text="Submit", command=lambda: self.submit_discount(description_entry.get(), multiplier_entry.get()))
        cancel_button = ttk.Button(self.root, text="Cancel", command=lambda: self.back(widgets))

        description_label.pack()
        description_entry.pack()
        multiplier_label.pack()
        multiplier_entry.pack()
        submit_button.pack()
        cancel_button.pack()

        widgets = [description_label, description_entry, multiplier_label, multiplier_entry, submit_button, cancel_button]
        
    def submit_discount(self, description, multiplier):
        
        try:
            multiplier = float(multiplier)
            print(multiplier)
        except ValueError:
            messagebox.showerror("Error", "Multiplier must be a number")
            return

        if not validate_description(description):
            messagebox.showerror("Error", "Description Too Short/Invalid")
            return
        else:
            Discount.createDiscount(description,multiplier)
    
    def viewDiscounts(self,widgets,operation):
        
        descriptions = []
                
        discounts = []
        
        getDescription = Discount.get_description()
        for x in getDescription:
            descriptions.append(x[0])
      
            
        for description in descriptions:
            multiplier = Discount.get_multiplier(description)
            discounts.append([description,multiplier[0]])
        
        for x in widgets:
            x.pack_forget()
            
        table = ttk.Treeview(self.root,columns=('description', 'multiplier'), show='headings')
        table.heading('description', text = "Description")
        table.heading('multiplier', text = "Multiplier")
        
        table.pack(fill='both',expand=TRUE)   
        
        if operation == "view":
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToDiscounts(widgets),width=20)
            back_button.pack()
            widgets = [table, back_button]
            
        elif operation == "update":
            update_button = ttk.Button(self.root,text="Update",command=lambda:self.updateDiscounts(widgets,table))
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToDiscounts(widgets))
    
            update_button.pack()
            back_button.pack()
            widgets = [table, update_button, back_button]
            
        elif operation == "delete":
            delete_button = ttk.Button(self.root,text="Delete",command=lambda:self.deleteDiscounts(widgets,table))  
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToDiscounts(widgets)) 
            
            delete_button.pack()
            back_button.pack()
            widgets = [table, delete_button, back_button]  
                    
                     
        viewDiscount = discounts
        
        for x in viewDiscount:
            description =  x[0]
            multipler = x[1][0]
            data = (description,multipler)
            table.insert(parent = '', index=0, values= data)
    
    
    def updateDiscounts(self,widgets):
        pass
    
    def deleteDiscount(self, widgets):
        
        selected_discounts = self.retrieve_selected_discounts()

        if not selected_discounts:
            messagebox.showinfo("Information", "No discounts selected.")
            return

        Discountinfo = []
        for discount in selected_discounts:
            if discount.get('description') and discount.get('multiplier'):
                Discountinfo.append((discount['description'], discount['multiplier']))
                yes_no = messagebox.askyesno("Delete Discount?", f"Are you sure you want to delete: {discount['description']}")

                if yes_no:
                    self.perform_discount_deletion(discount)
                    
        messagebox.showinfo("Deletion Complete", "Discount(s) deleted successfully.")
        self.viewDiscounts(widgets,"delete")
    
    def goBackToDiscounts(self, widgets):
        for x in widgets:
            x.pack_forget()
        Discounts(self.credentials,self.branch,self.root)

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
            

