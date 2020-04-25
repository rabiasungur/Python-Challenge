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
  
  for row in csvreader:
    total_votes = total_votes + 1
    
    row_candidate = row[2]
    candidates.append(row_candidate)
    

# * The total number of votes cast
print(f"Total Votes: {total_votes}")
print("-------------------------")

 # * A complete list of candidates who received votes
 # * The total number of votes each candidate won
 # * The percentage of votes each candidate won
 # * The winner of the election based on popular vote.

### To see the names of candidates
def candidate_names(candidates): 
  list_set = set(candidates)  
  candidates_list = (list(list_set)) 
  for x in candidates_list: 
    print(x)
#candidate_names(candidates)

c1 = candidates.count("Correy")
c2 = candidates.count("Khan")
c3 = candidates.count("Li")
c4 = candidates.count("O'Tooley")

p1 = c1/total_votes
p2 = c2/total_votes
p3 = c3/total_votes
p4 = c4/total_votes

print(f"Correy: {p1:.4%} ({c1})")
print(f"Khan: {p2:.4%} ({c2})")
print(f"Li: {p3:.4%} ({c3})")
print(f"O'Tooley: {p4:.4%} ({c4})")
print("-------------------------")
def winner(candidates): 
    return max(set(candidates), key = candidates.count) 
print(f"Winner: {winner(candidates)}")

output_pypoll = os.path.join("output.txt")
with open(output_pypoll, 'w') as txtfile:
  txtfile.write("Election Results")
  txtfile.write("\n-------------------------")
  txtfile.write(f"\nTotal Votes: {total_votes}")
  txtfile.write("\n-------------------------")
  txtfile.write(f"\nCorrey: {p1:.4%} ({c1})")
  txtfile.write(f"\nKhan: {p2:.4%} ({c2})")
  txtfile.write(f"\nLi: {p3:.4%} ({c3})")
  txtfile.write(f"\nO'Tooley: {p4:.4%} ({c4})")
  txtfile.write("\n-------------------------")
  txtfile.write(f"\nWinner: {winner(candidates)}")
 
  
  


###  with sort() ####
## votes = {}

## for candidate in candidates:
##  votes[candidate] = votes.get(candidate, 0) + 1
## sorted_candidates = sorted(votes, key=votes.get, reverse=True)
## for candidate in sorted_candidates:
## print("{0}: {1:.4%} ({2})".format(candidate, votes[candidate]/float(total_votes), votes[candidate]))
## print("-------------------------")  
## print("Winner: {}".format(sorted_candidates[0]))


###  with counter ####
### counter = collections.Counter(candidates)  
### print("Candidates Votes: " + str(counter))
### winner = counter.most_common(1)
### print("Winner: " + str(winner))

