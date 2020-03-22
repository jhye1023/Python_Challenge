import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

profit = []
monthly_changes = []
date = []


count = 0
total_profit = 0
total_change_profits = 0
previous_profit = 0



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

   #print(f"Header: {csv_header}")
    for row in csvreader:
       current_date = row[0]
       current_profit = int(row[1])
       date.append(current_date)
       profit.append(current_profit)    
       total_profit = total_profit + current_profit
       count = count + 1
       if len(profit) == 1:
           # First month to skip calcuration
           previous_profit = current_profit
           continue
       monthly_change_profits = current_profit - previous_profit
       monthly_changes.append(monthly_change_profits)
       total_change_profits = total_change_profits + monthly_change_profits
       average_change_profits = (total_change_profits/(len(profit) - 1))
       greatest_increase_profits = max(monthly_changes)
       greatest_decrease_profits = min(monthly_changes)
       increase_date = date[monthly_changes.index(greatest_increase_profits)]
       decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
       previous_profit = current_profit

  

    print("-----------------------------")
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Month: " + str(count))
    print("Total Profits: " + "$" + str(int(total_profit)))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ") ")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ") ")
    

with open('financial_analysis.txt','w') as text:
    text.write("-----------------------------\n")
    text.write("Financial Analysis"+ "\n")
    text.write("-----------------------------\n\n")
    text.write("Total Month: " + str(count) + "\n")
    text.write("Total Profits: " + "$" + str(int(total_profit)) + "\n")
    text.write("Average Change: " + "$" + str(int(average_change_profits)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n ")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n ")