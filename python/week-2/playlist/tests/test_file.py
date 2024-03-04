from playlist import create_playlist
import pytest


def test_one_song(monkeypatch):
    """Test a one-ong playlist"""
    inputs = iter(["Soothsayer", "Buckethead"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    output = create_playlist(1)
    assert output == [{"title": "Soothsayer", "artist": "Buckethead"}]


def test_seven_songs(monkeypatch):
    """Test a seven-song playlist"""
    inputs = iter(
        [
            "Soothsayer",
            "Buckethead",
            "Everybody Wants to Rule the World",
            "Tears for Fears",
            "Everything in Its Right Place",
            "Radiohead",
            "Visa fran Utanmyra",
            "Jan Johansson",
            "Road to Nowhere",
            "Talking Heads",
            "Orbaum",
            "Grip on the News",
            "Fool me twice.",
            "kuiper",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    output = create_playlist(7)
    assert output == [
        {"title": "Soothsayer", "artist": "Buckethead"},
        {"title": "Everybody Wants to Rule the World", "artist": "Tears for Fears"},
        {"title": "Everything in Its Right Place", "artist": "Radiohead"},
        {"title": "Visa fran Utanmyra", "artist": "Jan Johansson"},
        {"title": "Road to Nowhere", "artist": "Talking Heads"},
        {"title": "Orbaum", "artist": "Grip on the News"},
        {"title": "Fool me twice.", "artist": "kuiper"},
    ]
