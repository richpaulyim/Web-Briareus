from bs4 import BeautifulSoup
import requests

SP400 = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_400_companies")
DJ30 = requests.get("https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average#Components")

def constituents(index):
    
    table = BeautifulSoup(index.text,"lxml")

    constituents = ["List Begins After"]
    
    for listing in table.find('table', attrs={'class':"wikitable"}).find('tbody').find_all('tr'):
        constituents.append([])
        for value in listing.find_all('td'):
            constituents[len(constituents)-2].append(value.text.replace("\n","").replace("NYSE:\xa0",""))
    constituents.pop()
    
    return constituents

SP400 = constituents(SP400)
DJ30 = constituents(DJ30)
