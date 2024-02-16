class Album:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, title, release_year, artist_id):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    # ok so putting the id, name and genre into the __init__ class means that these attributes can be accessed from other places outside
    # of the class...for example accessing artist.name and artist.genre when adding artists to the artists table via the artist_repository.create() method!

    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    # The above method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records......
    # ok so do we just have this __eq__ method because we want to do TDD? 
    # then we can check if an Artist object returned from a function we wrote is the Artist object that it should be? ie - has the same attribute values...

    
    def __repr__(self):
        return f"Album({self.title}, {self.release_year}, {self.artist_id})"
    # This method makes it look nicer when we print an Artist... but is actually important for other reasons too:
    # the name __repr__ generally means string representation...
    # the __repr__ method is usually used to return a string in the format of an original object.
    # for example when an instance of the Artist class is made (ie an abject is made) then it is in the format:
    #   van_goch = Artist(1, "Vincent Van Goch", "Impressionism")

    # and when I run van_goch.__repr__()
    # it will return:
    # "Artist(1, "Vincent Van Goch", "Impressionism")"