import csv
import re
import os
import sys

filepath = input("Enter csv file path:")
with open(filepath, 'r') as f_read, open('output.csv', 'w', newline='') as f_write:
    writer = csv.writer(f_write, delimiter=',')
    for row in csv.reader(f_read):
        if row[25]:
            writer.writerow(row)