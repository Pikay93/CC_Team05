import mysql.connector
from mysql.connector import errorcode
import pandas as pd

cnx = mysql.connector.connect(host = 'localhost', database = 'db_grad_cs_1917', user = 'root', password='ppp')
cursor = cnx.cursor()

buy1001 = ("SELECT deal_instrument_id AS 'Instrument ID', instrument_name AS 'Instrument Name', " 
           "deal_type AS 'Deal Type', AVG(deal_amount) AS 'Average Price (£)' FROM deal "
           "JOIN instrument ON instrument_id = deal_instrument_id "
           "GROUP BY deal_instrument_id, deal_type "
           "ORDER BY deal_instrument_id;")

cursor.execute(buy1001)
average_prices = pd.DataFrame(cursor.fetchall(),columns=["Instrument ID","Instrument Name","Deal Type","Average Price (£)"])
average_prices_json = average_prices.to_json()
cursor.close() 
cnx.close()
