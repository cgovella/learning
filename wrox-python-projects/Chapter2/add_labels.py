import csv

fields = ['ItemID', 'Name', 'Description', 'Owner',
          'Price', 'Condition', 'DateRegistered']

with open('tooldesc2.csv') as td_in:
    rdr = csv.DictReader(td_in, fieldnames = fields)
    items = [item for item in rdr]

with open('tooldesc3.csv', 'w', newline='') as td_out:
    wrt = csv.DictWriter(td_out, fieldnames=fields)
    wrt.writeheader()
    wrt.writerows(items)


        