from lib.artist import Artist

class ArtistRepository:

# this is like the creation of a specialist librarian who is in charge of the Artists section of the 
# library. This librarian will make sure you can find what you need in the artists library.

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

# when we initialise an instance of the ArtistRepository class we pass it a connection argument.
# this is like giving the librarian a key to the artists library so that they can access the books.
# by having the connection assigned to a variable in the __init__ method, it is accessible by other
# methods throughout the class for database operations.

# so when you create an instance of ArtistsRepository and pass it a connection, that connection
# is stored within the instance and can be used throughout it's lifecycle.


    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
    # this runs a method on the self._connection  variable established in the __init__ function...
    # the method is .execute and it tells the program to use the connection to run a SQL command
    # in this case the SQL command is pretty simple, it just wants to get everything from the artists table...
    # the result of all this is held in the variable "rows"...so is the whole table held in the rows variable then?
    # IMPORTANT!!! : when using this syntax the results are usually returned as a dictionary...with the keys being the names of the 
    # columns and the values being the contents of the columns...
        
        artists = []
    # an empty list to collect the results
        
        for row in rows:    
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists
    # the above for loop goes through the rows collected by the 'rows = self._connection.execute('SELECT * from artists')
    # variable...
    # for each row collected it creates a variable called item.
    # item contains an instance of the Artist class.
    # This Artist class must accept 3 arguments...id, name and genre! See artist.py !
    # For each row that the for loop goes through it appends the row to the artists list!
    # it is using dictionaries to do this...row['id'] is finding the id key in the dictionary and
    # then pulling out the value that goes with the key...yes but the whole thing is then packaged into an Artist object...
    # analogy: book is written as notes - all over the place...the all function puts it into a book...





    # Find a single artist by their id
    def find(self, artist_id):
    # find accepts 2 args including artist_id which will be used to specify the result
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
    # again the rows variable holding the results of going through the established connection (__init__) to run a SQL
    # query that collects the results where the artist_id matches the one given in the argument...how though?
    # how = '%s'is placeholder text in the SQL query...the thing it will be replaced by is held in square brackets after it:
    # hence the [artist_id]

        row = rows[0]
    # this is putting the first index of rows into a variable 'row'
        
        return Artist(row["id"], row["name"], row["genre"])
    # Then finally creating an instance of the Artist class (creating an Artist object) that has the values of id, name and row.
    





    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
                                 artist.name, artist.genre])
        return None
    # ok so now I can explain this one without faff!
    # you give the .create() method the name of the artist you want to add.
    # it chats to your database ._connection.execute and then you INSERT using the SQL command:
    # ('INSERT INTO artists (name, genre) VALUES (%s, %s)', [artist.name, artist.genre]):
    # the %s %s are placeholders for [artist.name, artist.genre]

    # hang about hang about hang about...

    # do I have to have created an instance of the Artist class called "artist"...?

    # nope because the argument can be anything...I could say:
    # artist_repository = ArtistRepository(database_connection)

    # van_goch = Artist(id = None, name = 'Vincent', genre = 'Impressionism')
    # artist_repository.create(van_goch)...and it will do the following:
    # INSERT INTO artists (name, genre) VALUES (%s,%s), [van_goch.name, van_goch.genre]), which is:
    # INSERT INTO artists (name, genre) VALUES ("Vincent", "Impressionism")

    # before I have used the .create method through the ArtistRepository class the instance of the Artist class has no id...
    # should the Artist __init__ function be set so that it can have a default of None? because if I assign it something then it
    # could mess with the database no? Ans: it's ok, it can accept None.

    # Returning the id:
    # Just modify the return line so it says:
    # return artist.id ...? No this would not work! because it would just return the id of the thing you just inserted BEFORE it has been
    # assigned an id, so you'd get None back!
    # 
    # In order to return the id you need to run a query, that matches the name that you just inserted, like this:
    # def create(self, artist):
        # self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
        #                          artist.name, artist.genre])
        # rows =  self._connection.execute('SELECT * FROM artists WHERE name = %s', [artist.name])
        # row = rows[0]       ...why do we need this? This means I'm just getting the first index via the next line:
        # return Artist(row['id']), row['name'], row['genre'])
    
    # there is also another way, if your _connection object has certain methods attached to it (I don't know if ours does yet!):
    # def create(self, artist):
    # self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
    #                          artist.name, artist.genre])
    # artist_id = self._connection.lastrowid
    # return artist_id

    # this uses the .lastrowid method...do we have this though? No...







    # Delete an artist by their id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
        return None

# the above makes perfect sense considering everything else I have learnt from the rest of this...