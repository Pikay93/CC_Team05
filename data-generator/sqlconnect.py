import mysql.connector
from mysql.connector import errorcode

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
else:
    cnx.close()                                                  

create_newtable = ("CREATE TABLE deals_stream ("
                        "deal_id int"
");")

drop_table = ("DROP TABLE deals_stream")

cursor.execute(drop_table)
cursor.close()
cnx.close()
