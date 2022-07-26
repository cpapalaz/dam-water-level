# test code for graphing one of the csv datasets

import os
import matplotlib.pyplot as plt
import pandas as pd
import csv   

directoryPath = os.path.join("c:\\","/Users/cpapalaz/dam-water-level/csv_data/discharge_powergen_daily.csv")

f=open(directoryPath, "r")
lines = f.readlines()[1:] #skip column headers
reader = csv.reader(lines, delimiter=",") 
date_range =[]
var_values = []
for row in reader:
    date_range.append(row[0])
    var_values.append(row[1])  

date_range.pop() #remove last item as no data for current day/month
var_values.pop()

var_values_int =[]
for val in var_values:
    val= int(val.replace(',', '')) #convert data to int from string, ignore numerical commas
    var_values_int.append(val)

#plotting
plt.bar(date_range, var_values_int)

plt.xlabel("Month")
plt.ylabel("pwr discharge")

plt.title("Discharge Power Daily")

# plt.show()

#table
data = pd.read_csv(r"/Users/cpapalaz/dam-water-level/csv_data/discharge_powergen_daily.csv")
df = pd.DataFrame(data)

print (df)