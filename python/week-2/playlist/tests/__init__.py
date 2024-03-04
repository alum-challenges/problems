import check50
from re import escape


def regex(text):
    """match case-sensitively with any characters on either side"""
    return rf"^[\s\S]*{escape(text)}[\s\S]*$"


@check50.check()
def exists():
    """playlist.py exists"""
    check50.exists("playlist.py")
    check50.include("test_file.py")


@check50.check(exists)
def test_string_songcount():
    """playlist.py rejects non-numeric number of songs"""
    check50.run("python3 playlist.py").stdin("cat", prompt=True).reject()


@check50.check(exists)
def test_empty_songcount():
    """playlist.py rejects empty number of songs"""
    check50.run("python3 playlist.py").stdin("", prompt=True).reject()


@check50.check(exists)
def test_negative_songcount():
    """playlist.py rejects negative number of songs"""
    check50.run("python3 playlist.py").stdin("-10", prompt=True).reject()


@check50.check(exists)
def test_decimal_songcount():
    """playlist.py rejects non-integer number of songs"""
    check50.run("python3 playlist.py").stdin("3.14", prompt=True).reject()


@check50.check(exists)
def test_valid_songcount():
    """playlist.py accepts valid number of songs"""
    check50.run("python3 playlist.py").stdin("10", prompt=False).stdout(
        regex("Title:"), "Title:", regex=True
    ).kill()


@check50.check(exists)
def test_empty_song_name():
    """playlist.py rejects empty song title"""
    check50.run("python3 playlist.py").stdin("1", prompt=True).stdin(
        "Soothsayer", prompt=True
    ).stdin("", prompt=True).reject()


@check50.check(exists)
def test_empty_artist_name():
    """playlist.py rejects empty artist name"""
    check50.run("python3 playlist.py").stdin("1", prompt=True).stdin(
        "", prompt=True
    ).stdout(regex("Title:"), "Title:", regex=True).kill()


@check50.check(exists)
def test_one_song():
    """create_playlist() returns single-song playlist with correct format"""
    check50.run("pytest test_file.py -k 'test_one_song'").exit(0)


@check50.check(test_one_song)
def test_seven_songs():
    """create_playlist() return multi-song playlist with correct format"""
    check50.run("pytest test_file.py -k 'test_seven_songs'").exit(0)


@check50.check(test_one_song)
def test_one_song_output():
    """playlist.py outputs a single-song playlist with correct format"""

    output = """1. Soothsayer by Buckethead"""

    check50.run("python3 playlist.py").stdin("1", prompt=False).stdin(
        "Soothsayer", prompt=False
    ).stdin("Buckethead", prompt=False).stdout(regex(output), output, regex=True).kill()


@check50.check(test_one_song)
def test_seven_song_output():
    """playlist.py outputs a multi-song playlist with correct format"""

    output = """1. Soothsayer by Buckethead
2. Everybody Wants to Rule the World by Tears for Fears
3. Everything in Its Right Place by Radiohead
4. Visa fran Utanmyra by Jan Johansson
5. Road to Nowhere by Talking Heads
6. Orbaum by Grip on the News
7. Fool me twice. by kuiper"""

    check50.run("python3 playlist.py").stdin("7", prompt=False).stdin(
        "Soothsayer", prompt=False
    ).stdin("Buckethead", prompt=False).stdin(
        "Everybody Wants to Rule the World", prompt=False
    ).stdin(
        "Tears for Fears", prompt=False
    ).stdin(
        "Everything in Its Right Place", prompt=False
    ).stdin(
        "Radiohead", prompt=False
    ).stdin(
        "Visa fran Utanmyra", prompt=False
    ).stdin(
        "Jan Johansson", prompt=False
    ).stdin(
        "Road to Nowhere", prompt=False
    ).stdin(
        "Talking Heads", prompt=False
    ).stdin(
        "Orbaum", prompt=False
    ).stdin(
        "Grip on the News", prompt=False
    ).stdin(
        "Fool me twice.", prompt=False
    ).stdin(
        "kuiper", prompt=False
    ).stdout(
        regex(output), output, regex=True
    ).kill()
