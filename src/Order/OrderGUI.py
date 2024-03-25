from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from Order.OrderSQL import OrderSQL

class OrderGUI:
    
    def __init__(self, credentials, branch, root):
        self.tableOrder = None #An order sheet for a particular table
        
        order_label = ttk.Label(root,text="Order",font=("Arial", 28))
        order_label.pack()
        
        place_order_button = ttk.Button(root,text="Place Order",command=lambda: self.placeOrder(widgets,credentials, branch, root),width=50)
        view_order_button = ttk.Button(root,text="View Orders",command=lambda: self.viewOrders(widgets, credentials, branch, root,"view"),width=50)
        update_order_button = ttk.Button(root,text="Update Order",command=lambda: self.viewOrders(widgets,credentials,branch, root,"update"),width=50)
        cancel_order_button = ttk.Button(root,text="Cancel Order",command=lambda: self.viewOrders(widgets,credentials,branch, root,"cancel"),width=50)
 
        place_order_button.pack()
        view_order_button.pack()
        update_order_button.pack()
        cancel_order_button.pack()

        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,root),width=50) 
        back_button.pack()
        
        widgets = [order_label,back_button, place_order_button, view_order_button,update_order_button, cancel_order_button]
        
    #Place Table Order
    def placeOrder(self,widgets, credentials, branch, root):
        for x in widgets:
            x.pack_forget()
        
        place_order_label = ttk.Label(root,text="Place Order",font=("Arial", 28))
        place_order_label.pack()
        
        food_categories_button = ttk.Button(root,text="View Food Categories",command=lambda:self.foodCategories(widgets,credentials,branch,root),width=50)
        food_categories_button.pack()
        
        back_button = ttk.Button(root,text="Back",command=lambda : self.backToOrderPage(widgets,credentials,branch,root),width=50) 
        back_button.pack(side=BOTTOM)
        
        widgets =[place_order_label,food_categories_button,back_button]
    
    
    #View Table Orders
    def viewOrders(self,widgets,credentials,branch,root,operation):
        for x in widgets:
            x.pack_forget()
            
        view_orders = OrderSQL.getOrders(branch)
            
        table = ttk.Treeview(root,columns=("food_item", "price", "staff_username", "order_status", "payment_status", "table_number","order_number"), show='headings')
        table.heading("food_item", text = "Food Item")
        table.heading("price", text = "Price")
        table.heading("staff_username", text = "Staff Username")
        table.heading("order_status", text = "Order Status")
        table.heading("payment_status", text = "Payment Status")
        table.heading("table_number", text = "Table No.")
        table.heading("order_number", text = "Order No.")
        table.pack(fill='both', expand=TRUE)
        
        for x in view_orders:
            food_item = x[0]
            price = x[1]
            staff_username = x[2]
            order_status = x[3]
            payment_status = x[4]
            table_number = x[5]
            order_number = x[6]
            data = (food_item, price, staff_username, order_status, payment_status, table_number, order_number)
            table.insert(parent = '', index=0, values=data)
            
        if operation == "view":
            back_button = ttk.Button(root,text="Back",command=lambda:self.backToOrderPage(widgets,credentials,branch,root))
            back_button.pack()
            widgets = [back_button, table]
            
        elif operation == "update":
            update_order_button = ttk.Button(root,text="Update Order",command=lambda:self.updateOrder(widgets,credentials,branch, root, table))
            update_order_button.pack()
            back_button = ttk.Button(root,text="Back",command=lambda:self.backToOrderPage(widgets,credentials,branch,root))
            back_button.pack()
            widgets = [back_button, table, update_order_button]
            
        elif operation == "cancel":
            cancel_order_button = ttk.Button(root,text="Cancel Order",command=lambda:self.cancelOrder(widgets,credentials,branch, root, table))
            cancel_order_button.pack()
            back_button = ttk.Button(root,text="Back",command=lambda:self.backToOrderPage(widgets,credentials,branch,root))
            back_button.pack()
            widgets = [back_button, table, cancel_order_button]
    
    #Update Table Order
    def updateOrder(self, widgets,credentials,branch, root, table):
        orderInfo = []
        for i in table.selection():
            a = tuple((table.item(i)['values']))
            if a[0] != " ":
                orderInfo.append(table.item(i)['values'])
                #Asks for confirmation for the selected order to be changed:
                yes_no = messagebox.askyesno("Change Order?", "Are You Sure You Want To Change This Order?")           
                if yes_no:
                    food_item = orderInfo[0][0]
                    price = orderInfo[0][1]
                    if self.tableOrder == None:
                        self.tableOrder = ttk.Treeview(root,columns=('Item', 'Price'),show='headings')
                        self.tableOrder.heading('Item', text='Food Item')
                        self.tableOrder.heading('Price', text='Price')
                        self.tableOrder.pack(side=BOTTOM)
                        self.tableOrder.insert('', 'end', values=(food_item, price))
                        
    
    #Cancel Table Order
    def cancelOrder(self, widgets,credentials,branch, root, table):
        orderInfo = []
        for i in table.selection():
            a = tuple((table.item(i)['values']))
            if a[0] != " ":
                orderInfo.append(table.item(i)['values'])
                #Asks for confirmation for the selected order to be cancelled:
                yes_no = messagebox.askyesno("Cancel Order?", "Are You Sure You Want To Cancel This Order?")           
                if yes_no:
                        OrderSQL.cancelOrder(orderInfo,branch)
                        messagebox.showinfo("Order Cancelled", "Order Successfully Removed")
                        self.viewOrders(widgets,credentials,branch,root,"cancel")
    
       
    #Add Food Item To Basket
    def addToBasket(self, root, foodItemsInCategoryTable, credentials, branch):
        selecteditem = foodItemsInCategoryTable.selection()
        if self.tableOrder == None:
            self.tableOrder = ttk.Treeview(root,columns=('Item', 'Price'),show='headings')
            self.tableOrder.heading('Item', text='Food Item')
            self.tableOrder.heading('Price', text='Price')
            self.tableOrder.pack(side=BOTTOM)
                
            table_number_label = ttk.Label(root, text = "Table No:")
            table_number_label.pack()
            table_number_entry = ttk.Entry()
            table_number_entry.pack(side=BOTTOM)
            
            confirm_button = ttk.Button(root,text="Confirm Order",command=lambda:self.confirmOrder(table_number_entry,basket,credentials,branch,root),width=25)
            confirm_button.pack(side=BOTTOM)
            
            remove_item_button = ttk.Button(root,text="Remove Item From Basket",command=lambda:self.removeFromBasket())
            remove_item_button.pack(side=BOTTOM)
            
            basket = [self.tableOrder,table_number_entry,table_number_label,confirm_button,remove_item_button]
                        
        for item in selecteditem:
            food_item = foodItemsInCategoryTable.item(item, 'values')[0]
            price = foodItemsInCategoryTable.item(item, 'values')[1]
        self.tableOrder.insert('', 'end', values=(food_item, price))

    #Remove Food Item From Basket
    def removeFromBasket(self):
        item = self.tableOrder.selection()
        remove = messagebox.askyesno("Remove Item?", "Are You Sure You Want To Remove This Item?")
        if remove:
            self.tableOrder.delete(item)
    
    #Confirm Table Order
    def confirmOrder(self, table_number_entry,basket,credentials,branch,root):
        confirm_order = messagebox.askyesno("Confirm Order","Confirm Order?")
        if confirm_order:
            for item in self.tableOrder.get_children():
                food_item = self.tableOrder.item(item,'values')[0]
                price = self.tableOrder.item(item, 'values')[1]
                staff = credentials[1]
                order_status = "PENDING"
                payment_status = "PENDING"
                table_number = table_number_entry.get()
                order = [food_item,price,staff,order_status,payment_status,table_number]
                OrderSQL.addOrder(order, branch)
                messagebox.showinfo("Order Added", "Order Successfully Added")
                for x in basket:
                    x.pack_forget()
                OrderGUI(credentials,branch,root)
                
    #View Food Items In Food Category
    def foodItems(self,widgets,credentials,branch,root,table):
        for x in widgets:
            x.pack_forget()        
                
        for i in table.selection():
            a = tuple((table.item(i)['values']))
            if a[0] != " ":
                category = a
                items = OrderSQL.get_food_items(branch,category)
            
                foodItemsInCategoryTable = ttk.Treeview(root,columns=('food_item', 'price', 'category', 'description', 'diet'), show='headings')
                foodItemsInCategoryTable.heading('food_item', text="Food Item")
                foodItemsInCategoryTable.heading('price', text="Price") 
                foodItemsInCategoryTable.heading('category', text="Category")
                foodItemsInCategoryTable.heading('description', text="Description")
                foodItemsInCategoryTable.heading('diet', text="Diet")
            
                foodItemsInCategoryTable.pack(fill='both',expand=TRUE)
                add_to_basket_button = ttk.Button(root,text="Add To Basket",command=lambda:self.addToBasket(root, foodItemsInCategoryTable, credentials, branch))
                add_to_basket_button.pack()
                back_button= ttk.Button(root,text="Back",command=lambda:self.foodCategories(widgets, credentials,branch,root))
                back_button.pack(side=BOTTOM)
                widgets = [foodItemsInCategoryTable,back_button,add_to_basket_button]
                
                for x in items:
                    food_item = x[0]
                    price = x[1]
                    category = x[2]
                    description = x[3]
                    diet = x[4]
                    data = (food_item,price,category,description,diet)
                    foodItemsInCategoryTable.insert(parent = '', index=0, values=data)    
                    
                            
    #View Food Categories
    def foodCategories(self,widgets,credentials,branch,root):
        for x in widgets:
            x.pack_forget()
            
        view_food_categories = OrderSQL.get_food_categories(branch)
        
        #Creates the table containing the list of food categories:
        foodCategoriesTable = ttk.Treeview(root,columns=('categories', ), show='headings')
        foodCategoriesTable.heading('categories', text = "Food Categories")
    
        foodCategoriesTable.pack(fill='both',expand=TRUE)   
        
        view_items_button = ttk.Button(root,text="View Items",command=lambda:self.foodItems(widgets,credentials,branch,root,foodCategoriesTable),width=40)
        view_items_button.pack()
        
        back_button = ttk.Button(root,text="Back",command=lambda:self.placeOrder(widgets,credentials,branch,root))
        back_button.pack()
        
        widgets = [foodCategoriesTable, view_items_button,back_button]

        for x in view_food_categories:
            foodCategoriesTable.insert(parent = '', index=0, values= x)


    #Return To Order Page
    def backToOrderPage(self,widgets,credentials, branch,root):
        for x in widgets:
            x.pack_forget()
        OrderGUI(credentials,branch,root)
        

    #GO BACK TO USER HOME PAGE
    #Allows the user to go back to their home page
    def back(self,widgets,credentials, branch,root):
        if credentials[3] == "Admin":
            from AdminGUI.AdminGUI import ADMIN
            ADMIN(widgets,credentials, branch,root) 
        elif credentials[3] == "Manager":
            from ManagerGUI.ManagerGUI import MANAGER
            MANAGER(widgets,credentials,branch,root)
        elif credentials[3] == "Staff":
            from StaffGUI.StaffGUI import STAFF
            STAFF(widgets,credentials,branch,root)