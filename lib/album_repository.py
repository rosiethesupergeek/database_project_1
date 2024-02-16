from lib.album import Album

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums
    def all(self):
        rows = self._connection.execute('SELECT * from albums')     
        albums = []
    # an empty list to collect the results
        
        for row in rows:    
            item = Album(row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    

    # Find a single artist by their title
    def find(self, title):
    # find accepts 2 args including artist_id which will be used to specify the result
        rows = self._connection.execute(
            'SELECT * from albums WHERE title = %s', [title])
        row = rows[0]
        return Album(row["title"], row["release_year"], row["artist_id"])


    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year) VALUES (%s, %s)', [
                                 album.title, album.release_year])
        return None
    
    
    # Delete an album by it's title
    def delete(self, title):
        self._connection.execute(
            'DELETE FROM albums WHERE title = %s', [title])
        return None

# the above makes perfect sense considering everything else I have learnt from the rest of this...