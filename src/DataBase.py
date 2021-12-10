import sqlite3
class DataBase:
    def __init__(self):
         #connect to a database
        conn = sqlite3.connect('temperature.db')
        #create a cursor
        cursor =  conn.cursor()
        conn.close()

    def createTable(self,tempObj):
    #connect to a database
        conn = sqlite3.connect('temperature.db')
    #create a cursor
        cursor =  conn.cursor()
    #create a Table
        cursor.execute("""CREATE TABLE temperatureTable(
                Country PRIMARY KEY,
                Fossil1990 FLOAT,
                Fossil2005 FLOAT,
                Fossil2017 FLOAT,
                Fossil2017inPercentage FLOAT,
                Fossil2017vs2019PercentageChange FLOAT,
                PerLandArea2017 FLOAT,
                PerCapita2017 FLOAT,
                TotalIncludingLUCF2018 FLOAT,
                TotalExcludingLUCF2018 FLOAT
            )""")
        file_object = open("table.txt",'a')
        file_object.write("TableCreated")
        file_object.close()
    #parse list of namedTuples into table
        cursor.executemany("INSERT INTO temperatureTable VALUES(?,?,?,?,?,?,?,?,?,?)",tempObj)
        cursor.execute("DELETE FROM temperatureTable WHERE Country LIKE '%World%'")
    #commits commands
        conn.commit()
    #close our connection
        conn.close()

    #fetch country names for the top 10 countries with highest co2 emissions in 2017
    def fetch2017top10Countries(self):
        conn = sqlite3.connect('temperature.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Country FROM temperatureTable ORDER BY Fossil2017inPercentage DESC LIMIT 10')
        items = [ x[0] for x in cursor.fetchall()]  
        return items

    #fetch country emission percentages for the top 10 countries with highest co2 emissions in 2017
    def fetch2017top10Percentage(self):
        conn = sqlite3.connect('temperature.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Fossil2017inPercentage FROM temperatureTable ORDER BY Fossil2017inPercentage DESC LIMIT 10")
        items = [ x[0] for x in cursor.fetchall()]  
        return items