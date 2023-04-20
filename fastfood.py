import csv
with open('fastfood.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        print(row)

