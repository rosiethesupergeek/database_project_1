import psycopg

# who is this psychopg?!
# psychopg is a python module..so we import it so we can use it's features...
# the psychopg module is a postgreSQL adaptor for python. It provides a Python DB-API 2.0 compliant interface to the postgreSQL database
# wtf?!:
# Yup this postgreSQL adaptor is a standard interface for accessing databases from python.
# when I say standard interface, it's not like a GUI...it's a standard set of methods you can use in order to access your database..
# I guess a bit like a coffee machine and a kettle mean you can just crack on and make a coffee rather than building the machine...



from psycopg.rows import dict_row

# this imports the dict_row class from the rows class in psychopg...
# This is the dictionary stuff!!!!!
# this dict_row class means that when you retrieve query results from a table, they are returned as dictionaries...
# the keys are the column names and then the values are the values from the table...eg {Name: Vincent Can Goch, id: 1, genre: 'impresionism'}


import os

# this is a way to interact with your workspace...it's a bit like a toolbox with various tools for interacting with your workspace.
# The os module provides functions and methods which allow you to access and manipulate environment variables, navigate directories and perform other
# operating systems tasks...

# If the below seems too complex right now, that's OK.
# That's why we have provided it!
class DatabaseConnection:
    DATABASE_NAME = "music_library" # <-- CHANGE THIS!

    # ^^ environment variable in action! You are effectively putting a sticky note on your tool which has the address of your database on it....



    # This method connects to PostgreSQL using the psycopg library. We connect
    # to localhost and select the database name given in argument.

    # It contains a try block...this code runs and then if there are any problems with it, it gives you the exception error message.
    def connect(self):
        try:
            self.connection = psycopg.connect(
                f"postgresql://localhost/{self.DATABASE_NAME}",
                row_factory=dict_row)
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the database {self.DATABASE_NAME}! " \
                    f"Did you create it using `createdb {self.DATABASE_NAME}`?")
        

    # psychopg.connect is a method from the psychopg library which establishes a connection a postgreSQL database
    # f"postgresql://localhost/{self.DATABASE_NAME}" : this constructs a string which is used to tell the psychopg library where I want the connection
    # to go to....like instructions on how to get to a place...
    # it says: - make this a postgresql thing...make it on this machine (//localhost/)...go to this database (self.DATABASE_NAME)
    # TLDR: go here and connect to this, using the psychopg lib.
        
    # row_factory= dict_row says go to the psychopg library and use the dict_row class so that our results are returned as dictionaries.
    
    # the psychopg.OperationalError will happen if something goes wrong with the connection and then you will get an error message...




    # This method seeds the database with the given SQL file...understood.
    # We use it to set up our database ready for our tests or application.
    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        
    # this uses the ._check_connection method to make sure there is a connection to a valid database...if there isn't, it will break
    # if the connection is all good, then it will follow the path to find the sql_filename...if it can't find it then it raises an exception.

        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    # the cursor object is established through the .cursor() method being called...you use this to execute SQL queries and collect results from a database.
    # Then because you've created a cursor object you can then call a method on the cursor object which opens the sql file in read mode, then reads it
    # then gives it to the execute method...
    # this then executes the code with in the sql file, which seeds your database!!!








    # This method executes a SQL query on the database.
    # It allows you to set some parameters too. You'll learn about this later.
    def execute(self, query, params=None):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = '' \
        'DatabaseConnection.exec_params: Cannot run a SQL query as ' \
        'the connection to the database was never opened. Did you ' \
        'make sure to call first the method DatabaseConnection.connect` ' \
        'in your app.py file (or in your tests)?'
    

    # ok so the above checks the old connection again using the method _check_connection...which is written below
    # it then creates the cursor object again (remember this is created to allow execution of sql and to collect results from a database)
    # so on the line cursor.execute(query, params)...the query and the parameters are given to the execute method which is part of the cursor class?
    # This executes the query...
    # then it checks to see if the cursor has collected anything...(cursor.description is not None)...
    # if there are some results waiting there, it collects them and holds them in a result variable..."result = cursor.fetchall()"
    # otherwise (else) there are no result to be collected...so result is an empty variable...

    # then commit all the changes to the database "self.connection.commit()"
    # and finally return the result of the query.






    # so is the connection just left open all the time once it is opened? 



    # This private method checks that we're connected to the database.
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)
        
    # pretty self explanatory...
