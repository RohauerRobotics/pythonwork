# finding a number in a dictionary
import numpy as np
d = {"Dates": ["2020-06-08","2020-06-09","2020-06-10"]}

lst = d["Dates"]

find = "2020-06-09"

for x in (range(0,len(lst))):
    if lst[x] == find:
        print(x)
    else:
        print("not found")
