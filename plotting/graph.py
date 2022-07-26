#python function for plotting the data in csv_data
import os
import glob
import matplotlib.pyplot as plt
import pandas as pd
import csv   

directoryPath = os.path.join("c:\\","/Users/cpapalaz/dam-water-level/csv_data/")

#print csv files and choose

#extract date range and variable values for the csv file
for file in glob.glob(directoryPath+"*.csv"):
    f=open(file, "r")
    lines = f.readlines()[1:]
    reader = csv.reader(lines, delimiter=",")
    date_range =[]
    var_values = []
    for row in reader:
        date_range.append(row[0])
        var_values.append(row[1])  
    #plotting
    plt.plot(date_range, var_values) 

    plt.xlabel("Date")
    plt.ylabel(file[1])

    plt.xlim()
    plt.ylim()
    plt.title(file)

    plt.show()