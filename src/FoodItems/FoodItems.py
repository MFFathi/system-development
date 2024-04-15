from tkinter import *
from tkinter import ttk
from tkcalendar import *


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

class FoodItems():
    
    def __init__(self, widgets,credentials,branch,database,root):
        
        for x in widgets:
            x.pack_forget() 
        
        food_items_label = ttk.Label(root,text="Food Items",font=("Arial",28))
        create_food_item_button = ttk.Button(root,text="Create Food Item",command=lambda:self.createFoodItem(widgets,credentials,branch,database,root),width=50)
        read_food_item_button = ttk.Button(root,text="Read Food Items",command=lambda:self.readFoodItems(widgets,credentials,branch,database,root),width=50)
        update_food_item_button = ttk.Button(root,text="Update Food Item",command=lambda:self.updateFoodItem(widgets,credentials,branch,database,root),width=50)
        delete_food_item_button = ttk.Button(root,text="Delete Food Item",command=lambda:self.deleteFoodItem(widgets,credentials,branch,database,root),width=50)
        back_button = ttk.Button(root,text="Back",command=lambda:self.backToMenu(widgets,credentials,branch,database,root),width=50)
        
        
        food_items_label.pack(side=TOP)
        create_food_item_button.pack()
        read_food_item_button.pack()
        update_food_item_button.pack()
        delete_food_item_button.pack()
        back_button.pack()
        
        
        widgets = [food_items_label,
                   create_food_item_button,
                   read_food_item_button,
                   update_food_item_button,
                   delete_food_item_button,
                   back_button]
        





#CREATE FOOD ITEM:
    def createFoodItem(self,widgets,credentials,branch,database,root):
        
        for x in widgets:
                 x.pack_forget()   
                 
        food_name_entry = ttk.Entry()
        price_entry = ttk.Entry()
        category_entry = ttk.Entry()
        description_entry = ttk.Entry()
        diet_entry = ttk.Entry()
        
        
        food_name_label = ttk.Label(text="Name:")
        price_label = ttk.Label(text="Price:")
        category_label = ttk.Label(text="Category")
        description_label = ttk.Label(text="Description:")
        diet_label = ttk.Label(text="Diet:")
        
        submit_button = ttk.Button(root,text="Submit",command=lambda: submit(food_name_entry, price_entry, category_entry, description_entry, diet_entry, widgets, credentials, branch, database), width=20)        
        back_button = ttk.Button(root,text="Back",command=lambda: goBackToMenuFoodItem(widgets, credentials,branch,database),width=20)
        
        food_name_label.pack()
        food_name_entry.pack()
        
        price_label.pack()
        price_entry.pack()
        
        category_label.pack()
        category_entry.pack()
        
        
        diet_label.pack()
        diet_entry.pack()
        
        description_label.pack()
        description_entry.pack()
        submit_button.pack()
        back_button.pack()
        
               
        widgets = [food_name_label, 
                 price_label,
                 category_label,
                 description_label,
                 diet_label,
                 food_name_entry,
                 price_entry,
                 category_entry,
                 description_entry,
                 diet_entry,
                 submit_button,
                 back_button]

        def goBackToMenuFoodItem(widgets, credentials,branch,database):
            
            FoodItems(widgets,credentials,branch,database)
            
    



        def submit(food_name_entry, price_entry, category_entry, description_entry, diet_entry, widgets, credentials, branch, database):
    

                
                #Sees if submitted category exists:                
                database.execute("SELECT name FROM food_categories ORDER BY name")
                existingCategories = database.fetchall()

                validCategories = 0
                for x in existingCategories:
                    if(x[0] == category_entry.get()):
                         validCategories = validCategories + 1
                 
                if (food_name_entry.get() == "") and (price_entry.get() == "") and (category_entry.get() == "") and (description_entry.get() == "") and  (diet_entry.get() == ""):
                    incomplete_field = Tk()
                    incomplete_field.title("Error")
                    incomplete_field.geometry("275x50")
                    first_name_not_filled_label = ttk.Label(incomplete_field, text="Fields are incomplete!") 
                    close_button = ttk.Button(incomplete_field,text="close",command=lambda: incomplete_field.destroy())
                    first_name_not_filled_label.pack()
                    close_button.pack()
              
                elif food_name_entry.get() == "":
                    incomplete_field = Tk()
                    incomplete_field.title("Incomplete Field")
                    incomplete_field.geometry("275x50")
                    first_name_not_filled_label = ttk.Label(incomplete_field, text="Food Name Has Not Been Filled!") 
                    close_button = ttk.Button(incomplete_field,text="close",command=lambda: incomplete_field.destroy())
                    first_name_not_filled_label.pack()
                    close_button.pack()
                
                elif price_entry.get() == "":
                    incomplete_field = Tk()
                    incomplete_field.title("Incomplete Field!")
                    incomplete_field.geometry("275x50")
                    first_name_not_filled_label = ttk.Label(incomplete_field, text="Price Has Not Been Filled!") 
                    close_button = ttk.Button(incomplete_field,text="close",command=lambda: incomplete_field.destroy())
                    first_name_not_filled_label.pack()
                    close_button.pack()        
        
                elif category_entry.get() == "":
                    incomplete_field = Tk()
                    incomplete_field.title("Incomplete Field!")
                    incomplete_field.geometry("275x50")
                    first_name_not_filled_label = ttk.Label(incomplete_field, text="Category Has Not Been Filled!") 
                    close_button = ttk.Button(incomplete_field,text="close",command=lambda: incomplete_field.destroy())
                    first_name_not_filled_label.pack()
                    close_button.pack()
                    
                elif (validCategories != 1):
                    incomplete_field = Tk()
                    incomplete_field.title("Invalid Category")
                    incomplete_field.geometry("275x50")
                    category_not_filled_label = ttk.Label(incomplete_field, text="Category Does Not Exist!") 
                    categories_must_be_label = ttk.Label(incomplete_field,text="Categories Must Be One Of:")
                    close_button = ttk.Button(incomplete_field,text="close",command=lambda: incomplete_field.destroy())
                    category_not_filled_label.pack()
                    categories_must_be_label.pack()
                    for x in existingCategories:
                        must_be_label = ttk.Label(incomplete_field,text=x) 
                        must_be_label.pack()
                    close_button.pack()
        
                elif description_entry.get() == "":
                    incomplete_field = Tk()
                    incomplete_field.title("Incomplete Field!")
                    incomplete_field.geometry("275x50")
                    first_name_not_filled_label = ttk.Label(incomplete_field, text="Description Has Not Been Filled!") 
                    close_button = ttk.Button(incomplete_field,text="close",command=lambda: incomplete_field.destroy())
                    first_name_not_filled_label.pack()
                    close_button.pack()
                    
                elif diet_entry.get() == "":
                    incomplete_field = Tk()
                    incomplete_field.title("Incomplete Field!")
                    incomplete_field.geometry("275x50")
                    first_name_not_filled_label = ttk.Label(incomplete_field, text="Diet Has Not Been Filled!") 
                    close_button = ttk.Button(incomplete_field,text="close",command=lambda: incomplete_field.destroy())
                    first_name_not_filled_label.pack()
                    close_button.pack()
        
           
        
                else:

                    pass



                    
                
                    food_name = food_name_entry.get()
                    price = price_entry.get()
                    category = category_entry.get()
                    description = description_entry.get()
                    diet = diet_entry.get()
           
                        
                    sql = "SELECT * FROM food_items WHERE name = %s"
                    name = (food_name,)
                    database.execute(sql,name)
                    results = database.fetchall()
            
                    existentItem = FALSE
                    #Checks to see if a food item already exists:
                    for x in results:
                        #If the submitted food item is not new then it will not be added and a pop window will notify the user:
                        if x[0] == food_name:
                                exists = Tk()
                                exists.title("Food Item Already Exists")
                                existent_item_label = ttk.Label(exists,text="This Food Item Already Exists")
                                ok = ttk.Button(exists,text="Ok",command=lambda:exists.destroy())
                                existent_item_label.pack()
                                ok.pack()
                                existentItem = TRUE
                     
                    #If the submitted item is new then it will be added: 
                    if existentItem == FALSE:   
                        
                        sql = "INSERT INTO food_items (name, price, category, description, diet) VALUES (%s, %s, %s, %s, %s)"
                        val = (food_name,
                               price,
                               category,
                               description,
                               diet
                               )       
                        database.execute(sql,val)
                        
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

                        complete = Tk()
                        complete.title("Food Item Created")
                        complete.geometry("275x50")
                        account_creation_successful_label = ttk.Label(complete, text="Food Item Successfully Created") 
                        close_button = ttk.Button(complete,text="ok",command=lambda: complete.destroy())
                        account_creation_successful_label.pack()
                        close_button.pack()
                        for x in widgets:
                             x.pack_forget()
                        FoodItems(widgets,credentials, branch,database)
                        




















    
    def readFoodItems(self,widgets,credentials,branch,database,root):
        database.execute("SELECT name, price, category, description, diet FROM food_items ORDER BY name DESC")
        viewItemsList = database.fetchall()    
        for x in widgets:
            x.pack_forget() 
        
        #Creates the table containing the list of food items for the system:
        table = ttk.Treeview(root,columns=('food_name', 'price', 'category', 'description', 'diet'), show='headings')
        table.heading('food_name', text = "Food Name")
        table.heading('price', text = "Price")
        table.heading('category', text = "Category")
        table.heading('description', text = "Description")
        table.heading('diet', text = "Diet")
        
        table.pack(fill='both',expand=TRUE)   
        back_button=ttk.Button(root,text="Back",command=lambda:FoodItems(widgets,credentials,branch,database))
        back_button.pack()
        widgets = [table,
                   back_button]
    
        #Searches through the individual information about each item from the items list:
        for x in viewItemsList:
            food_name=  x[0]
            price = x[1]
            category = x[2]
            description = x[3] 
            diet = x[4]
            data = (food_name,price,category,description,diet)
            table.insert(parent = '', index=0, values= data)

















    




#UPDATE FOOD ITEM:
    def updateFoodItem(self,widgets,credentials,branch,database,root):
         
         def submitChanges(row_id,food_name_entry, price_entry, category_entry, description_entry, diet_entry,widgets,database):
            foodName = food_name_entry.get()
            price = price_entry.get()
            category = category_entry.get()
            description = description_entry.get()
            diet = diet_entry.get()
            
            
            foodNameSQL = "UPDATE food_items SET name = %s WHERE id = %s"
            val = (foodName,row_id)
            database.execute(foodNameSQL,val)
            
            priceSQL = "UPDATE food_items SET price = %s WHERE id = %s"
            val = (price,row_id)
            database.execute(priceSQL,val)
            
            categorySQL = "UPDATE food_items SET category = %s WHERE id = %s"
            val = (category,row_id)
            database.execute(categorySQL,val)
            
            descriptionSQL = "UPDATE food_items SET description = %s WHERE id = %s"
            val = (description,row_id)
            database.execute(descriptionSQL,val)
            
            dietSQL = "UPDATE food_items SET diet = %s WHERE id = %s"
            val = (diet,row_id)
            
            database.execute(dietSQL,val)
            
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
            
            changesMade = Tk()
            changesMade.title("Food Item Updated")
            user_has_been_updated_label = ttk.Label(changesMade,text="Food Item Has Been Updated")
            ok_button = ttk.Button(changesMade,text="Ok", command=lambda:[destroyWidgets(widgets),FoodItems(widgets,credentials,branch,database),changesMade.destroy(),destroyWidgets(widgets)])
            user_has_been_updated_label.pack()
            ok_button.pack()


        
         def update_selected_item(widgets,credentials):
            for x in widgets:
                x.pack_forget() 
                
            itemInfo = []
            for i in table.selection():
                    #print(table.item(i)['values']) 
                    #print("Delete!")
                    itemInfo.append(table.item(i)['values'])
                    
            food_name_entry = ttk.Entry()
            price_entry = ttk.Entry()
            category_entry = ttk.Entry()
            description_entry = ttk.Entry()
            diet_entry = ttk.Entry()
            
            
            food_name_entry.insert(0, itemInfo[0][0])
            price_entry.insert(0, itemInfo[0][1])
            category_entry.insert(0, itemInfo[0][2])
            description_entry.insert(0, itemInfo[0][3])
            diet_entry.insert(0, itemInfo[0][4])
            row_id = itemInfo[0][5]
            

            food_name_label = ttk.Label(text="Food name")
            price_label = ttk.Label(text="Price")
            category_label = ttk.Label(text="Category")
            description_label = ttk.Label(text="Description")
            diet_label = ttk.Label(text="Diet")
        
            submit_button = ttk.Button(root,text="Submit",command=lambda: submitChanges(row_id, food_name_entry, price_entry, category_entry, description_entry, diet_entry, widgets, database), width=20)        
            exit_button = ttk.Button(root,text="Exit",command=lambda: [destroyWidgets(widgets),FoodItems(widgets,credentials,branch,database)],width=20)
        
            food_name_label.pack()
            food_name_entry.pack()
        
            price_label.pack()
            price_entry.pack()
        
            category_label.pack()
            category_entry.pack()
        
            description_label.pack()
            description_entry.pack()
        
            diet_label.pack()
            diet_entry.pack()
        
            submit_button.pack()
            exit_button.pack()
        
            widgets = [food_name_label, 
                        price_label,
                        category_label,
                        description_label,
                        diet_label,
                        food_name_entry,
                        price_entry,
                        category_entry,
                        description_entry,
                        diet_entry,
                        submit_button,
                        exit_button]
            

         def updateItem(widgets,credentials):
             for i in table.selection():
                a = tuple((table.item(i)['values']))
                if a[0] != " ":
                    make_change_to_item = Tk()
                    make_change_to_item.title("Update This Food Item?")
                    are_you_sure_label = ttk.Label(make_change_to_item,text="Are you sure you want to make changes to this food item?")
                    yes_button = ttk.Button(make_change_to_item,text="Yes",command=lambda:[update_selected_item(widgets,credentials),make_change_to_item.destroy()])
                    no_button = ttk.Button(make_change_to_item,text="No", command=lambda:[make_change_to_item.destroy()])
                    are_you_sure_label.pack()
                    yes_button.pack(side=LEFT)
                    no_button.pack(side=RIGHT)
                    #update_selected_user.mainloop()
             

         def destroyWidgets(widgets):
            for x in widgets:
                    x.pack_forget()

        
             
         database.execute("SELECT name, price, category, description, diet, id FROM food_items ORDER BY name DESC")
         viewItemsList = database.fetchall()
        
    
         
         for x in widgets:
              x.pack_forget()
        
         #Creates the table containing the list of users for the system:
         table = ttk.Treeview(root,columns=('food_name', 'price', 'category', 'description', 'diet', 'id'), show='headings')
         table.heading('food_name', text = "Food Name")
         table.heading('price', text = " Price")
         table.heading('category', text = "Category")
         table.heading('description', text = "Description")
         table.heading('diet', text = "Diet")
         table.heading('id',text="ID")
        
         update_button = ttk.Button(root,text="Update",command=lambda:updateItem(widgets,credentials))
         back_button = ttk.Button(root,text="Back",command=lambda:FoodItems(widgets,credentials,branch,database))

         table.pack(fill='both',expand=TRUE)  
         update_button.pack()
         back_button.pack()
         widgets = [table,
                    update_button,
                    back_button]
            
         #Searches through the individual information about each user from the users list i.e. first name[0], last name[1], username[2], password[3], role[4] and inserts it into the table:
         for x in viewItemsList:
            food_name=  x[0]
            price = x[1]
            category = x[2]
            description = x[3] 
            diet = x[4]
            row_id = x[5]
            data = (food_name,price,category,description,diet,row_id)
            table.insert(parent = '', index=0, values= data)
        
    












    def deleteFoodItem(self,widgets,credentials,branch,database,root):
        #Deletes the selected user from the users table:
        def delete_selected_item():
            
            itemInfo = []
            for i in table.selection():
                    #print(table.item(i)['values']) 
                    #print("Delete!")
                    itemInfo.append(table.item(i)['values'])
            
            sql = "DELETE FROM food_items WHERE id = %s"
            row_id = (itemInfo[0][5], )

            database.execute(sql,row_id)
            
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
            #print(deleteAccount.rowcount, "record(s) deleted")
            itemDeletion = Tk()
            itemDeletion.title("Item Deleted")
            item_deletion_label = ttk.Label(itemDeletion, text="Food Item Successfully Deleted")
            ok_button = ttk.Button(itemDeletion,text="Ok",command=lambda:[itemDeletion.destroy(),self.deleteFoodItem(widgets,credentials,branch,database)])
            item_deletion_label.pack()
            ok_button.pack()
            

        #Asks the user if they're sure that they want to delete the selected user from the users table:
        def delete_item():
            for i in table.selection():
                 a = tuple((table.item(i)['values']))
                 if a[0] != " ":

                    deleteWindow = Tk()
                    deleteWindow.title("Delete Item")
                    are_you_sure_label = ttk.Label(deleteWindow,text="Are you sure you want to delete this item?")
                    yes_button = ttk.Button(deleteWindow,text="Yes",command=lambda:[deleteWindow.destroy(), delete_selected_item()])
                    no_button = ttk.Button(deleteWindow,text="No",command=lambda:deleteWindow.destroy())
                    are_you_sure_label.pack()
                    yes_button.pack(side=LEFT)
                    no_button.pack(side=RIGHT)
                    deleteWindow.mainloop()            
                       
        database.execute("SELECT name, price, category, description, diet, id FROM food_items ORDER BY name DESC")
        viewItemsList = database.fetchall()
        
    
        for x in widgets:
            x.pack_forget() 
        
        #Creates the table containing the list of users for the system:
        table = ttk.Treeview(root,columns=('food_name', 'price', 'category', 'description', 'diet', 'id'), show='headings')
        table.heading('food_name', text = "Food Name")
        table.heading('price', text = "Price")
        table.heading('category', text = "Category")
        table.heading('description', text = "Description")
        table.heading('diet', text = "Diet")
        table.heading('id', text="ID")
        
        delete_button = ttk.Button(root,text="Delete",command=lambda:delete_item())
        back_button = ttk.Button(root,text="Back",command=lambda:FoodItems(widgets,credentials,branch,database))

        table.pack(fill='both',expand=TRUE)  
        delete_button.pack()
        back_button.pack()
        widgets = [table,delete_button,back_button]
            
        #Searches through the individual information about each user from the users list i.e. first name[0], last name[1], username[2], password[3], role[4] and inserts it into the table:
        for x in viewItemsList:
            food_name=  x[0]
            price = x[1]
            category = x[2]
            description = x[3] 
            diet = x[4]
            row_id = x[5]
            data = (food_name,price,category,description,diet,row_id)
            table.insert(parent = '', index=0, values= data)
         


    def backToMenu(self, widgets,credentials,branch,database):
        for widget in widgets:
             widget.pack_forget()
            
        Menu(credentials,branch,database)