import csv
import os
import numpy

def IsTask(num):
    try:
        int(num)
        if int(num) > 6 or int(num) < 1:
            return False
        return True
    except ValueError:
        return False


print("Hi! Welcome to the Reward Tracker Program.")

file = input("Please Enter the Path to the CSV file: ")

while not os.path.exists(file):
    print("File Not Found! Please Try Again.")
    file = input("Please Enter the Path to the CSV file: ")

print("File Found!\n")

with open(file) as datafile:
    data = csv.reader(datafile, delimiter=",")
    Discount_Code, Customer_ID, Date, Discount, Amt_Bef_Discount = [], [], [], [], []

    for row in data:
        Discount_Code.append(row[0])
        Customer_ID.append(row[1])
        Date.append(row[2])
        Discount.append(row[3])
        Amt_Bef_Discount.append(row[4])

values = [Discount_Code,Customer_ID,Date,Discount,Amt_Bef_Discount]

for x in values:
    x.pop(0)

Money_Saved = []
Amt_Aft_Discount = []

for x in range(len(Discount_Code)):
    Money_Saved.append((float(Discount[x]) / 100) * float(Amt_Bef_Discount[x]))
    Amt_Aft_Discount.append(float(Amt_Bef_Discount[x]) - float(Money_Saved[x]))

values.append(Money_Saved)
values.append(Amt_Aft_Discount)
print(values)

print("Tasks:\n1.Print the customer ID's in order of money saved.\n"
      "2.Print the month in descending order by discount savings.\n"
      "3.Print which Discount Code has saved customers the most money\n"
      "4.Print which month was the highest grossing month\n"
      "5.Print which Discount Code code yielded the most post discount revenue for the business.\n")

done = False
while not done:
    task = input("Please select which task you would like to execute.\n"
                 "(If you are done with the program, enter '6'.)\n")

    valid_num = IsTask(task)

    while not valid_num:
        print("Invalid value! Try Again:\n")
        task = input("Please select which task you would like to execute.\n"
                     "(If you are done with the program, enter '6'.)\n")
        valid_num = IsTask(task)

    task_num = int(task)

    if task_num == 6:
        done = True
        print("Goodbye!")

    if task_num == 1:
        money_order = numpy.argsort(Money_Saved)
        correct_money_order = money_order[::-1]
        customer_order = []
        print(correct_money_order)
        for x in correct_money_order:
            customer_order.append(Customer_ID[x])
        print(customer_order)

"""
    if task == 2:


    if task == 3:


    if task == 4:


    if task == 5:
"""



