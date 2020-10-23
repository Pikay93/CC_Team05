import mysql.connector
from mysql.connector import errorcode
import json

def verifyUser(user, password):
    try:
        cnx = mysql.connector.connect(host = 'localhost', 
                                    database = 'db_grad_cs_1917', 
                                    user = 'root', 
                                    password='ppp')
        cursor = cnx.cursor()                              
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()                     
                                
    # users, anonymous_users, login_trail
    # counterparty, deals, instruments
    sql = """
    SELECT * from users where user_id=%s and user_pwd=%s
    """

    cursor.execute(sql, (user, password))

    result = cursor.fetchall()
    row_count=cursor.rowcount

    cursor.close()
    cnx.close()
    
    print(f"Found: {row_count>0}")

    return row_count>0

# verifyUser("aasas","asas")
# verifyUser("alison","gradprog2016@07")
