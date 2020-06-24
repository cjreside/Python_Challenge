# Import the OS Module
import os

# Import Module for reading CSV files
import csv

# Variables
votes = 0   
candidate_specific = []
candidate_votes = []
election_data = ['1', ]

# Start a For Loop through the file
for files in election_data:
    election_datacsv = csvpath = os.path.join('Resources', 'election_data.csv')
# Read the CSV file
    with open(election_datacsv) as csvfile:

# CSV reader specifies a delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
# Do not count the header
        line = next(csvreader, None)

# Use a Nested For Loop
        for line in csvreader:
# Establish the vote count
            votes = votes + 1
# Establish the candidate
            candidate_x = line[2]
# Add Votes to Candidates
            if candidate_x in candidate_specific:
                candidate_index = candidate_specific.index(candidate_x)
                candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
# Make a Spot for the Candidate in the list
            else:
                candidate_specific.append(candidate_x)
                candidate_votes.append(1)
# Declare additional variables
    percent = []
    max_votes = candidate_votes[0]
    max_index = 0       
# Calculate Percentages and Winner
    for count in range(len(candidate_specific)):
        vote_percent = (candidate_votes[count]/votes)*100 
        percent.append(vote_percent)
    
        if candidate_votes[count] > max_votes:
            max_votes = candidate_votes[count]
            print(max_votes)
            max_index = count

    winner = candidate_specific[max_index] 
# Round the Percentages
    percent = [round(i,2) for i in percent]

    print('Election Results')
    print('-----------------------')
    print(f'Total Votes: {votes}')
    print('-----------------------')
    for count in range(len(candidate_specific)):
        print(f'{candidate_specific[count]} : {percent[count]}% ({candidate_votes[count]})')
    print('-----------------------')
    print(f'Winner: {winner}')  
    print('-----------------------')    

# Export as text file
    os.chdir('Analysis')

    file = open('Election_Results.txt', 'w')
    file.write('Election Results' + '\n')
    file.write('---------------------------' + '\n')
    file.write(f'Total Votes: {votes}' + '\n')
    file.write('---------------------------' + '\n')
    for count in range(len(candidate_specific)):
        file.write(f'{candidate_specific[count]} : {percent[count]}% ({candidate_votes[count]})' + '\n')
    file.write('-----------------------' + '\n')
    file.write(f'Winner: {winner}' + '\n')
    file.write('-----------------------')
    file.close()
