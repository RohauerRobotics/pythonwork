# reading a csv file in python
import csv
import numpy as np

# defines a function w/ no entry
def csv_print():
    with open('stocks.csv', mode='r') as filename:
        stocks = csv.reader(filename, delimiter = ",")
        row_counter = 0
        for row in stocks:
            if row_counter == 0:
                print("Column names are", {", ".join(row)})
                row_counter += 1
            else:
                # Open:{row[1]}High:{row[2]}Low:{row[3]}Close:{row[4]}Adj Close:{row[5]}Volume:{row[6]}
                print("Date:",{row[0]})
                row_counter +=1

# defines a function w/ no entry
def csv_to_dict():
    # opens stock price list in read mode with name as file
    with open("stocks.csv", mode="r") as file:
        # separates the items by the comma
        info = csv.reader(file, delimiter = ",")
        # var definition for keeping track of the rows passed
        # set to zero for the starting row
        row_counter = 0
        # defines d as an empty library
        d = {}
        # cycles through rows in info
        for row in info:
            # at the first row
            if row_counter == 0:
                # cycles thru all of the items in each row
                for x in list(np.arange(0,len(row))):
                    # creates a name for each list held in the dictionary
                    d[row[x]] = []
                # adds one to the row counter to move to the second row
                row_counter += 1
            else:
                    # appends a string for every date in the row
                    d["Date"].append(row[0])
                    # cycles thru the dictionary lables and lists
                    for x,y in [("Open",1),("High",2),("Low",3),("Close",4),("Adj Close",5),("Volume",5)]:
                        # adds the value for each associated label as a float
                        d[x].append(float(row[y]))
                    # adds one to the row counter
                    row_counter += 1
        # returns the dictionary as a result
        return d

def find_date_info(d):
    year = input("Enter a year: ")
    month = input("Enter a month: ")
    day = input("Enter a day: ")
    compiled = str(year+"-"+month+"-"+day)
    dlist = d["Date"]
    print("Date entered: ", compiled)
    for x in range(0,len(dlist)):
        if dlist[x] == compiled:
            print("Length:", x)
            print("The Opening Price was:", d["Open"][x])
            print("The Closing Price was:", d["Close"][x])
        else:
            pass

test = csv_to_dict()

find_date_info(test)
