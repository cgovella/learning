import csv, datetime

def convertDate(item):
    theDate = item[-1]
    dateObj = datetime.strptime(theDate,'%Y-%m-%d')
    dateStr = datetime.strftime(dateObj,'%m/%d/%Y')
    item[-1] = dateStr
    return item

with open('tooldesc.csv') as td:
    rdr = csv.reader(td)
    items = list(rdr)

items = [convertDate(item) for item in items]

with open('tooldesc2.csv', 'w', newline='') as td:
    wrt = csv.writer(td)
    for item in items:
        wrt.writerow(item)
