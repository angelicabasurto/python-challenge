import os
import csv 

budget_data = os.path.join("budget_data.csv")
text_path = "output.txt" 

#Variables 
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0

with open('budget_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        total_months += 1 

        total_revenue = total_revenue + int(row["1"])

        previous_revenue = float(row["1"])
        revenue_change = float(row["1"])- previous_revenue
        month_of_change = [month_of_change] + [row["Date"]]
        revenue_change_list = revenue_change_list + [revenue_change]



