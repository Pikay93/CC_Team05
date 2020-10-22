import mysql.connector


def establish_connection():
    try:
        db_connection = mysql.connector.connect(
            host='127.0.0.1',
            database='db_grad_cs_1917',
            user='root',
            password='ppp'
        )
        return db_connection
    except:
        print("Error connecting to Database")
        return None