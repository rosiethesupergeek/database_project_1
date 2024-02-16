from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_album_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2),
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find('Fodder on My Wings')
    assert album == Album('Fodder on My Wings', 1982, 4)

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album('Wannabe', 1996, None))

    result = repository.all()
    assert result == [
    Album('Doolittle', 1989, 1),
    Album('Surfer Rosa', 1988, 1),
    Album('Waterloo', 1974, 2),
    Album('Super Trouper', 1980, 2),
    Album('Bossanova', 1990, 1),
    Album('Lover', 2019, 3),
    Album('Folklore', 2020, 3),
    Album('I Put a Spell on You', 1965, 4),
    Album('Baltimore', 1978, 4),
    Album('Here Comes the Sun', 1971, 4),
    Album('Fodder on My Wings', 1982, 4),
    Album('Ring Ring', 1973, 2),
    Album('Wannabe', 1996, None),
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete('Wannabe')

    result = repository.all()
    assert result == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2),
    ]
