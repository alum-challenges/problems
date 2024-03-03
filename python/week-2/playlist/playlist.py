def main():
    num_songs = input("How many songs are in your playlist? ")

    while not num_songs.isdigit():
        num_songs = input("How many songs are in your playlist? ")

    num_songs = int(num_songs)

    playlist = create_playlist(num_songs)

    for num, track in enumerate(playlist):
        print(f"{num + 1}. {track['title']} by {track['artist']}")


def create_playlist(num_songs: int):
    playlist = []

    for i in range(num_songs):
        title = input(f"{i + 1}. Title: ")
        artist = input(f"{i + 1}. Artist: ") if title else ""
        while not title or not artist:
            print("Title or artist cannot be blank")
            title = input(f"{i + 1}. Title: ")
            if not title:
                continue
            artist = input(f"{i + 1}. Artist: ")

        playlist.append({"title": title, "artist": artist})

    return playlist


if __name__ == "__main__":
    main()
