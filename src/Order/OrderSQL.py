from Databases.Databases import Databases


class OrderSQL():
    
    def getOrders(branch):
        
        if branch == "Birmingham":
            database = Databases.birmingham_db.cursor()
        
        elif branch == "Bristol":
            database = Databases.bristol_db.cursor()
            
        elif branch == "Cardiff":
            database = Databases.cardiff_db.cursor()
            
        elif branch == "Glasgow":
            database = Databases.glasgow_db.cursor()
            
        elif branch == "London":
            database = Databases.london_db.cursor()
            
        elif branch == "Manchester":
            database = Databases.manchester_db.cursor()
            
        elif branch == "Nottingham":
            database = Databases.nottingham_db.cursor()
        
        database.execute("SELECT * FROM orders ORDER BY order_number DESC")
        view_orders = database.fetchall()
        
        return view_orders
    
    def get_food_items(branch,category):
        
        if branch == "Birmingham":
            database = Databases.birmingham_db.cursor()
        
        elif branch == "Bristol":
            database = Databases.bristol_db.cursor()
            
        elif branch == "Cardiff":
            database = Databases.cardiff_db.cursor()
            
        elif branch == "Glasgow":
            database = Databases.glasgow_db.cursor()
            
        elif branch == "London":
            database = Databases.london_db.cursor()
            
        elif branch == "Manchester":
            database = Databases.manchester_db.cursor()
            
        elif branch == "Nottingham":
            database = Databases.nottingham_db.cursor()
        
        sql = "SELECT * FROM food_items WHERE category = %s ORDER BY name DESC"
        database.execute(sql,category)
        view_food_items = database.fetchall()
        
        return view_food_items
    
    def get_food_categories(branch):
        
        if branch == "Birmingham":
            database = Databases.birmingham_db.cursor()
        
        elif branch == "Bristol":
            database = Databases.bristol_db.cursor()
            
        elif branch == "Cardiff":
            database = Databases.cardiff_db.cursor()
            
        elif branch == "Glasgow":
            database = Databases.glasgow_db.cursor()
            
        elif branch == "London":
            database = Databases.london_db.cursor()
            
        elif branch == "Manchester":
            database = Databases.manchester_db.cursor()
            
        elif branch == "Nottingham":
            database = Databases.nottingham_db.cursor()
        
        database.execute("SELECT * FROM food_categories ORDER BY name DESC")
        view_food_categories = database.fetchall()
        
        return view_food_categories
    
    def addOrder(order,branch):
        food_item = order[0]
        price = order[1]
        staff = order[2]
        order_status = order[3]
        payment_status = order[4]
        table_number = order[5]
        
        database = Databases.getDatabase(branch).cursor()
        sql = "INSERT INTO orders (item, price, staff, order_status, payment_status, table_number) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (food_item, price, staff, order_status, payment_status, table_number)
        database.execute(sql,val)
        #Commits Changes To Relevant Database Based On The Branch That The User Is Making Changes To:
        if (branch == "Birmingham"):
            Databases.birmingham_db.commit()
            
        elif(branch == "Bristol"):
            Databases.bristol_db.commit()
        
        elif(branch == "Cardiff"):
            Databases.cardiff_db.commit()
          
        elif(branch == "Glasgow"):
            Databases.glasgow_db.commit()
 
        elif(branch == "London"):
            Databases.london_db.commit()

        elif(branch == "Manchester"):
            Databases.manchester_db.commit()
        
        elif(branch == "Nottingham"):
            Databases.nottingham_db.commit()
            
            
    def updateOrder(order,branch):
        food_item = order[0]
        price = order[1]
        staff = order[2]
        order_status = order[3]
        payment_status = order[4]
        table_number = order[5]
        order_number = order[6]
        
        database = Databases.getDatabase(branch).cursor()
        sql = "UPDATE orders SET item = %s WHERE order_number = %s"
        val = (food_item,order_number)
        database.execute(sql,val)

        sql = "UPDATE orders SET price = %s WHERE order_number = %s"
        val = (price,order_number)
        database.execute(sql,val)

        sql = "UPDATE orders SET staff = %s WHERE order_number = %s"
        val = (staff,order_number)
        database.execute(sql,val)
        
        #Commits Changes To Relevant Database Based On The Branch That The User Is Making Changes To:
        if (branch == "Birmingham"):
            Databases.birmingham_db.commit()
            
        elif(branch == "Bristol"):
            Databases.bristol_db.commit()
        
        elif(branch == "Cardiff"):
            Databases.cardiff_db.commit()
          
        elif(branch == "Glasgow"):
            Databases.glasgow_db.commit()
 
        elif(branch == "London"):
            Databases.london_db.commit()

        elif(branch == "Manchester"):
            Databases.manchester_db.commit()
        
        elif(branch == "Nottingham"):
            Databases.nottingham_db.commit()
        
        
    def cancelOrder(orderInfo,branch):
        
        sql = "DELETE FROM orders WHERE order_number = %s"
        orderNO = (orderInfo[0][6], )
    
        #Commits Changes To Relevant Database Based On The Branch That The User Is Making Changes To:
        if (branch == "Birmingham"):
            try:
                with Databases.birmingham_db.cursor() as database:
                    database.execute(sql,orderNO)
                    Databases.birmingham_db.commit()
            finally:  
                    pass         
        
        
        elif(branch == "Bristol"):
            try:
                with Databases.bristol_db.cursor() as database:
                    database.execute(sql,orderNO)
                    Databases.bristol_db.commit()
            finally: 
                    pass      
                                       

        elif(branch == "Cardiff"):
            try:
                with Databases.cardiff_db.cursor() as database:
                    database.execute(sql,orderNO)
                    Databases.cardiff_db.commit()
            finally:  
                    pass         


        elif(branch == "Glasgow"):
            try:
                with Databases.glasgow_db.cursor() as database:
                    database.execute(sql,orderNO)
                    Databases.glasgow_db.commit()
            finally:  
                    pass 
                        

        elif(branch == "London"):
            try:
                with Databases.london_db.cursor() as database:
                    database.execute(sql,orderNO)
                    Databases.london_db.commit()
            finally: 
                    pass         
                
        
        elif(branch == "Manchester"):
            try:
                with Databases.manchester_db.cursor() as database:
                    database.execute(sql,orderNO)
                    Databases.manchester_db.commit()
            finally:  
                    pass         
                
        
        elif(branch == "Nottingham"):
            try:
                with Databases.nottingham_db.cursor() as database:
                    database.execute(sql,orderNO)
                    Databases.nottingham_db.commit()
            finally:  
                    pass 
        
