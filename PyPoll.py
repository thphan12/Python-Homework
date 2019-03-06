import os
print(os.getcwd())
import csv
file_path ="./Instructions/PyPoll/Resources/election_data.csv"

total_votes = 0
percentage_vote = 0
candidates = 0
candidate_votes = 0
winner = []
Khan_vote = 0
Li_vote= 0
Correy_vote = 0
OTooley_vote = 0

with open(file_path, "r") as infile:
    csvdata = csv.reader(infile, delimiter=",")
    csv_header = next(infile)
    for row in csvdata:
        total_votes = total_votes + 1
        # Khan= enumerate(re.finditer(Khan))
        if row[2]=="Khan": 
            Khan_vote=Khan_vote + 1
        if row[2]=="Li":
            Li_vote=Li_vote + 1
        if row[2]== "Correy":
            Correy_vote=Correy_vote + 1
        if row[2] == "O'Tooley":
            OTooley_vote=OTooley_vote + 1
    winner_count=[Khan_vote,Correy_vote,Li_vote,OTooley_vote]
    winner_name=["Khan", "Correy","Li", "O'Tooley"]
    winner = str(winner_name[winner_count.index(max(winner_count))])

    Khan_percent=round((Khan_vote/total_votes)*100,2)
    Li_percent = round((Li_vote/total_votes)*100,2)
    Correy_percent = round((Correy_vote/total_votes)*100,2)
    OTooley_percent = round((OTooley_vote/total_votes)*100,2)
  
print(f"Election Results: {total_votes}")
print("-----------------------------------------")
print(f"Khan: {Khan_vote}, {Khan_percent}")
print(f"Correy: {Correy_vote}, {Correy_percent}")
print(f"Li: {Li_vote},{Li_percent}")
print(f"OTooley: {OTooley_vote},{OTooley_percent}")
print("-----------------------------------------")
print(f"Winner:{winner}")

