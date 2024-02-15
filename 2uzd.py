import csv

with open('fails.csv', 'r') as file:
    teksts = csv.reader(file)
    
    next(teksts)
    
    for row in teksts:
        print(row[3])