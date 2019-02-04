import os
import csv

#Declare Variables
numMonths = 0
netRevenue = 0

#prevMonthRev and change are used to determine the change between months
prevMonthRev = 0
change = []
grProf = 0
grProfDate = ""
grLoss = 0
grLossDate = ""

#Read budget_data.csv notebook as long as budget_data is in the same directory.
path = os.path.join(".","budget_data.csv")
with open(path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        numMonths = numMonths + 1
        netRevenue = netRevenue + int(row[1])
        change.append(int(row[1])-prevMonthRev)
        prevMonthRev = int(row[1])
        if(int(row[1]) > int(grProf)):
            grProf = row[1]
            grProfDate = row[0]
        if(int(row[1]) < int(grLoss)):
            grLoss = row[1]
            grLossDate = row[0]
        
#remove the first item in the change list because it is the difference between 0 and the first month
change.remove(change[0])

#print requested outputs to terminal
print(f"Total Months: {numMonths}")
print(f"Total: {netRevenue}")
print(f"Average Change: {(sum(change)/len(change)):.2f}")
print(f"Greatest Increase in Profits: {grProfDate} ({grProf})")
print(f"Greatest Decrease in Profits: {grLossDate} ({grLoss})")

#create budgetDataOutput.csv which contains the above information printed to the terminal
with open("budgetDataOutput.txt","w") as output:
    output.write("Below is the Budget Data Output for budget_data.csv:\n")
    output.write(f"Total Months: {numMonths}\n")
    output.write(f"Total: {netRevenue}\n")
    output.write(f"Average Change: {(sum(change)/len(change)):.2f}\n")
    output.write(f"Greatest Increase in Profits: {grProfDate} ({grProf})\n")
    output.write(f"Greatest Decrease in Profits: {grLossDate} ({grLoss})")
    output.close()