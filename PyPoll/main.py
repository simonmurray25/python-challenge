import os
import csv

total_votes = 0
candidates = []
winning_candidate = ""
winning_count = 0
winning_percentage = 0
candidate_votes = {}

csvpath = os.path.join("..","Resources","election_data.csv")
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_reader = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

output_file = os.path.join("output.txt")
with open(output_file, "w") as file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results) 


    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes:,})\n")
        print(candidate_results)

        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage


    print(f"---------------------\n")
    print(f"Winner: {winning_candidate}\n")
    print(f"Winning Percentage: {winning_percentage:.1f}%\n")
    print(f"-----------------------\n")



    # write the file 
    file.write(election_results)
    file.write(candidate_results)
    file.write(f"---------------------\n")
    file.write(f"Winner: {winning_candidate}\n")
    file.write(f"Winning Percentage: {winning_percentage:.1f}%\n")
    file.write(f"-----------------------\n")
    
        


