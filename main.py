import os
import csv

csvpath = os.path.join(r"C:\Users\krcon\OneDrive\Documents\GitHub\Python-ChallengeLocal\PyBank\Resources.csv")

def variables():
    total_months = 0
    net_profit = 0
    profit_losses = 0
    intial = 0 
    total_change = []
    date = []
    for row in csvreader:
        total_months = total_months +1
        date.append(row[0])
        net_profit = net_profit + int(row[1])
        
        
        if total_months == 1:
            final = int(row[1])
            monthly_change = 0
            total_change.append(monthly_change)
            profit_losses = profit_losses + monthly_change
            intial = final

        else:
            
            final = int(row[1])
            monthly_change = final - intial
            total_change.append(monthly_change)
            profit_losses = profit_losses + monthly_change
            intial = final
    
    
    average_change = profit_losses/(len(total_change)-1)
    greatest_inc = max(total_change)
    inc_date = date[total_change.index(greatest_inc)]
    greatest_dec = min(total_change)
    dec_date = date[total_change.index(greatest_dec)]

    print(f'Total Months: {total_months}')
    print(f'Total: ${net_profit}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {inc_date} (${greatest_inc})')
    print(f'Greatest Decrease in Profits: {dec_date} (${greatest_dec})')
    output_file = os.path.join("analysis")
    with open(output_file, "w") as text:
        text.write(f"Financial Analysis \n")
        text.write(f'Total Months: {total_months}\n')
        text.write(f'Total: ${net_profit}\n')
        text.write(f'Average Change: ${average_change}\n')
        text.write(f'Greatest Increase in Profits: {inc_date} (${greatest_inc})\n')
        text.write(f'Greatest Decrease in Profits: {dec_date} (${greatest_dec})\n')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    variables()