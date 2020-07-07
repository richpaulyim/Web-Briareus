import mysql.connector
import json
import os

# --------------------------------
# ----- LOAD CONFIGURATION -------
# --------------------------------

# It will be assumed that user configuration
# satisfies host, user and password fields
with open('/home/richpaulyim/Documents/configs/configyf.json') as json_data:
    # make sure to have the correct path specified
    data = json.load(json_data)
sqlconfig = data['mysql']

# --------------------------------
# ------- DATABASE CREATION ------ # -------------------------------- # connect to database
FinanceDatabase = mysql.connector.connect(
    host = sqlconfig['host'],
    user = sqlconfig['user'],
    passwd = sqlconfig['passwd']
)
# create database cursor
FinanceCursor = FinanceDatabase.cursor(buffered=True)
FinanceCursor.execute("SHOW DATABASES")


# check if the database 'YahooFinance" exists among databases
exists = any(name[0] == "YahooFinance" for name in FinanceCursor)

# if it exists, drop it
if exists:
    FinanceCursor.execute("DROP DATABASE YahooFinance;")
# if it does not exist, create database, add to config.json
if not exists:
    FinanceCursor.execute("CREATE DATABASE YahooFinance")
    with open('config.json', 'r') as config: # read data
        data = json.load(config)
        data['mysql']['database'] = 'YahooFinance' # add to dictionary
    os.remove("config.json")
    with open("config.json", 'w') as newconfig: # write data
        # dump modified config into new config
        # with pretty print indent of 4
        json.dump(data, newconfig, indent=4)
        print("Database was created.")

    # ============ TABLE CREATION ============ #

    # Here the script will create 6 tables
    # in the database with respect to the
    # percentage gains and losses

    FinanceCursor.execute("USE YahooFinance")
    tables = ['Gain20', 'Gain10', 'Gain5', 'Loss5', 'Loss10', 'Loss20']
    for table in tables:
        FinanceCursor.execute("CREATE TABLE " + table + " (" + \
                         "id INT AUTO_INCREMENT PRIMARY KEY," + \
                         "symbol varchar(8)," + \
                         "company_name varchar(25)," + \
                         "intraday_price float(4)," + \
                         "price_change float(4)," + \
                         "percent_change float(4)," + \
                         "daily_volume varchar(10)," + \
                         "average_volume varchar(10)," + \
                         "market_capitalization varchar(10)," + \
                         "date varchar(10))")

# otherwise, they will be assumed to have existed
# and the the correct tables for querying
