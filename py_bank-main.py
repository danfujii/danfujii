import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
 
    months = []
    profit_loss = []
    differences = []
    greatest_increase_date = ""
    greatest_decrease_date = ""
    
    for row in csvreader:
        months.append(row[0])   
        profit_loss.append(int(row[1]))
      
    
    print("Financial Analysis\n"
        "----------------------------")
    print(f"Total Months: {len(months)}\n"
    f"Total: $ {sum(profit_loss)}")
    

    for i in range(1, len(profit_loss)):
        
        differences.append(profit_loss[i] - profit_loss[i-1])
        
        avg_change = sum(differences) / len(differences)
        
        greatest_increase = max(differences)
        greatest_increase_date = str(months[differences.index(max(differences))])
        
        greatest_decrease = min(differences)
        greatest_decrease_date = str(months[differences.index(min(differences))])
  
    print(f"Average Change: $ {round(avg_change,2)}")  
    print(f"Greatest Increase in Profits: $ {greatest_increase_date} $ {greatest_increase}")
    print(f"Greatest Decrease in Profits: $ {greatest_decrease_date} $ {greatest_decrease}")


text_file = open("bank_summary.txt", "w")
text_file.write("Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {len(months)}\n"
        f"Total: $ {sum(profit_loss)}\n"
        f"Average Change: $ {round(avg_change,2)}\n"
        f"Greatest Increase in Profits: $ {greatest_increase_date} $ {greatest_increase}\n"
        f"Greatest Decrease in Profits: $ {greatest_decrease_date} $ {greatest_decrease}")
text_file.close()