from tkinter.constants import CENTER, LEFT, TOP
import tkinter as tk
from tkinter import Canvas, Text
import os
import graph

root = tk.Tk()
root.title('Fossil CO2 Emissions 2017')
root.geometry("700x700")
apps = []

canvas = tk.Canvas(root, height = 700, width = 700, bg ="#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
canvas2 = tk.Canvas(frame, height =150, width = 500)
canvas2.create_text(250,50, text="FOSSIL CO2 EMISSIONS 2017", fill ="black", font = ('Helvetica 18 bold'))
canvas2.create_text(250,100, text="""\n\nClick on the button to display the pie graph that represents the 
top 10 countries emitting the most amount of CO2 in 2017""", fill ="black", font = ('Helvetica 10 italic'))
canvas2.pack(side=TOP,padx=10,pady=10)

pieChart = tk.Button(frame, text = "Pie Chart", padx =205, pady=10, fg="white",bg="#263D42", command = graph.showPieChart)
pieChart.pack(side=TOP, pady=120)

frame.place(relwidth=0.8, relheight =0.8,relx = 0.1, rely=0.1)

root.mainloop()

