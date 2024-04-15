import mysql.connector

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

mycursor = birmingham_db.cursor()
#mycursor.execute("ALTER TABLE orders ADD COLUMN order_number INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("SELECT * FROM orders")
print (mycursor.description)
#print("Successful!")