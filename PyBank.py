import os
print(os.getcwd())
import csv
file_path ="./Instructions/PyBank/Resources/budget_data.csv"
data=[]
total_months= 0
total_revenue = 0
prev_revenue= 0
average_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
revenue_changes = []
date = []

with open(file_path, "r") as infile:
    csvdata = csv.reader(infile, delimiter=",")
    csv_header = next(infile)
    print(f"header: {csvdata}")
    for row in csvdata:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        revenue_change = int(row[1])-prev_revenue
        previous_revenue = int(row[1])
        revenue_changes.append(revenue_change)
        # date_val=(row[0])
        date.append(row[0])

greatest_decrease = min(revenue_changes) 
greatest_increase = max(revenue_changes)
average_revenue = sum(revenue_changes)/len(revenue_changes)

maxChangeDate = str(date[revenue_changes.index(max(revenue_changes))+1])
minChangeDate = str(date[revenue_changes.index(min(revenue_changes))+1])

print(f"Total Months: {total_months}")
print(f"Total Profit: {total_revenue}")
print(f"Average change: {average_revenue}")
print(f"Greatest Increase in Profits: {greatest_increase}, {maxChangeDate}")
print(f"Greatest Decrease in Profits: {greatest_decrease},{minChangeDate}")