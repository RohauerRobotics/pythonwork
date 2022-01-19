# Moment Arm Physics Simulation
# Only Runs in 2D to keep things simple
import csv
import numpy as np

def dictionary_inputs():
    len_list = []
    mass_list = []
    with open("model_inputs.csv", mode = "r" ) as file:
        info = csv.reader(file, delimiter = ",")
        for row in info:
            if row[0] != 'arm_lengths_milimeters':
                len_list.append(int(row[0]))
            else:
                pass
            if row[1] != 'arm_mass_grams':
                mass_list.append(int(row[1]))
            else:
                pass
            print(row[1])
    d = {'arm_lengths_milimeters': len_list,'arm_mass_grams': mass_list}
    return(d)

values = dictionary_inputs()
print(values)

def 
