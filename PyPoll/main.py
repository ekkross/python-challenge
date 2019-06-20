# In this challenge, you are tasked with helping a small, rural town modernize its vote- counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by- one, but unfortunately, his concentration isn't what it used to be.)
# • You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# o The total number of votes cast
# o A complete list of candidates who received votes 
# o The percentage of votes each candidate won
# o The total number of votes each candidate won
# o The winner of the election based on popular vote.
# • As an example, your analysis should look similar to the one below:
# • Election Results
# • -------------------------
# • Total Votes: 3521001
# • -------------------------
# • Khan: 63.000% (2218231)
# • Correy: 20.000% (704200)
# • Li: 14.000% (492940)
# • O'Tooley: 3.000% (105630)
# • -------------------------
# • Winner: Khan
# • -------------------------
# • In addition, your final script should both print the analysis to the terminal and export a
# text file with the results.

import os
import csv

source_file = os.path.join("..", "election_data.csv")

outfile = os.path.join("..", "PyPoll.txt")

total_votes = 0
results = {}
with open(source_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        candidate = str(row[2])
        if candidate in results:
            results[candidate] = results[candidate] + 1   
        else:
            results[candidate] = 1

winner = max(results, key=results.get)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(sum(results.values() )))
print("-------------------------")

for key in results:
    print (key + ": " + str(round((results[key]/sum(results.values())) * 100 , 3 )) + "% (" + str(results[key]) + ")")

print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

with open(outfile,"w") as file:
    file.write("Election Results\n")
    file.write("\n-------------------------\n")
    file.write("Total Votes: " + str(sum(results.values())))
    file.write("\n-------------------------\n")

    for key in results:
        file.write(key + ": " + str(round((results[key]/sum(results.values())) * 100 , 3 )) + "% (" + str(results[key]) + ")")
        file.write("\n-------------------------\n")
        file.write("Winner: " + winner)
        file.write("\n-------------------------\n")
