import os
import csv

#Declare variables
candidates = []
uniqueCandidates = []

#Open election_data.csv as long as election_data is in the same folder as this file
path = os.path.join(".","election_data.csv")
with open(path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    #Iterate through the entire list, determine total num votes and all unique candidates
    for row in csvreader:
        candidates.append(row[2])
        if(row[2] not in uniqueCandidates):
            uniqueCandidates.append(row[2])

#Create a list of vote counts 
voteCount = []
for names in uniqueCandidates:
    voteCount.append(candidates.count(names))

#Print Election Results total vote count
print("Election Results\n-------------------------")
print(f"Total Votes: {len(candidates)}\n-------------------------")

#For each unique candidate, calculate the percentage of votes and print number of votes
for item in uniqueCandidates:
    print(f'''{item}: {"{0:.3f}".format((candidates.count(item)/len(candidates))*100)} ({candidates.count(item)}) ''')

#Find out what the max votes is and pass the index back to unique candidates and return the winning candidate
print("-------------------------")
print(f"Winner: {uniqueCandidates[voteCount.index(max(voteCount))]}")
print("-------------------------")


#create budgetDataOutput.csv which contains the above information printed to the terminal
with open("electionDataOutput.txt","w") as output:
    output.write("")
    output.write("Election Results\n-------------------------\n")
    output.write(f"Total Votes: {len(candidates)}\n-------------------------\n")

    for item in uniqueCandidates:
        output.write(f'''{item}: {"{0:.3f}".format((candidates.count(item)/len(candidates))*100)} ({candidates.count(item)}) \n''')

    output.write("-------------------------\n")
    output.write(f"Winner: {uniqueCandidates[voteCount.index(max(voteCount))]}\n")
    output.write("-------------------------")