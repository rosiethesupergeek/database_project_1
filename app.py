from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!")
        
        while True:
            print("""What would you like to do?
                    1 - List all albums
                    2 - List all artists""")
            
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                album_repository = AlbumRepository(self._connection)
                albums = album_repository.all()

                for album in albums:
                    print(f"{album.title}: {album.release_year} ({album.artist_id})")
            elif choice == 2:
                artist_repository = ArtistRepository(self._connection)
                artists = artist_repository.all()

                for artist in artists:
                    print(f"{artist.id}: {artist.name} ({artist.genre})")

if __name__ == '__main__':
        app = Application()
        app.run()

        

        # print(album_repository.find(1))
        # print(artist_repository.find(1))





