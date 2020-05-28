# import the finance screener
import ScreenMachine as sm
from ScreenerPath import *

# import database and parsing library 
import mysql.connector
import json

# loading json MySQL configurations and database
with open("~/Documents/Configs/config_yf.json") as json_data:
    data = json.load(json_data)
sqlconfig = data['mysql']

# connecting to database and creating cursor
financeDB = mysql.connector.connect(
    host = sqlconfig['host'],
    user = sqlconfig['user'],
    passwd = sqlconfig['passwd'],
    database = sqlconfig['database']
)
financeCursor = financeDB.cursor()

# Build ScreenMachine() Yahoo Finance web driver object
obj = sm.ScreenMachine(headless=True)

# list of available tables to be built
tablelist = [
            ('Gain20',  20),
            ('Gain10',  10),
            ('Gain5' ,  5),
            ('Loss20', -20),
            ('Loss10', -10),
            ('Loss5' , -5)]

# scrape and insert data into tables
for config in tablelist:
    obj.build_screener(verbose=False)
    if config[1] > 0:
        data = obj.filter_config(verbose=False,
                                 greater=True,
                                 val=config[1])
    else:
        data = obj.filter_config(verbose=False,
                                 greater=False,
                                 val=config[1])
    sql_cmd = "INSERT INTO " +config[0]+ " (" +\
                     "symbol," + \
                     " company_name," + \
                     " intraday_price," + \
                     " price_change," + \
                     " percent_change," + \
                     " daily_volume," + \
                     " average_volume," + \
                     " market_capitalization," + \
                     " date)" + \
                " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    financeCursor.executemany(sql_cmd, data)
    financeDB.commit()
    print(financeCursor.rowcount, "was inserted")

# symbol, name, intraday price, change, 
# percentage change, volume, average volume (3 month)
# market cap, date
