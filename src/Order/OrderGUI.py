from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from Order.OrderSQL import OrderSQL

class OrderGUI:
    
    def __init__(self, credentials, branch, root):
        
        #Attributes:
        self.credentials = credentials
        self.branch = branch
        self.root = root
        self.tableOrder = ttk.Treeview(root,columns=('Item', 'Price'),show='headings')
        self.orderInfo = [] 
        self.replacementOrder = []
        self.food_item = NONE
        self.price = NONE
        self.orderStatus = NONE
        self.paymentStatus = NONE
        self.table_number = NONE
        self.order_number = NONE
        order_label = ttk.Label(root,text="Order",font=("Arial", 28))
        order_label.pack()
        self.add_items_widgets = []
        self.replace_items_widgets = []
        self.table_number_label = ttk.Label(root, text = "Table No:")
        self.table_number_entry = ttk.Entry(root)
        self.confirm_button = ttk.Button(root,text="Confirm Order",command=lambda:self.confirmOrder(self.table_number_entry,self.add_items_widgets,"place",NONE),width=25)                
        self.foodItemsInCategoryTable = ttk.Treeview(self.root,columns=('food_item', 'price', 'category', 'description', 'diet'), show='headings')
        self.ordersTable = ttk.Treeview(self.root,columns=("food_item", "price", "staff_username", "order_status", "payment_status", "table_number","order_number"), show='headings')

        #Order Management Page:
        place_order_button = ttk.Button(root,text="Place Order",command=lambda: self.placeOrder(widgets),width=50)
        view_order_button = ttk.Button(root,text="View Orders",command=lambda: self.viewOrders(widgets,"view"),width=50)
        update_order_button = ttk.Button(root,text="Update Order",command=lambda: self.viewOrders(widgets,"update"),width=50)
        cancel_order_button = ttk.Button(root,text="Cancel Order",command=lambda: self.viewOrders(widgets,"cancel"),width=50)
 
        place_order_button.pack()
        view_order_button.pack()
        update_order_button.pack()
        cancel_order_button.pack()

        back_button = ttk.Button(root,text="Back",command=lambda : self.back(widgets,credentials,branch,root),width=50) 
        back_button.pack()
        
        widgets = [order_label,back_button, place_order_button, view_order_button,update_order_button, cancel_order_button]
        
        
    #Place Table Order:
    def placeOrder(self,widgets):
        for x in widgets:
            x.pack_forget()
            
        self.table_number_label.forget()
        self.table_number_entry.forget()
        
        place_order_label = ttk.Label(self.root,text="Place Order",font=("Arial", 28))
        place_order_label.pack()
        
        food_categories_button = ttk.Button(self.root,text="View Food Categories",command=lambda:self.foodCategories(widgets,"place"),width=50)
        food_categories_button.pack()
        
        back_button = ttk.Button(self.root,text="Back",command=lambda : self.backToOrderPage(widgets),width=50) 
        back_button.pack(side=BOTTOM)
        
        widgets =[place_order_label,food_categories_button,back_button]
    
    
    #View Table Orders:
    def viewOrders(self,widgets,operation):
        for x in widgets:
            x.pack_forget()
            
        for x in self.ordersTable.get_children():
            self.ordersTable.delete(x)
            
        view_orders = OrderSQL.getOrders(self.branch)
        
        table_orders_label = ttk.Label(self.root,text="Table Orders",font=("Arial",28))
        table_orders_label.pack()
            
        self.ordersTable.heading("food_item", text = "Food Item")
        self.ordersTable.heading("price", text = "Price")
        self.ordersTable.heading("staff_username", text = "Staff Username")
        self.ordersTable.heading("order_status", text = "Order Status")
        self.ordersTable.heading("payment_status", text = "Payment Status")
        self.ordersTable.heading("table_number", text = "Table No.")
        self.ordersTable.heading("order_number", text = "Order No.")
        self.ordersTable.pack(fill='both', expand=TRUE)
        
        for x in view_orders:
            food_item = x[0]
            price = x[1]
            staff_username = x[2]
            order_status = x[3]
            payment_status = x[4]
            table_number = x[5]
            order_number = x[6]
            data = (food_item, price, staff_username, order_status, payment_status, table_number, order_number)
            self.ordersTable.insert(parent = '', index=0, values=data)
            
        if operation == "view":
            view_orders_back_button = ttk.Button(self.root,text="Back",command=lambda:self.backToOrderPage(widgets))
            view_orders_back_button.pack()
            widgets = [view_orders_back_button, self.ordersTable,table_orders_label]
            
        elif operation == "update":
            update_order_button = ttk.Button(self.root,text="Update Order",command=lambda:self.updateOrder(widgets))
            update_order_button.pack()
            view_orders_back_button = ttk.Button(self.root,text="Back",command=lambda:self.backToOrderPage(widgets))
            view_orders_back_button.pack()
            widgets = [view_orders_back_button, update_order_button,table_orders_label,self.ordersTable]
            
        elif operation == "cancel":
            cancel_order_button = ttk.Button(self.root,text="Cancel Order",command=lambda:self.cancelOrder(widgets))
            cancel_order_button.pack()
            view_orders_back_button = ttk.Button(self.root,text="Back",command=lambda:self.backToOrderPage(widgets))
            view_orders_back_button.pack()
            widgets = [view_orders_back_button, self.ordersTable, cancel_order_button,table_orders_label]
    
    
    #Update Table Order:
    def updateOrder(self, widgets):
        for i in self.ordersTable.selection():
            a = tuple((self.ordersTable.item(i)['values']))
        if a[0] != " ":
            for item in self.tableOrder.get_children():
                self.tableOrder.delete(item)
            self.orderInfo.clear()
            self.orderInfo.append(self.ordersTable.item(i)['values'])
            #Asks for confirmation for the selected order to be changed:
            yes_no = messagebox.askyesno("Change Order?", "Are You Sure You Want To Change This Order?")           
            if yes_no:
                for x in widgets:
                    x.pack_forget()          
                self.foodCategories(widgets,"update")
                self.tableOrder.heading('Item', text='Food Item')
                self.tableOrder.heading('Price', text='Price')
                self.tableOrder.pack(side=BOTTOM)
                self.food_item = self.orderInfo[0][0]
                self.price = self.orderInfo[0][1]
                self.tableOrder.insert('', 'end', values=(self.food_item, self.price))
                                 
    
    #Cancel Table Order:
    def cancelOrder(self, widgets):
        for i in self.ordersTable.selection():
            a = tuple((self.ordersTable.item(i)['values']))
            if a[0] != " ":
                self.orderInfo.clear()
                self.orderInfo.append(self.ordersTable.item(i)['values'])
                #Asks for confirmation for the selected order to be cancelled:
                yes_no = messagebox.askyesno("Cancel Order?", "Are You Sure You Want To Cancel This Order?")           
                if yes_no:
                        OrderSQL.cancelOrder(self.orderInfo,self.branch)
                        messagebox.showinfo("Order Cancelled", "Order Successfully Removed")
                        self.viewOrders(widgets,"cancel")
    
    #Add Items To Basket:
    def add(self,foodItemsInCategoryTable):
        for i in foodItemsInCategoryTable.selection():
            a = tuple((foodItemsInCategoryTable.item(i)['values']))
            if a[0] != " ":
                selectedItem = foodItemsInCategoryTable.selection()
                for item in selectedItem:
                    food_item = foodItemsInCategoryTable.item(item, 'values')[0]
                    price = foodItemsInCategoryTable.item(item, 'values')[1]
                self.table_number_entry.pack(side=BOTTOM)
                self.table_number_label.pack(side=BOTTOM)
                self.confirm_button.pack(side=BOTTOM)
                self.tableOrder.insert('', 'end', values=(food_item, price))
        
    def check_empty_basket(self,back_button,add_button,widgets):
        food = []
        for item in self.tableOrder.get_children():
            food.append(self.tableOrder.item(item)['values'][0])
        if len(food) == 0:
            self.tableOrder.pack_forget()
            self.confirm_button.pack_forget()
            self.table_number_entry.pack_forget()
            self.table_number_label.pack_forget()
        for x in widgets:
            x.forget()
        back_button.forget()
        add_button.forget()
        
        
    #Remove Food Item From Basket
    def removeFromBasket(self):
        
        for i in self.tableOrder.selection():
            a = tuple((self.tableOrder.item(i)['values']))
            if a[0] != " ":
                item = self.tableOrder.selection()
                remove = messagebox.askyesno("Remove Item?", "Are You Sure You Want To Remove This Item?")
                if remove:
                    self.tableOrder.delete(item)
       
     
    #Replaces one item from a table order:
    def replaceItem(self,widgets,foodItemsInCategoryTable):
        selectedItem = foodItemsInCategoryTable.selection()
        for i in selectedItem:
            replacementOrder = []
            a = tuple((foodItemsInCategoryTable.item(i)['values']))
            if a[0] != " ":
                replacementOrder.append(foodItemsInCategoryTable.item(i)['values'])
                #Asks for confirmation for the selected order to be cancelled:
                yes_no = messagebox.askyesno("Replace Item?", "Are You Sure You Want To Replace This Item?")           
                if yes_no:
                    for row in self.tableOrder.get_children():
                        self.tableOrder.delete(row)
                    for item in selectedItem:
                        self.food_item = foodItemsInCategoryTable.item(item, 'values')[0]
                        self.price = foodItemsInCategoryTable.item(item, 'values')[1]
                        self.tableOrder.insert('', 'end', values=(self.food_item, self.price))   
                    
                    #Gets username of staff that is making the change to the order
                    self.staff = self.credentials[1]
                    
                    #Leaves the rest of the information about the order unchanged
                    self.orderStatus = self.orderInfo[0][3]
                    self.paymentStatus = self.orderInfo[0][4]
                    self.table_number = self.orderInfo[0][5]    
                    self.order_number = self.orderInfo[0][6] 
                    newOrder = [self.food_item,self.price,self.staff,self.orderStatus,self.paymentStatus,self.table_number,self.order_number]
                    confirm_button = ttk.Button(self.root,text="Confirm Changes",command=lambda:self.confirmOrder(self.table_number,widgets,"update",newOrder))
                    confirm_button.pack()
                    self.replace_items_widgets.append(confirm_button)
                    widgets.append(confirm_button)
    
    
    #Confirm Table Order
    def confirmOrder(self, table_number_entry,widgets,operation,newOrder):
        #Sends a placed order to database:
        if operation == "place":
                if table_number_entry.get() == "":
                            messagebox.showerror("Error", "Please Enter Table Number")
                else:
                    confirm_order = messagebox.askyesno("Confirm Order","Confirm Order?")
                    if confirm_order :
                                                
                            for item in self.tableOrder.get_children():
                                food_item = self.tableOrder.item(item,'values')[0]
                                price = self.tableOrder.item(item, 'values')[1]
                                staff = self.credentials[1]
                                order_status = "PENDING"
                                payment_status = "PENDING"
                                table_number = table_number_entry.get()
                                order = [food_item,price,staff,order_status,payment_status,table_number]
                            
                                OrderSQL.addOrder(order, self.branch)
                                messagebox.showinfo("Order Added", "Order Successfully Added")
                                self.orderInfo.clear()
                                for x in widgets:
                                    x.pack_forget()
                                self.tableOrder.pack_forget()
                                self.table_number_entry.pack_forget()
                                self.table_number_label.pack_forget()
                                self.confirm_button.pack_forget()
                                self.foodItemsInCategoryTable.pack_forget()
                                self.backToOrderPage(self.add_items_widgets)

        #Commits updates to an existing order:
        elif operation == "update":
                for item in self.tableOrder.get_children():
                    food_item = newOrder[0]
                    price = newOrder[1]
                    staff = newOrder[2]
                    order_status = "PENDING"
                    payment_status = "PENDING"
                    table_number = self.table_number
                    order_number = self.order_number
                    order = [food_item,price,staff,order_status,payment_status,table_number,order_number]
                    
                    OrderSQL.updateOrder(order, self.branch)
                    messagebox.showinfo("Order Updated", "Order Successfully Changed")
                    self.replacementOrder.clear()
                    self.orderInfo.clear()
                    for x in self.replace_items_widgets:
                        x.pack_forget()
                    self.viewOrders(self.add_items_widgets,"update")
                
                
    #View Food Items In Food Category
    def foodItems(self,widgets,foodCategoriesTable,operation):       
        
        #Gathers items from selected food category:
        for i in foodCategoriesTable.selection():
            a = tuple((foodCategoriesTable.item(i)['values']))
            if a[0] != " ":
                category = a
                items = OrderSQL.get_food_items(self.branch,category)
                
                for x in widgets:
                    x.pack_forget() 
                                
                food_items_label = ttk.Label(self.root,text="Food Items",font=("Arial",28))
                food_items_label.pack(side=TOP)
            
                self.foodItemsInCategoryTable.heading('food_item', text="Food Item")
                self.foodItemsInCategoryTable.heading('price', text="Price") 
                self.foodItemsInCategoryTable.heading('category', text="Category")
                self.foodItemsInCategoryTable.heading('description', text="Description")
                self.foodItemsInCategoryTable.heading('diet', text="Diet")
            
                self.foodItemsInCategoryTable.pack(fill='both',expand=TRUE,side=TOP)
                                
                if (operation == "place"):
                    add_to_basket_button = ttk.Button(self.root,text="Add To Basket",command=lambda:self.add(self.foodItemsInCategoryTable))
                    add_to_basket_button.pack()
                    remove_item_button = ttk.Button(self.root,text="Remove Item From Basket",command=lambda:self.removeFromBasket())
                    remove_item_button.pack()
                    
                    back_button= ttk.Button(self.root,text="Back",command=lambda:[self.check_empty_basket(back_button,add_to_basket_button,widgets), clearItems(),self.foodCategories(widgets,operation)],width=40)
                    back_button.pack(side=BOTTOM)
                    
                    #Treeview For Table Order 
                    self.tableOrder.heading('Item', text='Food Item')
                    self.tableOrder.heading('Price', text='Price')
                    self.tableOrder.pack(side=BOTTOM)
                    
                    self.add_items_widgets = [self.foodItemsInCategoryTable,back_button,add_to_basket_button,food_items_label,remove_item_button]
                    
                elif operation == "update":
                    for x in self.foodItemsInCategoryTable.get_children():
                        self.foodItemsInCategoryTable.delete(x)
                    replace_item_button = ttk.Button(self.root,text="Replace",command=lambda:self.replaceItem(widgets,self.foodItemsInCategoryTable))
                    replace_item_button.pack()
                    back_button= ttk.Button(self.root,text="Back",command=lambda:self.foodCategories(widgets,operation))
                    back_button.pack(side=BOTTOM)
                    
                    widgets = [self.foodItemsInCategoryTable,back_button,replace_item_button,food_items_label]
                    
                    self.replace_items_widgets = [replace_item_button,self.foodItemsInCategoryTable,self.confirm_button,back_button,self.tableOrder,food_items_label]
                             
                #Inserts gathered food items from selected category into the food items table 
                for x in items:
                    food_item = x[0]
                    price = x[1]
                    category = x[2]
                    description = x[3]
                    diet = x[4]
                    data = (food_item,price,category,description,diet)
                    self.foodItemsInCategoryTable.insert(parent = '', index=0, values=data)
                    
        #Clears items in the food items category table:
        def clearItems():
            for item in self.foodItemsInCategoryTable.get_children():            
                self.foodItemsInCategoryTable.delete(item)
            self.foodItemsInCategoryTable.pack_forget()
            food_items_label.pack_forget()
            remove_item_button.pack_forget()
                               
                            
    #View Food Categories
    def foodCategories(self,widgets,operation):
        for x in widgets:
            x.pack_forget()
        view_food_categories = OrderSQL.get_food_categories(self.branch)
        
        food_categories_label = ttk.Label(self.root,text="Food Categories",font=("Arial",28))
        food_categories_label.pack(side=TOP)
        
        #Creates the table containing the list of food categories:
        foodCategoriesTable = ttk.Treeview(self.root,columns=('categories', ), show='headings')
        foodCategoriesTable.heading('categories', text = "Food Categories")
    
        foodCategoriesTable.pack(fill='both',expand=TRUE,side=TOP)   
        
        for x in view_food_categories:
            foodCategoriesTable.insert(parent = '', index=0, values= x)
        
        if operation == "place":
            view_items_button = ttk.Button(self.root,text="View Items",command=lambda:self.foodItems(widgets,foodCategoriesTable,"place"),width=40)
            view_items_button.pack()
            back_button = ttk.Button(self.root,text="Back",command=lambda:[items_left_in_basket()],width=40)
            back_button.pack(side=BOTTOM)
            widgets = [foodCategoriesTable, view_items_button,back_button,food_categories_label]
            
        elif operation == "update":
            view_items_button = ttk.Button(self.root,text="View Items",command=lambda:self.foodItems(widgets,foodCategoriesTable,"update"),width=40)
            view_items_button.pack()
            back_button = ttk.Button(self.root,text="Back",command=lambda:[self.tableOrder.pack_forget(), self.viewOrders(widgets,"update")])
            back_button.pack()
            widgets = [foodCategoriesTable, view_items_button,back_button,food_categories_label]

        #Checks if there are any items remaining inside the basket, if the user chooses to no longer place an order:
        def items_left_in_basket():
            food = []
            for item in self.tableOrder.get_children():
                food.append(self.tableOrder.item(item)['values'][0])
            if len(food) == 0:
                self.placeOrder(widgets)
                self.tableOrder.forget()
                self.confirm_button.pack_forget()
            else:
                itemsRemaining = messagebox.askyesno("Items Remaining In Basket","Are You Sure You Want To Exit?")
                if itemsRemaining:
                    for item in self.tableOrder.get_children():
                        self.tableOrder.delete(item)
                    self.placeOrder(widgets)
                    self.tableOrder.forget()
                    self.confirm_button.pack_forget()
                else:
                    pass
                    
        
    #Return To Order Page
    def backToOrderPage(self,widgets):
        for x in widgets:
            x.pack_forget()
        OrderGUI(self.credentials,self.branch,self.root)
        

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
