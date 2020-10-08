#FIND door, and kitchen

#!/usr/bin/env python3
import sqlite3
#some initial data
id = 4;
temperature = 0.0;
date = '2014-01-05';
#connect to database file
dbconnect = sqlite3.connect("my.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

try:
    cursor.execute('''create table temperature(id integer, temp float, date text)''');
except sqlite3.OperationalError:
    print('''\n operational error:
                temperature table already exists,
                deleting all rows\n''')
    cursor.execute('''DELETE FROM temperature''')

for i in range(10):
    #execute insert statement
    id += 1;
    temperature += 1.1;
    cursor.execute('''insert into temperature values (?, ?, ?)''',
    (id, temperature, date));
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temperature');
#print data
for row in cursor:
    print(row['id'],row['temp'],row['date'] );


print("\n ===== STARTING OPERATIONS ON SENSORS TABLE ===== \n");

try:
    cursor.execute('''create table sensors(id integer, type text, zone text)''');
except sqlite3.OperationalError:
    print('''\n operational error:
                sensor table already exists,
                Deleting all rows\n''')
    cursor.execute('''DELETE FROM sensors''')

#insert table entries 
cursor.execute('''insert into sensors values (?, ?, ?)''',
               (1, 'door', 'kitchen'));
cursor.execute('''insert into sensors values (?, ?, ?)''',
               (2, 'temperature', 'kitchen'));
cursor.execute('''insert into sensors values (?, ?, ?)''',
               (3, 'door', 'garage'));
cursor.execute('''insert into sensors values (?, ?, ?)''',
               (4, 'motion', 'garage'));
cursor.execute('''insert into sensors values (?, ?, ?)''',
               (5, 'temperature', 'garage'));

dbconnect.commit();

#display all the sensors in the kitchen
print("\r\n\n -- kitchen sensors -- \n");
cursor.execute('SELECT * FROM sensors WHERE zone == "kitchen"');
#print data
for row in cursor:
    print(row['id'],row['type'],row['zone'] );

#display all the door sensors

print("\r\n\n -- door sensors -- \n");
cursor.execute('SELECT * FROM sensors WHERE type == "door"');
#print data
for row in cursor:
    print(row['id'],row['type'],row['zone'] );


#close the connection
dbconnect.close();