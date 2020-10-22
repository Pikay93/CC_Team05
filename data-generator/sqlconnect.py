import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(host = 'localhost', database = 'db_grad_cs_1917', user = 'root', password='ppp')
cursor = cnx.cursor()

create_newtable = ("CREATE TABLE deals_stream ("
                    "deal_id int"
");")

drop_table = ("DROP TABLE deals_stream")

cursor.execute(drop_table)
cursor.close()
cnx.close()
