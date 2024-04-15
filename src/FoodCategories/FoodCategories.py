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


class FoodCategories():
    
    def __init__(self, widgets,credentials,branch,database,root):
        
        for x in widgets:
            x.pack_forget() 
        
        food_items_label = ttk.Label(root,text="Food Categories",font=("Arial",28))
        create_food_item_button = ttk.Button(root,text="Create Food Category",command=lambda:self.createFoodCategory(widgets,credentials,branch,database,root),width=50)
        read_food_item_button = ttk.Button(root,text="Read Food Categories",command=lambda:self.readFoodCategories(widgets,credentials,branch,database,root),width=50) 
        update_food_item_button = ttk.Button(root,text="Update Food Category",command=lambda:self.updateFoodCategory(widgets,credentials,branch,database,root),width=50)
        delete_food_item_button = ttk.Button(root,text="Delete Food Category",command=lambda:self.deleteFoodCategory(widgets,credentials,branch,database,root),width=50)
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
        










#CREATE FOOD CATEGORY:
    def createFoodCategory(self, widgets,credentials,branch,database,root):
        
        def addFoodCategory(category_name,branch,database):
            
            sql = "SELECT * FROM food_categories WHERE name = %s"
            name = (category_name,)
            database.execute(sql,name)
            results = database.fetchall()
            
            existentCategory = FALSE
            #Checks to see if a category already exists:
            for x in results:
                #If the submitted category is not new then it will not be added and a pop window will notify the user:
                if x[0] == category_name:
                     exists = Tk()
                     exists.title("Category Already Exists")
                     existent_category_label = ttk.Label(exists,text="Category " + category_name + " Already Exists")
                     ok = ttk.Button(exists,text="Ok",command=lambda:exists.destroy())
                     existent_category_label.pack()
                     ok.pack()
                     existentCategory = TRUE
                     
            #If the submitted category is new then it will be added: 
            if existentCategory == FALSE:   
                if category_name != '':
                    sql = "INSERT INTO food_categories (name) VALUE (%s)"
                    val = (category_name, )
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

                    foodCategoryAdded = Tk()
                    foodCategoryAdded.title("Food Category Created")
                    food_category_created_label = ttk.Label(foodCategoryAdded,text="Food Category " + category_name + " Has Been Created")
                    ok = ttk.Button(foodCategoryAdded,text="Ok",command=lambda:foodCategoryAdded.destroy())
                    food_category_created_label.pack()
                    ok.pack()
                else:
                     exists = Tk()
                     exists.title("Category Incomplete")
                     existent_category_label = ttk.Label(exists,text="Please fill the category field")
                     ok = ttk.Button(exists,text="Ok",command=lambda:exists.destroy())
                     existent_category_label.pack()
                     ok.pack()
                       

        def submit(food_category_entry):
            
            category_name = food_category_entry.get()

           
            submitWindow = Tk()
            submitWindow.title("Submit Food Category?")
            submit_label = ttk.Label(submitWindow,text="Submit " + category_name + " As Food Category?")
            yes = ttk.Button(submitWindow,text="Yes",command=lambda:[addFoodCategory(category_name,branch,database),submitWindow.destroy()])
            no = ttk.Button(submitWindow,text="No",command=lambda:submitWindow.destroy())
            submit_label.pack()
            yes.pack()
            no.pack()
            
            
        def backToFoodCategories(widgets,credentials,branch,database):
            FoodCategories(widgets,credentials,branch,database)
             


        for x in widgets:
             x.pack_forget()
             
        create_food_category_label = ttk.Label(root,text="Create Food Category",font=("Arial",28))
        enter_food_category_label = ttk.Label(root,text="Please Enter Food Category Below:")
        food_category_entry = ttk.Entry()
        back_button = ttk.Button(root,text="Back",command=lambda:backToFoodCategories(widgets,credentials,branch,database),width=50)
        submit_button = ttk.Button(root,text="Submit",command=lambda:submit(food_category_entry),width=50)
        
        create_food_category_label.pack()
        enter_food_category_label.pack()
        food_category_entry.pack()
        submit_button.pack()
        back_button.pack()
        widgets = [create_food_category_label,
                   enter_food_category_label,
                   food_category_entry,
                   submit_button,
                   back_button]
        
        
    










#READ FOOD CATEGORIES:
    def readFoodCategories(self,widgets,credentials,branch,database,root):
            
            #View items inside selected food category:
            def viewItemsInSelectedFoodCategory(widgets,database):
                
                paging = 2
                for i in foodCategoriesTable.selection():
                    sql = "SELECT * FROM food_items WHERE category = %s" 
                    a = tuple((foodCategoriesTable.item(i)['values']))
                    if a[0] != " ":
                        for x in widgets:
                             x.pack_forget()
                        category = a
                    

                        database.execute(sql,category)
                        items = database.fetchall()
                    
                        foodItemsInCategoryTable = ttk.Treeview(root,columns=('food_item', 'price', 'category', 'description', 'diet'), show='headings')
                        foodItemsInCategoryTable.heading('food_item', text="Food Item")
                        foodItemsInCategoryTable.heading('price', text="Price") 
                        foodItemsInCategoryTable.heading('category', text="Category")
                        foodItemsInCategoryTable.heading('description', text="Description")
                        foodItemsInCategoryTable.heading('diet', text="Diet")
                    
                        foodItemsInCategoryTable.pack(fill='both',expand=TRUE)
                        back_button= ttk.Button(root,text="Back",command=lambda:back(paging, widgets, credentials,branch,database))
                        back_button.pack()
                        widgets = [foodItemsInCategoryTable,back_button]
                    
                        for x in items:
                        
                            food_item = x[0]
                            price = x[1]
                            category = x[2]
                            description = x[3]
                            diet = x[4]
                            data = (food_item,price,category,description,diet)
                            foodItemsInCategoryTable.insert(parent = '', index=0, values=data)
                
            def back(paging,widgets,credentials,branch,database):
                for x in widgets:
                     x.pack_forget()
                if paging == 1:
                    FoodCategories(widgets,credentials,branch,database)
                elif paging == 2:
                    self.readFoodCategories(widgets,credentials,branch,database)
                        

            for x in widgets:
                x.pack_forget() 
            #View food categories:
            database.execute("SELECT * FROM food_categories ORDER BY name DESC")
            foodCategoriesList = database.fetchall()
           
            paging = 1
            
        
            #Creates the table containing the list of users for the system:
            foodCategoriesTable = ttk.Treeview(root,columns=('categories', ), show='headings')
            foodCategoriesTable.heading('categories', text = "Food Categories")
        
            foodCategoriesTable.pack(fill='both',expand=TRUE)   
            
            view_items_button = ttk.Button(root,text="View Items",command=lambda:viewItemsInSelectedFoodCategory(widgets, database))
            back_button = ttk.Button(root,text="Back",command=lambda:back(paging,widgets,credentials,branch,database))
            view_items_button.pack()
            back_button.pack()
            
            widgets = [foodCategoriesTable,
                       view_items_button,
                       back_button]
    
            
        #Searches through the individual information about each user from the users list i.e. first name[0], last name[1], username[2], password[3], role[4] and inserts it into the table:
            for x in foodCategoriesList:
                foodCategoriesTable.insert(parent = '', index=0, values= x)
           
    
















#UPDATE FOOD CATEGORIES:
    def updateFoodCategory(self, widgets, credentials, branch,database,root):
         
         def viewItemsInSelectedFoodCategory(paging,widgets,credentials,branch,database):
                
                paging = 2
                for i in foodCategoriesTable.selection():
                    sql = "SELECT * FROM food_items WHERE category = %s" 
                    a = tuple((foodCategoriesTable.item(i)['values']))
                    if a[0] != " ":
                        for x in widgets:
                             x.pack_forget()
                        category = a
                    

                        database.execute(sql,category)
                        items = database.fetchall()
                    
                        foodItemsInCategoryTable = ttk.Treeview(root,columns=('food_item', 'price', 'category', 'description', 'diet'), show='headings')
                        foodItemsInCategoryTable.heading('food_item', text="Food Item")
                        foodItemsInCategoryTable.heading('price', text="Price") 
                        foodItemsInCategoryTable.heading('category', text="Category")
                        foodItemsInCategoryTable.heading('description', text="Description")
                        foodItemsInCategoryTable.heading('diet', text="Diet")
                    
                        foodItemsInCategoryTable.pack(fill='both',expand=TRUE)
                        back_button= ttk.Button(root,text="Back",command=lambda:back(paging, widgets, credentials,branch,database))
                        back_button.pack()
                        widgets = [foodItemsInCategoryTable,back_button]
                    
                        for x in items:
                        
                            food_item = x[0]
                            price = x[1]
                            category = x[2]
                            description = x[3]
                            diet = x[4]
                            data = (food_item,price,category,description,diet)
                            foodItemsInCategoryTable.insert(parent = '', index=0, values=data)
                        


#CATEGORY NAME CHANGE:
         def submitCategoryNameChange(category_entry,categoryChange, widgets, credentials, branch,database):
            
           
            new_category_name = category_entry.get()
            if new_category_name != "":
                categoryChange.destroy()
            #Grabs the name of the old category:
                for i in foodCategoriesTable.selection():
                        sql = "SELECT * FROM food_categories WHERE name = %s" 
                        a = tuple((foodCategoriesTable.item(i)['values']))
                        oldCategory = a[0]
            
             
                sql = "UPDATE food_categories SET name = %s WHERE name = %s"
                val = (new_category_name,oldCategory,  )
                database.execute(sql, val)
            
                sql = "UPDATE food_items SET category = %s WHERE category = %s"
                val = (new_category_name,oldCategory,  )
                database.execute(sql, val)
                
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
            
                changed = Tk()
                changed.title("Category Name Changed")
                changed_label = ttk.Label(changed,text=oldCategory + " Has Been Changed To " + new_category_name)
                ok = ttk.Button(changed,text="Ok",command=lambda:[changed.destroy(), self.updateFoodCategory(widgets, credentials, branch,database)])
                changed_label.pack()
                ok.pack()
                
            else:
                emptyField = Tk()
                emptyField.title("Category Incomplete!")
                fill_category = ttk.Label(emptyField,text="Please Fill Category Field")
                ok = ttk.Button(emptyField,text="Ok",command=lambda:emptyField.destroy())
                fill_category.pack()
                ok.pack()


         def renameSelectedCategory(widgets, credentials,branch,database):
            
            categoryChange = Tk()
            categoryChange.title("Rename Category")
            category_label = ttk.Label(categoryChange,text="New Name Of Category:")
            food_category_entry = ttk.Entry(categoryChange)
            category_label.pack()
            food_category_entry.pack()
            submit = ttk.Button(categoryChange,text="Submit",command=lambda:[submitCategoryNameChange(food_category_entry,categoryChange, widgets, credentials, branch,database)])
            submit.pack()

         def renameCategory(widgets, credentials,):
            for i in foodCategoriesTable.selection():
                a = tuple((foodCategoriesTable.item(i)['values']))
                if a[0] != " ":
                    
                    rename = Tk()
                    rename.title("Rename Category?")
                    rename_label = ttk.Label(rename,text="Are you sure you want to rename this category?")
                    yes = ttk.Button(rename,text="Yes",command=lambda:[rename.destroy(),renameSelectedCategory(widgets, credentials,branch,database)])
                    no = ttk.Button(rename,text="No",command=lambda:rename.destroy())
                    rename_label.pack()
                    yes.pack()
                    no.pack()
           

         def back(paging,widgets,credentials,branch,database):
                for x in widgets:
                     x.pack_forget()
                if paging == 1:
                    FoodCategories(widgets,credentials,branch,database)
                elif paging == 2:
                    self.updateFoodCategory(widgets,credentials,branch,database)
                


                    
         for x in widgets:
             x.pack_forget() 
    
         database.execute("SELECT * FROM food_categories ORDER BY name DESC")
         foodCategoriesList = database.fetchall()
         paging = 1
                
        
         #Creates the table containing the list of users for the system:
         foodCategoriesTable = ttk.Treeview(root,columns=('categories', ), show='headings')
         foodCategoriesTable.heading('categories', text = "Food Categories")
        
         foodCategoriesTable.pack(fill='both',expand=TRUE)   
            
         view_items_button = ttk.Button(root,text="View Items",command=lambda:viewItemsInSelectedFoodCategory(paging,widgets,credentials,branch,database))
         rename_button = ttk.Button(root,text="Rename",command=lambda:renameCategory(widgets, credentials,))
         back_button = ttk.Button(root,text="Back",command=lambda:back(paging,widgets,credentials,branch,database))
         
         rename_button.pack()
         view_items_button.pack()
         rename_button.pack()
         back_button.pack()
         widgets = [foodCategoriesTable,
                       view_items_button,
                       rename_button,
                       back_button]
         
    
            
         #Searches through the individual information about each user from the users list i.e. first name[0], last name[1], username[2], password[3], role[4] and inserts it into the table:
         for x in foodCategoriesList:
            foodCategoriesTable.insert(parent = '', index=0, values= x)
        

























#DELETE FOOD CATEGORIES:
    def deleteFoodCategory(self,widgets,credentials, branch,database,root):
        
        def deleteSelectedFoodCategory():
                for i in foodCategoriesTable.selection():
                    sql = "DELETE FROM food_categories WHERE name = %s" 
                    category = tuple((foodCategoriesTable.item(i)['values']))
                    database.execute(sql,category)
                    
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



                foodCategoryRemoved = Tk()
                foodCategoryRemoved.title("Food Category Deleted")
                food_category_removed_label = ttk.Label(foodCategoryRemoved,text="Food Category Deleted")
                ok = ttk.Button(foodCategoryRemoved,text="OK",command=lambda:[foodCategoryRemoved.destroy(),self.deleteFoodCategory(widgets,credentials,branch,database)])
                                
                food_category_removed_label.pack()
                ok.pack()
                    
                   
        def deleteFoodCategory():
            for i in foodCategoriesTable.selection():
                a = tuple(foodCategoriesTable.item(i)['values']) 
                if a != " ":
                    delete = Tk()
                    delete.title("Delete Food Category?")
                    delete.geometry("275x50")
                    delete_label = ttk.Label(delete,text="Are You Sure You Want To Delete This Category?")
                    yes = ttk.Button(delete,text="Yes",command=lambda:[deleteSelectedFoodCategory(),delete.destroy()])
                    no = ttk.Button(delete,text="No",command=lambda:delete.destroy())
                    delete_label.pack()
                    yes.pack(side=LEFT)
                    no.pack(side=RIGHT)
            


        database.execute("SELECT * FROM food_categories ORDER BY name DESC")
        foodCategoriesList = database.fetchall()
           
        for x in widgets:
            x.pack_forget() 
        
        #Creates the table containing the list of users for the system:
        foodCategoriesTable = ttk.Treeview(root,columns=('categories', ), show='headings')
        foodCategoriesTable.heading('categories', text = "Food Categories")
        
        foodCategoriesTable.pack(fill='both',expand=TRUE)   
            
        delete_category_button = ttk.Button(root,text="Delete",command=lambda:deleteFoodCategory())
        back_button = ttk.Button(root,text="Back",command=lambda:FoodCategories(widgets,credentials,branch,database))
        delete_category_button.pack()
        back_button.pack()
        widgets = [foodCategoriesTable,back_button,delete_category_button]
            
        #Searches through the individual information about each user from the users list i.e. first name[0], last name[1], username[2], password[3], role[4] and inserts it into the table:
        for x in foodCategoriesList:
            foodCategoriesTable.insert(parent = '', index=0, values= x) 
  
  
    def backToMenu(self, widgets,credentials,branch,database):
        for widget in widgets:
             widget.pack_forget()
            
        Menu(credentials,branch,database)
        
