print("Financial Analysis")
print("------------------------") 
  # Read budget_data.csv

import os

import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
with open(csvpath) as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  firstrow = next(csvreader)
  months = 0
  total = 0
  total_change = 0
  pre_profitloss = 867884
  months_list = []
  profitloss_changes = []

  for row in csvreader:

    months = months + 1
    months_list.append(row[0])

    profitloss = int(row[1])
    total = total + profitloss

    current_profitloss = int(row[1])
    change = current_profitloss - pre_profitloss
    profitloss_changes.append(change)
    total_change = total_change + change 
    pre_profitloss = current_profitloss
    #ave_change = total_change/(months-1)

    greatest_increase = max(profitloss_changes)
    greatest_decrease = min(profitloss_changes)

    increase_date = months_list[profitloss_changes.index(greatest_increase)]
    decrease_date = months_list[profitloss_changes.index(greatest_decrease)]

    
    
  # The total number of months included in the dataset
  print(f"Total Months: {months}")
    
  # The net total amount of "Profit/Losses" over the entire period
  print(f"Total: $ {total}")

  # The average of the changes in "Profit/Losses" over the entire period
  print(f"Average  Change: $ {total_change/(months-1)}")

  # The greatest increase in profits (date and amount) over the entire period
  print(f"Greatest increase: {str(increase_date)} $ {greatest_increase}")


  # The greatest decrease in losses (date and amount) over the entire period
  print(f"Greatest decrease: {str(decrease_date)} $ {greatest_decrease}")

output_file = os.path.join("output.txt")