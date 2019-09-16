import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")


with open(bank_csv, newline='') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=',')
#    print(bank_data)
    next(bank_data, None)

    months = sum((1 for row in bank_data))

    print("Financial Analysis\n"
        "----------------------------")

    print(f"Total Months: {months}")

with open(bank_csv, newline='') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=',')
    next(bank_data, None)    

    total = sum(int(row[1]) for row in bank_data)

    print(f"Total: $ {total}")

with open(bank_csv, newline='') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=',')
    next(bank_data, None)

    avg_change = total / months

    print(f"Average Change: $ {avg_change}")

with open(bank_csv, newline='') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=',')
    next(bank_data, None)
    max_profits = max(row[1] for row in bank_data)

    print(f"Greatest Increase in Profits: $ {max_profits}")    

with open(bank_csv, newline='') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=',')
    next(bank_data, None)

    min_profits = min(row[1] for row in bank_data)

    print(f"Greatest Decrease in Profits: $ {min_profits}")




#with open(bank_csv, newline='') as csvfile:
#    bank_data = csv.reader(csvfile, delimiter=',')
#    next(bank_data, None)

 #   change_rev = (int(row[1][1]) for row in bank_data)

  #  avg_change = change_rev / months

   # print(f"Average Change: $ {avg_change}")

text_file = open("bank_summary.txt", "w")
text_file.write("Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {months}\n"
        f"Total: $ {total}\n"
        f"Average Change: $ {avg_change}\n"
        f"Greatest Increase in Profits: $ {max_profits}\n"
        f"Greatest Decrease in Profits: $ {min_profits}")
text_file.close()