from datetime import datetime
import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect

#Did not end up needing this class, but I left it commented out just to show I can do it lol
#
#class Hoitojakso:
#    def __init__(self, pn, ad, rd, ward, weight):
#        self.pn = pn
#        self.ad = ad
#        self.rd = rd
#        self.ward = ward
#        self.weight = weight

# function for connecting to database
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection successful")
    except Error as e:
        print("Error has occurred: {}").format(e)
    return connection

# function for executing queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Successfully inserted record")
    except Error as e:
        print("Error has occurred: {}").format(e)
    

#create a date for excluding dates preceding it
es = "07.06.2006"
ed = datetime.strptime(es, '%d.%m.%Y').date()

#open and read all the lines from a text file
with open('hoitojakso.txt') as f:
    lines = f.readlines()

connection = create_connection('hoitojakso.db')

for line in lines:
    fi = line.split(",") #using comma as a separator, extract all the fields into an array
    if fi[0] != "Patientnumber": #excludes the first line to avoid conversion errors. 
        cad = datetime.strptime(fi[1], '%d.%m.%Y').date() #converts the second field (arrival date) into date
        if cad > ed: #If the arrival date is later than the exclusion date, execute a query
            insert = """ 
            INSERT INTO
             hoitojakso (patientnumber, arrivaldate, releasedate, ward, weight)
            VALUES
             ({}, '{}', '{}', '{}', {})
            """.format(fi[0], fi[1], fi[2], fi[3], fi[4])
            execute_query(connection, insert)