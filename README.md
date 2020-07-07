# Web-Tools

This repo holds different web-scrapers and tools. Each folder has its own README.md file.

## Scrapers
### Stock-Hits 
Stock data on the NASDAQ and NYSE from the Yahoo Finance Screener. Stores data in MySQL database. 

### Spotify-Hits 
Top trending songs on Spotify. Data is available in CSV folder; optional storing script into MySQL database.


## Miscellaneous
#### Old
Old toy scripts and files.

#### Configurations for MySQL databases with "config.json"
File "config.json" contains general and basic configurations that are used as
database credentials for the web scrapers above.

#### Crontab with "crontab\_sample"
File "crontab\_sample" contains the commands that can be used to tell cron damaeon to
execute scheduled tasks.

#### PIP for Web-Briareus with "requirements.txt"
Read in the requirements.txt folder
`pip install -r requirements.txt`
In your virtual environment. The correct packages will be installed. 
