import sqlite3

members = [
   ['Fred', 'fred@lendylib.org'],
   ['Mike', 'mike@gmail.com'],
   ['Joe', 'joe@joesmail.com'],
   ['Rob', 'rjb@somcorp.com'],
   ['Anne', 'annie@bigbiz.com'],
]
member_sql = '''insert into member (Name, Email) values (?, ?)'''

items = [
   ['Lawnmower','Tool',    0, 150,'Excellent', '2012-01-05'],
   ['Lawnmower','Tool',    0, 370,'Fair',      '2012-04-01'],
   ['Bike',     'Vehicle', 0, 200,'Good',      '2013-03-22'],
   ['Drill',    'Tool',    0, 100,'Good',      '2013-10-28'],
   ['Scarifier','Tool',    0, 200,'Average',   '2013-09-14'],
   ['Sprinkler','Tool',    0,  80,'Good',      '2014-01-06'] 
]
item_sql = '''
insert into item 
(Name, Description, ownerID, Price, Condition, DateRegistered) 
values (?, ?, ?, ?, ?, date(?))'''
set_owner_sql = '''
update item
set OwnerID = (SELECT ID from member where name = ?)
where item.id = ?
'''

loans = [
   [1,3,'2012-01-04','2012-04-26'],
   [2,5,'2012-09-05','2013-01-05'],
   [3,4,'2013-07-03','2013-07-22'],
   [4,1,'2013-11-19','2013-11-29'],
   [5,2,'2013-12-05', None]
]
loan_sql = '''
insert into loan 
(itemID, BorrowerID, DateBorrowed, DateReturned ) 
values (?, ?, date(?), date(?))'''

db = sqlite3.connect('lendy.db')
cur = db.cursor()

cur.executemany(member_sql, members)
cur.executemany(item_sql, items)
cur.executemany(loan_sql, loans)

owners = ('Fred','Mike','Joe','Rob','Anne','Fred') 
for item in cur.execute("select id from item").fetchall():
    itemID = item[0]	
    cur.execute(set_owner_sql, (owners[itemID-1], itemID))

cur.close()
db.commit()
db.close()

