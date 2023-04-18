import os
import csv 

budget_data = os.path.join("Resources", "budget_data.csv")

#Variables 
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
revenue_change_list = []
revenue_average = 0
dates = []
greatest_increase = ["", 0]
greatest_decrease = []


with open(budget_data) as csvfile: 
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
      
        total_months += 1 

        total_revenue = total_revenue + int(row["Profit/Losses"])
        revenue_change = int(row["Profit/Losses"])- previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]

    greatest_increase = max(total_revenue)
    greatest_index = total_revenue.index(greatest_increase)
    greatest_date = dates[greatest_index]

    greatest_decrease = max(total_revenue)
    worst_index = total_revenue.index(greatest_decrease)
    worst_date = dates[worst_index]
   

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total_Revenue: ${str(total_revenue)}")
print(f"Average Revenue Change:  {str(round(revenue_average,2))}")
print(f"Greatest Increase in Revenue:   %  (greatest_increase[0], greatest_increase[1])")
print(f"Greatest Decrease in Revenue:   % (greatest_decrease[0], greatest_decrease[1])")

output = open("output.txt", "w")
line1 = ("Financial Analysis")
line2 = ("---------------------")
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total_Revenue: ${str(total_revenue)}")
line5 = str(f"Average Revenue Change:   %{str(round(revenue_average,2))}")
line6 = str(f"Greatest Increase in Revenue:   %  (greatest_increase[0], greatest_increase[1])")
line7 = str(f"Greatest Decrease in Revenue:   %  (greatest_decrease[0], greatest_decrease[1])")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))




    