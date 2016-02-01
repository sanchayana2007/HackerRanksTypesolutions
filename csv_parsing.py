__author__ = 'Sanchayan'
import csv


if __name__=="__main__":

    with open('Excel.csv', 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        for row in reader:
            print (row[0])

