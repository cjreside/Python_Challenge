# Import the OS Module
import os

# Import Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables
num_rows = 0
months = []
ProfLoss = []
ProfChange = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies a delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Do not count the header
    header = next(csvreader)

# Use a For Loop to count the number of Rows
    for row in csvreader:
        num_rows += int(row[1])
        months.append(row[0])
        ProfLoss.append(row[1])

# Use a For Loop to determine your variables for the calculating Profit Changes, Total, Etc..
    for row in range(len(ProfLoss)-1):
        ProfChange.append(int(ProfLoss[row + 1])-int(ProfLoss[row]))
        maxprofchange = max(ProfChange)
        minprofchange = min(ProfChange)
        maxprof = ProfChange.index(max(ProfChange)) + 1
        minprof = ProfChange.index(min(ProfChange)) + 1

# Display the results for Total Number of Months, Total Profit/Loss, Average Profit/Loss, Greatest Increase and Decrease in Profits
    print('Financial Analysis')
    print('------------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${num_rows}')
    print(f'Average Change: ${round(sum(ProfChange)/len(ProfChange),2)}')
    print(f'Greatest Increase in Profits: {months[maxprof]} (${(str(maxprofchange))})')
    print(f'Greatest Decrease in Profits: {months[minprof]} (${(str(minprofchange))})')

# Export a text file with the results to the Analysis Directory
    os.chdir('Analysis')

    file = open('Financial_Analysis.txt', 'w')
    file.write('Financial Analysis' + '\n')
    file.write('------------------------------' + '\n')
    file.write(f'Total Months: {len(months)}' + '\n')
    file.write(f'Total: ${num_rows}' + '\n')
    file.write(f'Average Change: ${round(sum(ProfChange)/len(ProfChange),2)}' + '\n')
    file.write(f'Greatest Increase in Profits: {months[maxprof]} (${(str(maxprofchange))})' + '\n')
    file.write(f'Greatest Decrease in Profits: {months[minprof]} (${(str(minprofchange))})' + '\n')
    file.close()

 