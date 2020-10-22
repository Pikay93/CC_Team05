import mysql.connector


def establlish_connection():
    try:
        db_connection = mysql.connector.connect(
            host="hostname",
            user="username_here",
            passwd="password_here",
            database="database_name"
        )
        return db_connection
    except:
        print("Error connecting to Database")
        return None