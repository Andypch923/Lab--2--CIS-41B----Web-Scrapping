import WebScrapper
import DataBase

temp = DataBase.DataBase()
sth = WebScrapper.TemperatureScraper()

temp.createTable(sth.getlistOfCO2Data())
for i in temp.fetch2017top10Countries():
    print(i)