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

csvpath = os.path.join("..", "uo_bootcamp", "budget-data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

	total_months = sum(1 for row in csvreader)
	total_money
	average_change
	increase
	decrease


print("Financial Analysis")
print("----------------------------")
print("Total Months: " + total_months)
print("Total: " + total_money)
print("Average Change: " + average_change)
print("Greatest Increase in Profits: " + increase)
print("Greatest Decrease in Profits: " + decrease)


