# Your task is to create a Python script that analyzes the records to calculate each of the following:
# o The total number of months included in the dataset
# o The net total amount of "Profit/Losses" over the entire period
# o The average of the changes in "Profit/Losses" over the entire period
# o The greatest increase in profits (date and amount) over the entire period 
# o The greatest decrease in losses (date and amount) over the entire period
# • As an example, your analysis should look similar to the one below:
# • Financial Analysis
# • ----------------------------
# • Total Months: 86
# • Total: $38382578
# • Average Change: $-2315.12
# • Greatest Increase in Profits: Feb-2012 ($1926159)
# • Greatest Decrease in Profits: Sep-2013 ($-2196167)
# • In addition, your final script should both print the analysis to the terminal and export a
# text file with the results.

import os
import csv

csvpath = os.path.join("..", "Resources", "budget-data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

print("Financial Analysis")
print("----------------------------")


