
import csv
import os

#whats the best way to enter path?
file_to_load = os.path.join(r"C:\Users\krcon\OneDrive\Desktop\Git\PythonChallenge\PyPoll\election_data.csv")
file_to_save = os.path.join(r"C:\Users\krcon\OneDrive\Desktop\Git\PythonChallenge\PythonChallenge\PyPoll\Analysis.txt")

total_votes = 0

#Calling lists to capture data when reading through?
candidate_options = []
candidate_votes = {}

#keeping tab on total counts?
winning_candidate = ""
winning_count = 0

winning_percentage = 0


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
     #reading through each row?
    for row in reader:

        
        total_votes = total_votes + 1
        #print(total_votes)
        

        #defining what we need to capture?
        candidate_name = row[2]


        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
          
        #then add a vote count?   
        candidate_votes[candidate_name] += 1

     
with open(file_to_save, "w") as txt_file:
    election_results = (
       f"Election Results\n"
       f"Total Votes: {total_votes:,}\n" )
    print(election_results, end="")

    txt_file.write(election_results)

    #save the final candidate vote count to file.
    for candidate_name in candidate_votes:

        #retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #winner, winning candidate, percent
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #print winner
    winning_candidate_summary = (
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n" )
    print(winning_candidate_summary)

    #prite to file
    txt_file.write(winning_candidate_summary)