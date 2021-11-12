from urllib.request import urlopen
from bs4 import BeautifulSoup
import Input
from collections import namedtuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Database
from tkinter import * 

class Graph:
    def __init__(self, country, percentage):
        self.country = country
        self.percentage = percentage

    def piechart(self):
        print(self.country)
        print(self.percentage)
        plt.pie(np.array(self.percentage),labels = np.array(self.country))
        plt.show()

class FrontEnd:
    def __init__(self):
        self.window = Tk() 
        self.window.title("CO2 file") 
        self.window.geometry('200x150') 
        self.lab = Label(self.window, text="Button Clicked") 
        self.lab.grid(column=0, row=0) 
    
    def calling_Piechart(self):
        Inputdata =  Input.input()
        data= Database.DataBase()
        data.connect()
        data.table()
        #use getlst() to insert data returned in Input.py
        data.insert(Inputdata.getlst())
        data.readTable()
        Plot=Graph(data.country,data.percentage)
        Plot.piechart()
    
    def clicked(self): 
        self.lab.configure(text="Select a Plot") 
        bot1 = Button(self.window, text="Pie Chart", fg='Green', command=self.calling_Piechart)
        bot1.grid(column=1, row=1) 
        self.window.mainloop() 



