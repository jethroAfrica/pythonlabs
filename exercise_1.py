import csv
with open('https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)