import mysql.connector 
#DATABASES TO CONNECT TO:
class Databases:
    birmingham_db = mysql.connector.connect(
        host = "localhost",
        user="Francis",
        password="@Deadmaul/951*",
        database="horizon_restaurant_birmingham",
        )

    bristol_db = mysql.connector.connect(
        host = "localhost",
        user="Francis",
        password="@Deadmaul/951*",
        database="horizon_restaurant_bristol",
        )


    cardiff_db = mysql.connector.connect(
        host = "localhost",
        user="Francis",
        password="@Deadmaul/951*",
        database="horizon_restaurant_cardiff",
        )


    glasgow_db = mysql.connector.connect(
        host = "localhost",
        user="Francis",
        password="@Deadmaul/951*",
        database="horizon_restaurant_glasgow",
        )


    london_db = mysql.connector.connect(
        host = "localhost",
        user="Francis",
        password="@Deadmaul/951*",
        database="horizon_restaurant_london",
        )


    manchester_db = mysql.connector.connect(
        host = "localhost",
        user="Francis",
        password="@Deadmaul/951*",
        database="horizon_restaurant_manchester",
        )


    nottingham_db = mysql.connector.connect(
        host = "localhost",
        user="Francis",
        password="@Deadmaul/951*",
        database="horizon_restaurant_nottingham",
        )
    
    def getDatabase(branch):
        
        if (branch == "Birmingham"):
            database = Databases.birmingham_db    
        
        elif(branch == "Bristol"):
            database = Databases.bristol_db
        
        elif(branch == "Cardiff"):
            database = Databases.cardiff_db
          
        elif(branch == "Glasgow"):
            database = Databases.glasgow_db
 
        elif(branch == "London"):
            database = Databases.london_db

        elif(branch == "Manchester"):
            database = Databases.manchester_db
        
        elif(branch == "Nottingham"):
            database = Databases.nottingham_db
            
        return database