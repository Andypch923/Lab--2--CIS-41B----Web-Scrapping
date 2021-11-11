from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import namedtuple

class input:
# open/read
    def __init__(self):
        html = urlopen('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions')
        parseHtml = BeautifulSoup(html, 'html.parser')
        table = parseHtml.find('table', {'class':'wikitable sortable'})

#Create a NamedTuple
        co2NT = namedtuple('co2NT',['country','percentage'])
#Create an empty list
        self.lst = []
        counter = 0
        for i in table.find_all('tr'): 
            if counter>1: 
                title = i.text.split('\n')
                nameOfCountry = title[1] 
                nameOfCountry = nameOfCountry[1:len(nameOfCountry)]
                NT = co2NT(nameOfCountry,float(title[5].strip('%'))/100) 
                self.lst.append(NT)
            counter += 1

    def getlst(self):
        return self.lst