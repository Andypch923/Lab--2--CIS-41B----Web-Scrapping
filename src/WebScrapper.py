from typing import NamedTuple
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pandas as pd

myUrl = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"
uClient = uReq(myUrl)
page_html = uClient.read()
page_soup = bs(page_html,"html.parser")

co2_dataFrame = {
    "Country":[],
    "1990 Fossil CO2 Emissions (Mt CO2)":[],
    "2005 Fossil CO2 Emissions (Mt CO2)":[],
    "2017 Fossil CO2 Emissions (Mt CO2)":[],
    "2017 Fossil CO2 Emissions (% of the world)":[],
    "2017 vs 1990 change (%)":[],
    "2017 Per land area (t CO2/km^2/yr)":[],
    "2017 Per capita (t CO2/cap/yr)":[],
    "2018 CO2 emissions (Total including LUCF)":[],
    "2018 CO2 emissions (Total excluding LUCF)":[]
}



co2table = page_soup.findAll("table",{"class":"wikitable sortable jquery-tablesorter"})
print(len(co2table))


