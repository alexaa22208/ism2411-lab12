# Reflection

# 1) Excel allows people to sort, view and calculate data using spreadsheets. Python can be used to automate processes
# such as reading files, calculating totals and creating new files whereas Excel allows for easier viewing and manual 
# editing of data.

# 2) An append file could be used by a business to keep track of customers orders. This would allow new orders to be
# added to the file without previous orders being erased.

import csv

print("--- Exercise 2 ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

print("--- Exercise 3 ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(header)

    for row in reader:
        print(row)



print("--- Exercise 4 ---")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("--- Exercise 5 ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    rows_written = 0
    total_rows = 0

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                rows_written += 1

print(f"Rows written: {rows_written} out of {total_rows}")


print("--- Exercise 6 ---")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

# csv.reader uses column positions, while DictReader uses column names.
# DictReader is easier when working with CSV files that have clear headers.


print("--- Exercise 7 ---")

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


print("--- Exercise 8 ---")

from datetime import datetime

current_time = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f"{current_time} - Total revenue: ${total_revenue:.2f}\n")