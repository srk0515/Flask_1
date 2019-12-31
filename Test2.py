import csv


with open('hazmat.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    #to skip heading
    next(csv_reader)

    for line in csv_reader:
        print(line[0])
        print(line[1])
        print(line)

