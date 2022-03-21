#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The total number of votes each candidate won.
#4. The percentage of votes each candidate won.
#5. The winner of the election based on popular vote.
import csv
import os

#Assign a variab le for the file to load and the path
election_file = os.path.join('Resources','election_results.csv')
#Open the election results and read the file
with open(election_file) as election_data:
    
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
        #print(row[0])

election_results = os.path.join('analysis','election_analysis.txt')
with open(election_results,"w") as results_file:
    results_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")



