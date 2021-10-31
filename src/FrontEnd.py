from tkinter.constants import CENTER, LEFT, TOP
import tkinter as tk
from tkinter import Canvas, Text
import os


root = tk.Tk()
root.title('Fossil CO2 Emissions 2017')
root.geometry("700x700")
apps = []

canvas = tk.Canvas(root, height = 700, width = 700, bg ="#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
canvas2 = tk.Canvas(frame, height =150, width = 500)
canvas2.create_text(250,50, text="FOSSIL CO2 EMISSIONS 2017", fill ="black", font = ('Helvetica 18 bold'))
canvas2.create_text(250,100, text="""\n\nClick on a button to display the pie graph that represents the 
temperature differential from the baseline (0 Degree Celcius)""", fill ="black", font = ('Helvetica 10 italic'))
canvas2.pack(side=TOP,padx=10,pady=10)

xyplot = tk.Button(frame, text = "XY Plot", padx =205, pady=10, fg="white",bg="#263D42")
xyplot.pack(side=TOP, pady=30)

barChart = tk.Button(frame, text = "Bar Chart", padx =200, pady=10, fg="white",bg="#263D42")
barChart.pack(side=TOP,pady=30)

linearRegression = tk.Button(frame, text = "Linear Regression", padx =178, pady=10, fg="white",bg="#263D42")
linearRegression.pack(side=TOP,pady=30)

frame.place(relwidth=0.8, relheight =0.8,relx = 0.1, rely=0.1)




root.mainloop()

