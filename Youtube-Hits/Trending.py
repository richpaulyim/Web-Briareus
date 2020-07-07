from datetime import datetime
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

# produce range of dates
def date_range(begin, end):

    """
    Takes two strings like
    date1 = '2011-05-03'
    date2 = '2011-05-10'
    and returns range of days, bounds inclusive
    """

    return pd.date_range(begin, end).strftime("%Y-%m-%d")

# get data table from spotify charts url 
def daily_charts(date, region):

    """
    Takes date and returns list of lists of relevant data
    position, track, artist, streams, date
    region can be 'us' or 'global'
    """ 

    # create lxml using requests and bs4
    table = requests.get('https://spotifycharts.com/regional/' + \
                  region + '/daily/' + date)
    tabletxt = table.text
    tablesoup = BeautifulSoup(tabletxt, "lxml")

    chart = []
    # start parsing bs4 object
    for row in tablesoup.find_all('tr')[1:]:
        try:
            track = row.find_all('td')

            # pull all the contents
            position = track[1].text
            trackartist = track[3].text.split('\nby')
            name = trackartist[0].replace('\n','')
            artist = trackartist[1].replace('\n','')[1:]
            streams = track[4].text

            chart.append((int(position), name, artist, \
                int(streams.replace(',','')), date))
        except:
            pass

    return chart


# produce csv
def chart_makeCSV(year, name="unnamed"):
    
    """
    Generates csv file of all charts for top 200 global and us
    """

    # create list of dates
    begin = str(year) + '-01-01'
    end = str(year) + '-12-31'
    dates = list(date_range(begin, end))

    # create csvs
    uscsv = open(name+'_US_'+str(year)+'.csv','w')
    globalcsv = open(name+'_Global_'+str(year)+'.csv','w')
    uf = csv.writer(uscsv, delimiter=',')
    gf = csv.writer(globalcsv, delimiter=',')
    # write headers
    uf.writerow(['position','track','artist','streams','date'])
    gf.writerow(['position','track','artist','streams','date'])

    for day in tqdm(dates):
        usday = daily_charts(day, 'us')
        globalday = daily_charts(day, 'global')
        for us in usday:
            uf.writerow(us)
        for glob in globalday:
            gf.writerow(glob)


if __name__ == "__main__":

    #[print(date) for date in date_range('2011-05-03', '2011-05-10')]
    #print(daily_charts('2017-07-20', 'us'))

    chart_makeCSV(2017, 'CSV/top200')
    chart_makeCSV(2018, 'CSV/top200')
    chart_makeCSV(2019, 'CSV/top200')
    chart_makeCSV(2020, 'CSV/top200')
    
