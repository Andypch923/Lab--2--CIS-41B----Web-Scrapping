
import sqlite3

class DataBase:
    def init(self,lst):
        self.lst = lst
    def connect(self):
            #name the database
            connect = sqlite3.connect('CO2.db')
            #create curser
            cursor = connect.cursor()
            Query = "select sqlite_version();"
            cursor.execute(Query)
            data = cursor.fetchall()


    def table(self):
            connect = sqlite3.connect('CO2.db')
            create_table_query = '''CREATE TABLE Database (
                                        country PRIMARY KEY, percentage Float);'''

            cursor = connect.cursor()
            cursor.execute(create_table_query)
            #table created
            connect.commit()


    def insert(self,lst):
            connect = sqlite3.connect('CO2.db')
            cursor = connect.cursor()
            insert_query = """ INSERT INTO Database
                                    (country,percentage) VALUES (?,?),lst"""
            cursor.executemany(insert_query)
            connect.commit()

    #read table from db before graphing
    def readTable(self, lst):
            connect = sqlite3.connect('CO2.db')
            cursor = connect.cursor()
            query = """SELECT * from Database"""
            cursor.execute(query)
            data = cursor.fetchall()
            country = []
            percentage= []
            for row in data:
                country.append(row[0])
                percentage.append (row[1])
            return country, percentage
            cursor.close()
