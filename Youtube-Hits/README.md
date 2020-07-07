# Spotify Top Charts Data 

This directory contains code for scraping and collecting Spotify streaming data
from since 2017.

### ConstructDatabaseYoutube.py
Creates database, or optionally deletes existing database with configured
database name of 'YoutubeTrends.'

### ExtractInsertYoutube.py
Extracts and pulls trending videos into MySQL database.

### Trending.py
Uses standard suite of python web scraping and parsing modules. Functions to
generate the CSVs in the CSV folder are contained under the '__name__' idiom describing and determining the execution context of the script apart from when it is being imported by another script.   
