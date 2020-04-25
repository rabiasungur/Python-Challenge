print("Election Results")
print("-------------------------")

import os
import csv
#import collections

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')
with open(csvpath) as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  firstrow = next(csvreader)
  total_votes = 0
  candidates = []
  candidate_votes = []
  
  for row in csvreader:
    total_votes = total_votes + 1
    
    row_candidate = row[2]
    candidates.append(row_candidate)
    

# * The total number of votes cast
print(f"Total Votes: {total_votes}")
print("-------------------------")

  # * A complete list of candidates who received votes
  ### To see the names of candidates
def candidate_names(candidates): 
  list_set = set(candidates)  
  candidates_list = (list(list_set)) 
  for x in candidates_list: 
    print(x)
#candidate_names(candidates)
      

  # * The total number of votes each candidate won
c1 = candidates.count("Correy")
c2 = candidates.count("Khan")
c3 = candidates.count("Li")
c4 = candidates.count("O'Tooley")

# * The percentage of votes each candidate won
p1 = c1/total_votes*100
p2 = c2/total_votes*100
p3 = c3/total_votes*100
p4 = c4/total_votes*100

print(f"Correy: %{p1} ({c1})")
print(f"Khan: %{p2} ({c2})")
print(f"Li: %{p3} ({c3})")
print(f"O'Tooley: %{p4} ({c4})")
print("-------------------------")

  # * The winner of the election based on popular vote.
def winner(candidates): 
    return max(set(candidates), key = candidates.count) 
print(f"Winner: {winner(candidates)}")

#counter = collections.Counter(candidates)  
#print("Candidates Votes: " + str(counter))
#winner = counter.most_common(1)
#print("Winner: " + str(winner))

output_file = os.path.join("output.txt")