# import the Spotlight module
from Spotlight import *
from datetime import timedelta, date

# import database and parsing library 
import mysql.connector
import json

# loading json MySQL configurations and database
with open("/home/richpaulyim/Documents/configs/configspot.json") as json_data:
    data = json.load(json_data)
sqlconfig = data['mysql']

# connecting to database and creating cursor
spotifyDB = mysql.connector.connect(
    host = sqlconfig['host'],
    user = sqlconfig['user'],
    passwd = sqlconfig['passwd'],
    database = sqlconfig['database']
)
spotifyCursor = spotifyDB.cursor()

# list of available tables to append to 
tablelist = ['USA200', 'Global200']
regions = ['us', 'global']

# generate "yesterday's date" data is guaranteed 
# to be available from the previous day
day = str(date.today() - timedelta(days=1))
print(day)

# scrape and insert data into tables
for i, config in enumerate(tablelist):
    data = daily_charts(day, regions[i])
    print(data)
    sql_cmd = "INSERT INTO " + config + " (" +\
                     " position," + \
                     " track," + \
                     " artist," + \
                     " streams," + \
                     " date)" + \
                " VALUES (%s,%s,%s,%s,%s)"
    spotifyCursor.executemany(sql_cmd, data)
    spotifyDB.commit()
    print(spotifyCursor.rowcount, "was inserted")

# symbol, name, intraday price, change, 
# percentage change, volume, average volume (3 month)
# market cap, date
