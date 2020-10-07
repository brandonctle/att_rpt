# Rewards Program Tracking
AT&amp;T Challenge: Rewards Program Tracking

### *This Program was created in its entirety by Brandon Le, October 2020*

The purpose of this Python3 prgram is to read a CSV file, and return a set of values based on a selected query.

### Tasks:
1. Print the customer ID's in order of money saved. (Return List)
2. Print the month in descending order by discount savings. (Return List)
3. Print which Discount Code has saved customers the most money (Return string)
4. Print which month was the highest grossing month (Return String)
5. Print which Discount Code code yielded the most post discount revenue for the business. (Return String)

The program will read 2 arguments:
1. Path to the CSV file.
2. Number corresponding to the task performed.

As many tasks can be calculated at once.

# Underlying Assumptions
We assume that the CSV file headers are uniform (Discount_Code, Customer_ID, etc.).

# Input Processing
To run the program, the following command needs to be run from the command line, in the same directory as the program.
```
python reward_tracker.py <csv file path> <task> <task> <task>
```
For example, if we have a CSV file in the "data" folder, titled "june_data.csv", and we wanted to view tasks 2, 3, and 4, we would input:
```
python reward_tracker.py ./data/june_data.csv 2 3 4
```

# Data Validation
The program is designed to recognize and handle input errors, particularly regarding a path to a file which doesn't exist.
* If the user directs a path that doesn't exist, the program will reply "File not Found!" and exit the program.
* If numbers are inputted outside the task scope (1 - 5), they will simply be ignored.

# Output
The output will be in a nested list, in the order the task was called. For example, if the tasks 1, 3, and 2 were inputted:
``` [[<task 1 result>], [<task 3 result>], [<task 2 result>]] ```

# Required Dependencies - Imports
* **Python (3.8)**
* **Numpy** - this can be installed through running `python pip install numpy`, and helps with list sorting.
* **csv** - this is a built in library module with Python, and requires no installation
* **datetime** - this is another built in library module used to properly format the month ouput.
