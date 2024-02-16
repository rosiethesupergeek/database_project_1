from lib.album import Album

"""
Album constructs with a title, release_year and artist_id

"""
def test_album_constructs():
    album = Album('Doolittle', 1989, 1)
    assert album.title == 'Doolittle'
    assert album.release_year == 1989
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album('Test Title', 1989, 1)
    assert str(album) == "Album(Test Title, 1989, 1)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album('Test Title', 1989, 1)
    album2 = Album('Test Title', 1989, 1)
    assert album1 == album2
