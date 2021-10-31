from tkinter.constants import CENTER, LEFT, TOP
import myParser
import temperature
import slope
import co2
import DataBase
import tkinter as tk
from tkinter import Canvas, Text
import os
import Graph
import BackEnd

#parse raw data from html file
rawParsedCo2 = myParser.myParser("Co2.html")
rawParsedTemp = myParser.myParser("Temperature.html")

#create containers to store processed raw data for temperature and Co2 file
tempObj = temperature.temperature(rawParsedTemp.getRawData())
co2Obj = co2.co2(rawParsedCo2.getRawData())

slopeObj = slope.slope(co2Obj.getCo2Dict(),tempObj.getTempDict())

dataBaseObj = DataBase.DataBase()
f = open("table.txt","a+")
f.seek(0)
if (f.read() == ""):
    f.close()
    dataBaseObj.createTable(tempObj.getTempData())

root = tk.Tk()
root.title('Temperature Differential GUI')
root.geometry("700x700")
apps = []

canvas = tk.Canvas(root, height = 700, width = 700, bg ="#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
canvas2 = tk.Canvas(frame, height =150, width = 500)
canvas2.create_text(250,50, text="TEMPERATURE GUI APP", fill ="black", font = ('Helvetica 18 bold'))
canvas2.create_text(250,100, text="""\n\nClick on a button to display a graph that represents the 
temperature differential from the baseline (0 Degree Celcius)""", fill ="black", font = ('Helvetica 10 italic'))
canvas2.pack(side=TOP,padx=10,pady=10)

xyplot = tk.Button(frame, text = "XY Plot", padx =205, pady=10, fg="white",bg="#263D42",command= BackEnd.xyPlot)
xyplot.pack(side=TOP, pady=30)

barChart = tk.Button(frame, text = "Bar Chart", padx =200, pady=10, fg="white",bg="#263D42", command = BackEnd.barChart)
barChart.pack(side=TOP,pady=30)

linearRegression = tk.Button(frame, text = "Linear Regression", padx =178, pady=10, fg="white",bg="#263D42",command = BackEnd.linearRegression)
linearRegression.pack(side=TOP,pady=30)

frame.place(relwidth=0.8, relheight =0.8,relx = 0.1, rely=0.1)




root.mainloop()

