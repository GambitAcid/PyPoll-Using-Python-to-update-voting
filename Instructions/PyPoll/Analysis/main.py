# Dependencies // Importing the election dataset
import os
import csv

# Specify the file to write to working directory 

csvpath = os.path.join("..", "Resources", "election_data.csv")

#Assign and Initialize Variables Total Vote Counter
total_votes = 0 

#Assigning all candidates name and associated votes they received 
candidate_lists = []
candidate_votes = {}
# Variables for the winning candidate / Candidate is empty string to winner and count to votes
candidate_winner= ""
winner_counter = 0

# Open the file using "read" mode. 
with open(csvpath) as csvfile:

# Step 1 Initialize csv.reader // Read In CSV convert to list of dict
    csv_reader = csv.DictReader(csvfile)

# A complete list of candidates who received vote then trying to convert to a list 
    for row in csv_reader:
    #Adding to the total amount of the votes 
        total_votes = total_votes + 1 
    #Getting each candidates name from row 
        candidate_name = row['Candidate']
        #print(candidate_name)
        #If statement that says IF we find a new candidate thats not already in lists
        if candidate_name not in candidate_lists:
            #Add to new list of candidates running
            candidate_lists.append(candidate_name)
            #Look through that candidates lists and count votes// setting up to have a vote count 
            candidate_votes[candidate_name] = 0
        #Adding votes to running count 
        candidate_votes[candidate_name] = candidate_votes[candidate_name]  + 1 

# #Printing Results 
# print("Election Results")
# print("--------------------")
# print("Total Votes: " + str(total_votes))
# print("--------------------") 


# Predicting the winner for candidate in candidate_votes with a for loop:
# The percentage of votes each candidate won
print("Election Results")
print("--------------------")
print("Total Votes: " + str(total_votes))

with open('Election_Results.txt', 'w') as text:
    Election_Result = f"\nElection Results\n\ntotal_votes{total_votes}\n"
    text.write(Election_Result)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        votes_percent = float(votes) / float(total_votes) * 100

        #The total number of votes each candidate won
        if (votes > winner_counter):
            winner_counter = votes
            candidate_winner = candidate

        #Print the winner of the election based on popular vote:

        summary = f"{candidate}: {votes_percent:.1f}% ({votes})\n"
        text.write(summary)

        print("--------------------") 
        print(summary)
        print("--------------------") 
    print("Winner: " + str(candidate_winner) + " " + str(votes_percent) + " %") 
    print("--------------------") 
    text.write(candidate_winner)


    # with open('Election_Results.txt', 'w') as text:
    # text.write("Election Results\n")
    # text.write("\n--------------------")
    # text.write("\nTotal Votes: " + str(total_votes))
    # text.write("\n--------------------")
    # text.write(summary)
    # text.write("\n--------------------")
    # text.write("\nWinner: " + str(candidate_winner) + " " + str(votes_percent) + " %")
    # text.write("\n--------------------") 



