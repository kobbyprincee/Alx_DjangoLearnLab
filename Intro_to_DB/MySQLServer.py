# Import modules
import mysql.connector
from mysql.connector import connect, Error

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "kobbyprince",
        password = "Password123!",
        )
        
    mycursor = mydb.cursor()
    
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alxbookstore' created or alredy exists!")
    
    # close the connection 
    mycursor.close()
    mydb.close()
    
    with connect(
            host = "localhost",
            user = "kobbyprince",
            password = "Password123!",
            database = "alx_book_store",
            ) as connection:
                print(connection)

except mysql.connector.Error as e:
    print("Error: ", e)
