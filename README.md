# Web-Briareus

This repo holds original web-scrapers. Each folder has its own README.md file.

## Scrapers

### Stock-Hits 
![alt text](https://github.com/richpaulyim/Web-Briareus/blob/master/Templates-Configs/stockhits.png)
Stock data on the NASDAQ and NYSE from the Yahoo Finance Screener. Stores data in MySQL database. 

### Spotify-Hits 
![alt text](https://github.com/richpaulyim/Web-Briareus/blob/master/Templates-Configs/spotifyhits.png)
Top trending songs on Spotify. Data is available in CSV folder; optional storing script into MySQL database.

#### (More web scrapers to be added)


## Template-Configs 

#### Configurations for MySQL databases with "config.json"
File "config.json" contains general and basic configurations that are used as
database credentials for the web scrapers above.

#### PIP for Web-Briareus with "requirements.txt"
Read in the requirements.txt folder
`pip install -r requirements.txt`
In your virtual environment. The correct packages will be installed. 

#### Crontab with "crontab"
File "crontab\_sample" contains the commands that can be used to tell cron damaeon to
execute scheduled tasks.

("Briareus, also called Aegaeon, in Greek mythology, one of three 100-armed, 50-headed Hecatoncheires (from the Greek words for “hundred” and “hands”), the sons of the deities Uranus (Heaven) and Gaea (Earth)." -Encyclopaedia Britannica)
