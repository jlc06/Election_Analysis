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
election_results = os.path.join('analysis','election_analysis.txt')
#Initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file
with open(election_file) as election_data:
    
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open(election_results,"w") as results_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results,end="")
    results_file.write(election_results)

    for candidate in candidate_options:
        votes = candidate_votes[candidate]
        vote_percentage = (float(votes) / float(total_votes)) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        results_file.write(candidate_results)
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    results_file.write(winning_candidate_summary)
              

#print(total_votes)
#print(candidate_votes)



