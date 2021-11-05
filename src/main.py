import scraper2
import WebScrapper
temp = scraper2.DataBase()
scrapperObj = WebScrapper.TemperatureScraper()
temp.connect()
temp.table()

temp.insert(scrapperObj.getlistOfCO2Data())