import Input
import sqlite3

class DataBase:
    def __init__(self):
        return 
    def connect(self):
        try:
            #name the database
            connect = sqlite3.connect('CO2.db')
            #create curser
            cursor = connect.cursor()
            Query = "select sqlite_version();"
            cursor.execute(Query)
            data = cursor.fetchall()

        except sqlite3.Error as error:
            error
    def table(self):
        try:
            connect = sqlite3.connect('CO2.db')
            create_table_query = '''CREATE TABLE Database (
                                        country PRIMARY KEY, percentages FLOAT)'''

            cursor = connect.cursor()
            cursor.execute(create_table_query)
            #table created
            connect.commit()

        except sqlite3.Error as error:
            error

    def insert(self,lst):
        try:
            connect = sqlite3.connect('CO2.db')
            cursor = connect.cursor()
            insert_query = """ INSERT INTO Database
                                    (country,percentages) VALUES (?,?)"""
            cursor.executemany(insert_query,lst)
            cursor.execute("DELETE FROM Database WHERE country LIKE '%World%'")
            connect.commit()
            cursor.close()

        except sqlite3.Error as error:
                error
    #read table from db before graphing
    def readTable(self):
        try:
            connect = sqlite3.connect('CO2.db')
            cursor = connect.cursor()
            query = """SELECT country,percentages from Database ORDER BY percentages DESC LIMIT 10"""
            cursor.execute(query)
            data = cursor.fetchall()
            self.country = []
            self.percentage= []
            for row in data:
                self.country.append(row[0])
                self.percentage.append(row[1])
            cursor.close()
            return self.country, self.percentage

        except sqlite3.Error as error:
            error
        if (connect):
            connect.close()
