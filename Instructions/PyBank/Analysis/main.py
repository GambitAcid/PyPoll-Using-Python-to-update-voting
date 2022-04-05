# Dependencies // Importing the budget dataset
import os
import csv
import statistics

from numpy import average

# Specify the file to write to working directory with os library

csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open the file using "read" mode. 
with open(csvpath, 'r') as csvfile:

# Step 1 Initialize csv.reader // Read In CSV
    csv_reader = csv.reader(csvfile, delimiter=',')
#Extract and read the header row first
    csv_header = next(csv_reader)
	
# Step 2 Assign and Initialize months, profits, dates, counters and set previous month to 0 .

    months = []
    profits = [] 
    monthly_pl = []
    net_change_pl = 0
    previous_month = 0
    counter = 0 
    total_pls = 0 


#Step 3 Loop // Read through each row of data after the header in csv reader
#Step 3a.1 Row[0] : Row Index position of 0. Pulling date from 0 position.

#Step 3a.2  Append date to date lists. Use len function to return the total number of months included in the dataset
    for row in csv_reader:
        counter = counter + 1 
        months.append(row[0])
#Step 3b Profit and Loss Determine Loss From Month To Month over the entire period 
        profits.append(row[1])
        total_pls = total_pls + int(row[1])

#Step 3b.1 Pull profit and loss from each row, row [1]
#Step 3b.2 Subtract previous month from current month// tracking revenue
        current_month = int(row[1])
        if counter == 1: pass 
        else: 
            monthly_pl_tot = (current_month) - (previous_month)
            monthly_pl.append(monthly_pl_tot)
            net_change_pl = net_change_pl + monthly_pl_tot
        previous_month = current_month
    
#Step 4 Calculate Average of Changes 
        #aver_pl = sum(net_change_pl)/counter
    # for i in range(1, len(current_month)):
    #     net_change_pl.append(current_month[i] - current_month [i -1])
    #     aver_pl = round(statistics.mean(net_change_pl), 2)
    #     #net_change_pl = int(net_change_pl)

aver_pl = sum(monthly_pl) / (counter - 1)
    

#Step 5 The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#The net total amount of "Profit/Losses" over the entire period
        
    

greatest_inc = max(monthly_pl)
greatest_dec = min(monthly_pl)
greatest_in_mon = months[monthly_pl.index(greatest_inc)]
greatest_de_mon = months[monthly_pl.index(greatest_dec)]
print(monthly_pl)
print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(counter))
print("Total Profits: " + "$" + str(total_pls))
print("Average Change :" + "$" + str(aver_pl))
print("Greatest Increase In Profits: " + str(greatest_in_mon ) + " $" + str(greatest_inc))
print("Greatest Decrease In Profits: " + str(greatest_de_mon ) + " $" + str(greatest_dec))
print("--------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------------")
    text.write("\nTotal Months: " + str(counter))
    text.write("\nTotal Profits: " + "$" + str(total_pls))
    text.write("\nAverage Change :" + "$" + str(aver_pl))
    text.write("\nGreatest Increase In Profits: " + str(greatest_in_mon ) + " $" + str(greatest_inc))
    text.write("\nGreatest Decrease In Profits: " + str(greatest_de_mon ) + " $" + str(greatest_dec))
    text.write("\n------------------------")
