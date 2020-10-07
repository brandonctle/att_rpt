import csv
import os
import sys
import numpy
from datetime import datetime

def IsTask(num):
    try:
        int(num)
        if int(num) > 6 or int(num) < 1:
            return False
        return True
    except ValueError:
        return False

def Task1():
    customer_list, money_saved_list, correct_order = [], [], []

    for x in range(len(Customer_ID)):
        if Customer_ID[x] in customer_list:
            location = customer_list.index(Customer_ID[x])
            money_saved_list[location] = money_saved_list[location] + Money_Saved[x]
        else:
            customer_list.append(Customer_ID[x])
            money_saved_list.append(Money_Saved[x])

    money_order = numpy.argsort(money_saved_list)
    correct_money_order = money_order[::-1]
    correct_order = []

    for x in correct_money_order:
        correct_order.append(int(customer_list[x]))

    return correct_order


file = sys.argv[1]

while not os.path.exists(file):
    print("File Not Found! Please Try Again.")

#print("File Found!\n")

with open(file) as datafile:
    data = csv.DictReader(datafile, delimiter=",")
    Discount_Code, Customer_ID, Date, Discount, Amt_Bef_Discount = [], [], [], [], []

    for row in data:
        Discount_Code.append(row['Discount_Code'])
        Customer_ID.append(int(row['Customer_ID']))
        Date.append(row['Date(MM/DD/YYYY)'])
        Discount.append(float(row['Discount(%)']))
        Amt_Bef_Discount.append(float(row['Amt_Bef_Discount($)']))

values = [Discount_Code,Customer_ID,Date,Discount,Amt_Bef_Discount]

Money_Saved = []
Amt_Aft_Discount = []

for x in range(len(Discount_Code)):
    Money_Saved.append((float(Discount[x]) / 100) * float(Amt_Bef_Discount[x]))
    Amt_Aft_Discount.append(float(Amt_Bef_Discount[x]) - float(Money_Saved[x]))

values.append(Money_Saved)
values.append(Amt_Aft_Discount)
#print(values)

task_count = len(sys.argv)

final_output = []

for x in range(2, task_count):
    task = sys.argv[x]

    if not IsTask(task):
        print(task + " is an Invalid Task!!")
    else:
        #print(task)

        if task == '1':
            final_output.append(Task1())

        if task == '2':
            Correct_Order = Task1()
            Month_Order = []

            for i in Correct_Order:
                location = Customer_ID.index(i)
                full_format = Date[location]
                date_object = datetime.strptime(full_format, '%m/%d/%Y')
                new_format = date_object.strftime('%B %Y')
                Month_Order.append(new_format)

            final_output.append(Month_Order)

        if task == '3':
            highest_saving = 0.0

            for y in Money_Saved:
                if y > highest_saving:
                    highest_saving = y

            location = Money_Saved.index(highest_saving)
            final_output.append([Discount_Code[location]])

        if task == '4':
            month_list, month_value = [], []
            highest_grossing_value = 0
            highest_grossing_month = ''

            for z in range(len(Date)):
                if Date[z] in month_list:
                    location = month_list.index(Date[z])
                    month_value[location] = month_value[location] + Amt_Bef_Discount[z]
                else:
                    month_list.append(Date[z])
                    month_value.append(Amt_Bef_Discount[z])

            for i in month_value:
                if i > highest_grossing_value:
                    highest_grossing_value = i
                    highest_grossing_month = month_list[month_value.index(i)]

            date_object = datetime.strptime(highest_grossing_month, '%m/%d/%Y')
            hgm_formatted = [date_object.strftime('%B %Y')]

            final_output.append(hgm_formatted)

        if task == '5':
            discount_list, discount_postrev_value = [],[]
            highest_pdr_value = 0
            highest_pdr_ID = ''

            for j in range(len(Discount_Code)):
                if Discount_Code[j] in discount_list:
                    location = discount_list.index(Discount_Code[j])
                    discount_postrev_value[location] = discount_postrev_value[location] + Amt_Aft_Discount[j]
                else:
                    discount_list.append(Discount_Code[j])
                    discount_postrev_value.append(Amt_Aft_Discount[j])

            for i in discount_postrev_value:
                if i > highest_pdr_value:
                    highest_pdr_value = i
                    highest_pdr_ID = [discount_list[discount_postrev_value.index(i)]]

            final_output.append(highest_pdr_ID)

print(final_output)
