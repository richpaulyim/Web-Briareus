# YahooFinance Screener Scraper 
This is a fully working version of a webscraper I built that uploads scraped data from yahoo finance's website onto a MySQL database. This project would have been literally impossible without all the open source resources and countless online forum posts and answers. 

### ConstructDatabase.py
This script creates the YahooFinance database with the user's specfied MySQL congifuration file of user, host and password. It also creates the necessary tables of 20 percent gain/loss, 10 percent gain/loss and 5 percent gain/loss.

### ExtractInsert.py
This script extracts information from Yahoo Finance using the ScreenMachine module created specifically for this problem. It also performs the insertion into the MySQL database using the mysql.connector module.

### ScreenMachine.py
This is the module that builds and implements selenium webdriver with specified modifications and hyperparameters. 

### ScreenPath.py
This script specifies the xpath locations of certain tags and their content

## Next steps:
- Automation with CronTabs, or more elegant solution, for daily scraping without manual script run. 

### How to get mysql up and running
`sudo apt-get install mysql-server`
`pip3 install mysql-connector-python`
`sudo mysql -u`
Then sign in with root-user password.
`GRANT ALL PRIVILEGES on *.* to 'user'@'localhost' IDENTIFIED BY 'password';`

### Make sure chromedriver is installed
Visit https://chromedriver.chromium.org/downloads to get a download of chromedriver and make sure it is in your system path. 
WARNING: You must install the version of chromedriver that your chrome installation is. For linux check your chrome version with `google-chrome --version`
This must be the chromedriver installation version. 
Then unzip and extract your chromedriver to path, and specify the path of the driver. In this case we extract to /bin, which is usually in PATH by default. 
`sudo apt-get install unzip`
`unzip ***chromdriver*** -d /bin`

### Using requirements.txt
Read in the requirements.txt folder
`pip install -r requirements.txt`
In your virtual environment. The correct packages will be installed. 

