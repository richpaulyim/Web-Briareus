import mysql.connector
import json
import os

# --------------------------------
# ----- LOAD CONFIGURATION -------
# --------------------------------

# It will be assumed that user configuration
# satisfies host, user and password fields
with open('/home/richpaulyim/Documents/configs/configspot.json') as json_data:
    # make sure to have the correct path specified
    data = json.load(json_data)
sqlconfig = data['mysql']

# --------------------------------
# ------- DATABASE CREATION ------
# --------------------------------

# connect to database
SpotifyDatabase = mysql.connector.connect(
    host = sqlconfig['host'],
    user = sqlconfig['user'],
    passwd = sqlconfig['passwd']
)
# create database cursor
SpotifyCursor = SpotifyDatabase.cursor(buffered=True)
SpotifyCursor.execute("SHOW DATABASES")


# check if the database 'SpotifyHits" exists among databases
exists = any(name[0] == "SpotifyHits" for name in SpotifyCursor)

# if it exists, drop it
if exists:
    SpotifyCursor.execute("DROP DATABASE SpotifyHits;")

# if it does not exist, create database, add to config.json
if not exists:
    SpotifyCursor.execute("CREATE DATABASE SpotifyHits")
    with open('config.json') as config:
        # read data
        data = json.load(config)
        data['mysql']['database'] = 'SpotifyHits' # add to dictionary
    os.remove("config.json")
    with open("config.json", 'w') as newconfig: # write data
        # dump modified config into new config
        # with pretty print indent of 4
        json.dump(data, newconfig, indent=4)
        print("Database was created.")

    # ============ TABLE CREATION ============ #

    # Here the script will create 2 tables
    # in the database for daily US and International charts 

    SpotifyCursor.execute("USE SpotifyHits")
    tables = ['USA200','Global200']
    for table in tables:
        SpotifyCursor.execute("CREATE TABLE " + table + " (" + \
                         "id INT AUTO_INCREMENT PRIMARY KEY," + \
                         "position float(4)," + \
                         "track varchar(100)," + \
                         "artist varchar(30)," + \
                         "streams float(16)," + \
                         "date varchar(10))")

