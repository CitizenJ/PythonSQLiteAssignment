# PythonSQLiteAssignment

This is a small and simple Python application that reads the content of a text file (hoitojakso.txt) and inserts them into a SQLite database (hoitojakso.db). This application was made as an assignment for a company I was applying for at the time and was made in roughly 2-3 hours despite little to no prior experience with either Python or SQLite.

ASSIGNMENT DETAILS

The given assignment was to read a stream of care periods into a database table. Only periods with arrival dates of 7.6.2006 or later are included. Patient number and arrival date are used as primary keys. The application has to coded with Python. The selection of database was free - I chose SQLite as Python has inbuilt support for it and it's quick and easy to setup.

CODE IN DETAIL

Coming soon. Meanwhile, refer to comments included in the code.

KNOWN ISSUES

When run, the application will print the following error message: "error has occurred: patientnumber and arrivaldate are not unique". This due to the text file containing the same combination of patient number and arrival date twice. Since patient number and arrival date are used as a composite key, and a composite keys have to be unique, the same combination cannot occur twice. The application nevertheless handles this error gracefully, and the rest of the data will be successfully inserted to the database. 
