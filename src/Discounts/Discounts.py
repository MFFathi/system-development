
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
        self.table = ttk.Treeview(self.root,columns=('description', 'multiplier'), show='headings')
        
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
            
        for i in self.table.get_children():
            self.table.delete(i)
            
        self.table.heading('description', text = "Description")
        self.table.heading('multiplier', text = "Multiplier")
        
        self.table.pack(fill='both',expand=TRUE)   
        
        if operation == "view":
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToDiscounts(widgets),width=20)
            back_button.pack()
            widgets = [self.table, back_button]
            
        elif operation == "update":
            update_button = ttk.Button(self.root,text="Update",command=lambda:self.updateDiscounts(widgets))
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToDiscounts(widgets))
    
            update_button.pack()
            back_button.pack()
            widgets = [self.table, update_button, back_button]
            
        elif operation == "delete":
            delete_button = ttk.Button(self.root,text="Delete",command=lambda:self.deleteDiscount(widgets))  
            back_button = ttk.Button(self.root, text="Back",command=lambda:self.goBackToDiscounts(widgets)) 
            
            delete_button.pack()
            back_button.pack()
            widgets = [self.table, delete_button, back_button]  
                    
                     
        viewDiscount = discounts
        
        for x in viewDiscount:
            description =  x[0]
            multipler = x[1][0]
            data = (description,multipler)
            self.table.insert(parent = '', index=0, values= data)
    
    
    def updateDiscounts(self,widgets):
        
        def submit(description, multiplier):
            submit = messagebox.askyesno("Submit Changes?","Are You Sure You Want To Submit These Changes")
            if submit:
                Discount.set_multiplier(originalDescription,multiplier)
                Discount.set_description(originalDescription,description)
                messagebox.showinfo("Discount Updated","Discount Successfully Updated")
                self.viewDiscounts(widgets,"update")
        
        discountInfo = []
        for i in self.table.selection():
            a = tuple((self.table.item(i)['values']))
            if a[0] != " ":
                discountInfo.append(self.table.item(i)['values'])
                
                #Asks for confirmation for the selected user to be updated:
                yes_no = messagebox.askyesno("Update This User?", "Are You Sure You Want To Make Changes To This User?")
                if (yes_no) == False: 
                    self.viewUsers(widgets,"update")
                else:
                    for x  in widgets:
                        x.pack_forget()
                    description_label = ttk.Label(self.root, text="Description:")
                    description_entry = ttk.Entry(self.root, width=50)
                    multiplier_label = ttk.Label(self.root, text="Multiplier:")
                    multiplier_entry = ttk.Entry(self.root, width=50)

                    submit_button = ttk.Button(self.root, text="Submit", command=lambda: submit(description_entry.get(),multiplier_entry.get()))
                    cancel_button = ttk.Button(self.root, text="Cancel", command=lambda: self.back(widgets))

                    description_label.pack()
                    description_entry.pack()
                    multiplier_label.pack()
                    multiplier_entry.pack()
                    submit_button.pack()
                    cancel_button.pack()
                    
                    originalDescription = discountInfo[0][0]
                    description_entry.insert(0, discountInfo[0][0])
                    multiplier_entry.insert(0,discountInfo[0][1])
                    
                    widgets = [description_label, description_entry, multiplier_label, multiplier_entry, submit_button, cancel_button]
                        
                        
    
    def deleteDiscount(self, widgets):

        discountInfo = []
        for i in self.table.selection():
            a = tuple((self.table.item(i)['values']))
            if a[0] != " ":
                discountInfo.append(self.table.item(i)['values'])
                
                #Asks for confirmation for the selected user to be updated:
                yes_no = messagebox.askyesno("Delete This Discount?", "Are You Sure You Want To Delete This Discount?")
                if (yes_no): 
                    description = discountInfo[0][0]
                    multiplier = discountInfo[0][1]
                    Discount.delete(description,multiplier)
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
            

