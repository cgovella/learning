import shelve

# ID, Name, Description, OwnerID, Price, Condition, DateRegistered
items = [
['1','Lawnmower','Tool','1','$150','Excellent','2012-01-05'],
['2','Lawnmower','Tool','2','$370','Fair','2012-04-01'],
['3','Bike','Vehicle','3','$200','Good','2013-03-22'],
['4','Drill','Tool','4','$100','Good','2013-10-28'],
['5','Scarifier','Tool','5','$200','Average','2013-09-14'],
['6','Sprinkler','Tool','1','$80','Good','2014-01-06'] 
]

# ID, Name, Email
members = [
['1', 'Fred', 'fred@lendylib.org'],
['2', 'Mike', 'mike@gmail.com'],
['3', 'Joe', 'joe@joesmail.com'],
['4', 'Rob', 'rjb@somcorp.com'],
['5', 'Anne', 'annie@bigbiz.com'],
]

# ID, ItemID, BorrowerID, DateBorrowed, DateReturned
loans = [
['1','1','3','4/1/2012','4/26/2012'],
['2','2','5','9/5/2012','1/5/2013'],
['3','3','4','7/3/2013','7/22/2013'],
['4','4','1','11/19/2013','11/29/2013'],
['5','5','2','12/5/2013','None']
]

def createDB(data, shelfname):
    try:
       shelf = shelve.open(shelfname,'c')
       for datum in data:
           shelf[datum[0]] = datum
    finally:
       shelf.close()

def readDB(shelfname):
    try:
       shelf = shelve.open(shelfname,'r')
       return [shelf[key] for key in shelf]
    finally:
       shelf.close()

def main():
    print('Creating data files...')
    createDB(items, 'itemshelf')
    createDB(members, 'membershelf')
    createDB(loans, 'loanshelf')

    print('reading items...')
    print(readDB('itemshelf'))
    print('reading members...')
    print(readDB('membershelf'))
    print('reading loans...')
    print(readDB('loanshelf'))

if __name__ == "__main__": main()
