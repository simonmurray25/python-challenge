import os
import csv

total_months = []
total_profits = []
monthly_changes = []
greatest_increase = ["",0]
greatest_decrease = ["",999999999999]
dates = []

csvpath = os.path.join("..","Resources","budget_data.csv")
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_reader = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])


        total_profits.append(int(row[1]))
        #total_profits = [int(x) for x in total_profits]
        net_profit = sum(total_profits)
        dates.append(row[0])

    for profit in range(len(total_profits)-1):
        monthly_changes.append(int(total_profits[profit+1]-total_profits[profit]))

        #monthly_changes = [int(i) for i in monthly_changes]
        #average_change = format(sum(monthly_changes)/len(monthly_changes),".2f")
        #average_change = format(average_change,".2f")

        for j in monthly_changes:
            if j > greatest_increase[1]:
                greatest_increase[1] = j
                greatest_increase[0] = row[0]
        for k in monthly_changes:
            if k < greatest_decrease[1]:
                greatest_decrease[1] = k
                greatest_decrease[0] = row[0]
index_gi = monthly_changes.index(greatest_increase[1])
index_gd = monthly_changes.index(greatest_decrease[1])
dates[index_gi]
dates[index_gd]
total_months = len(total_months)
average_change = format(sum(monthly_changes)/len(monthly_changes),".2f")

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_profit}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {dates[index_gi]} {greatest_increase[1]}")
print(f"Greatest Decrease in Profits: {dates[index_gd]} {greatest_decrease[1]}")

output_file = os.path.join("output.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: {net_profit}\n")
    file.write(f"Average Change: {average_change}\n")
    file.write(f"Greatest Increase in Profits: {dates[index_gi]} {greatest_increase[1]}\n")
    file.write(f"Greatest Decrease in Profits: {dates[index_gd]} {greatest_decrease[1]}")
