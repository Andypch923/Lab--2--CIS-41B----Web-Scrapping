import DataBase
import WebScrapper
import matplotlib.pyplot as plt
import numpy as np
#Scrape from website, creating a table to store it, and extract data from database to make
# a pie chart 
def showPieChart():
    dataBaseObj = DataBase.DataBase()
    scrapperObj = WebScrapper.TemperatureScraper()
    f = open("table.txt","a+")
    f.seek(0)
    if (f.read() == ""):
        f.close()
        dataBaseObj.createTable(scrapperObj.getlistOfCO2Data())
    my_labels = dataBaseObj.fetch2017top10Countries()
    my_labels.append('Others')
    my_labels = np.array(my_labels)
    percentagesRaw = dataBaseObj.fetch2017top10Percentage()
    percentages = []
    sum = 0
    for i in percentagesRaw:
        temp = float(i.strip('%'))/100
        percentages.append(temp)
        sum += temp
    percentages.append(1-sum)
    percentages = np.array(percentages)
    plt.pie(percentages,labels = my_labels, autopct = '%.2f%%', textprops={'fontsize': 5})
    plt.show()

