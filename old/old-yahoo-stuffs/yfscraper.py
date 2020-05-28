from bs4 import BeautifulSoup
import requests

def daily_active(which="both"):
    """
    Daily list of gainers and losers

    Ordered on percentage change, specify, 'which' as
        'both', 'Gainers', 'losers'
        index 3 represents intraday price
        index 4 represents intraday price change
        index 5 represents overall percentage change


    """

    gainers = 'https://finance.yahoo.com/gainers'
    losers = 'https://finance.yahoo.com/losers'

    gain = requests.get(gainers)
    lose = requests.get(losers)
    gaindata = gain.text
    losedata = lose.text

    gainsoup = BeautifulSoup(gaindata,"lxml")
    losesoup = BeautifulSoup(losedata,"lxml")

    values = []

    if which == 'both' or which == 'gainers':

    if which == 'both' or which == 'losers':
        for listing in losesoup.find_all('tr', attrs={'class':'simpTblRow'}):
            for value in listing.find_all('td'):
                values.append(value.text)

    values = [values[x:x+5] for x in range(0,len(values),10)]

    for i in range(0, len(values)):
        values[i][2] = float(values[i][2])
        values[i][3] = float(values[i][3])
        values[i][4] = float(values[i][4][:-1])

    return values

print(daily_active(which='losers'))
