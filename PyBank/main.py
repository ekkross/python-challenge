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

csvpath = os.path.join("..", "budget-data.csv")
outfile = os.path.join("..", "PyBank.txt")

monthly_changes = []
monthly_changes_for_month = []


with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    profit_by_month = dict(csvreader)

    profits = list(map(int, profit_by_month.values()))
    month_list = list(profit_by_month.keys())

    for i in range(len(profits) - 1):
        monthly_changes.append(profits[i + 1] - profits[i])
        monthly_changes_for_month.append(month_list[i])

    increase_profit = max(monthly_changes)
    increase_month_idx = monthly_changes.index(increase_profit)
    increase_month = month_list[increase_month_idx + 1]

    decrease_profit = max(monthly_changes)
    decrease_month_idx = monthly_changes.index(decrease_profit)
    decrease_month = month_list[decrease_month_idx + 1]

    total_months = str(len(profit_by_month))
    total_money = str(sum(profits))
    average_change = sum(monthly_changes)/len(monthly_changes)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(total_months))) 
print(f"Total: ${total_money}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits:: {increase_month} (${increase_profit})")
print(f"Greatest Decrease in Profits:: {decrease_month} (${decrease_profit})")

with open(outfile,"w") as file:
    file.write("Financial Analysis\n")
    file.write("________________________________________________\n")
    file.write("Total Months: " + str(len(total_months)))
    file.write("\n")
    file.write(f"Total: ${total_money}\n")
    file.write(f"Average Change: ${round(average_change,2)}\n")
    file.write(f"Greatest Increase in Profits:: {increase_month} (${increase_profit})\n")
    file.write(f"Greatest Decrease in Profits:: {decrease_month} (${decrease_profit})")
