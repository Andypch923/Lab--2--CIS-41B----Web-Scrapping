from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from collections import namedtuple
#Scrape table off website, store in namedTuple and create a list of namedtuples storing data 
# of co2 emission from each country
class TemperatureScraper:

    def __init__(self):
        #Using beautiful soup to scrape table of class wikitable sortable from website
        # to get table of data
        myUrl = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"
        uClient = uReq(myUrl)
        page_lxml = uClient.read()
        page_soup = bs(page_lxml,"lxml")
        co2_dataNamedTuple = namedtuple('co2_dataNamedTuple',['a','b','c','d','e','f','g','h','i','j'])
        co2table = page_soup.find("table",{"class":"wikitable sortable"})

        self.__listOfCO2Data = []


        count = 0
        #store data of each row from table to namedTuple and append it to a list object listOfCO2Data
        for i in co2table.find_all('tr'):
            if count > 1:
                x = i.text.split('\n')
                temp = x[1]
                temp = temp[1:len(temp)]
                tempCO2Data = co2_dataNamedTuple(temp,x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10])
                self.__listOfCO2Data.append(tempCO2Data)
            count += 1
    
    #return private list listOfCO2Data
    def getlistOfCO2Data(self):
        return self.__listOfCO2Data



    
