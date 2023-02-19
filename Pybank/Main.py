# File creation
import os

# Reading the CSV file
import csv

# Setting path
filepath = os.path.join('.','Resources','budget_data.csv')

# Creating list 
budget_data = []

# Opening the CSV
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

#Storing in  a dictionary
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": 
		int(row["Profit/Losses"]),"change": 0})

#  total months
total_months = len(budget_data)

# changes between months
previous_amount = budget_data[0]["amount"]
for i in range(total_months):
 	 budget_data[i]["change"] = budget_data[i]["amount"] - previous_amount
prev_amount = budget_data[i]["amount"]

# total amount
total_amount = sum(row['amount'] for row in budget_data) 

#average of  changes
total_change = sum(row['change'] for row in budget_data)
average = round(total_change / (total_months-1), 2)

#Increase and Decrease from the changes
get_increase = max(budget_data, key=lambda x:x['change'])
get_decrease = min(budget_data, key=lambda x:x['change'])

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})')
print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})')


# Exporting to a text file 
# Setting path
filepath = os.path.join('PyBank_Results.txt')
with open(filepath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('-----------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_amount}', file=text_file)
    print(f'Average Change: ${average}', file=text_file)
    print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})', file=text_file)
    print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})', file=text_file)
