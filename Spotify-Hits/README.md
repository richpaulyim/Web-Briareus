# Spotify Top Charts Data 

This directory contains code for scraping and collecting Spotify streaming data
from since 2017.

### CSV
Contains top 200 charts from 2017 to now (July 5, 2020) in 8 CSVs, 2 for each
year for US and global regional differences in streaming. Top charts for 2020
are still under construction as of commit date to this directory. 

### ConstructDatabaseSpotify.py
Creates database, or optionally deletes existing database with configured
database name of 'SpotifyHits.'

### ExtractInsertSpotify.py
Extracts and Inserts data from previous day (yesterday). This can be run as
python script. 

### Spotlight.py
Uses standard suite of python web scraping and parsing modules. Functions to
generate the CSVs in the CSV folder are contained under the "main" namespace
contained at the very end. 
