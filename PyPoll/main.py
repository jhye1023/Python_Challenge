import os
import csv

cvspath = os.path.join("Resources","election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent =[]

with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
         count = count + 1
         candidatelist.append(row[2])
    for x in set(candidatelist):
         unique_candidate.append(x)
         y = candidatelist.count(x)
         vote_count.append(y)
         z = round((y/count)*100,2)
         vote_percent.append(z)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]    

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + (str(vote_percent[i])) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


with open('financial_analysis.txt', 'w') as text:
    text.write("-------------------------\n")
    text.write("Election Results" + "\n")   
    text.write("-------------------------\n")
    text.write("Total Votes :" + str(count) + "\n")    
    text.write("-------------------------\n")
    for i in range(len(unique_candidate)):
        text.write(unique_candidate[i] + ": " + (str(vote_percent[i])) +"% (" + str(vote_count[i])+ ")\n")
    text.write("-------------------------\n")
    text.write("The winner is: " + winner)
    text.write("-------------------------\n")