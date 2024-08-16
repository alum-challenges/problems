import check50
from re import escape, search, sub


def regex(text):
    """match case-sensitively with any characters on either side"""
    return rf"^[\s\S]*{escape(text)}[\s\S]*$"


INVALID = "Invalid directions, please try again.\n> "
GO = {
    "north": "You walk north and arrive at an orchard of apple trees.\n> ",
    "south": "You walk south and arrive at a field of healings herbs.\n> ",
    "east": "You walk east and arrive at a spring full of drinking water.\n> ",
    "west": "You walk west and arrive at a lumber yard full of firewood.\n> ",
    "home": "You go home, ending your adventure here. Goodbye!",
}
INVENTORY = {
    "apples": 0,
    "herbs": 0,
    "water": 0,
    "firewood": 0,
}


@check50.check()
def exists():
    """adventure.py exists"""
    check50.exists("adventure.py")


@check50.check(exists)
def test_no_ifs():
    """adventure.py does not contain if statements"""
    with open("adventure.py", "r") as file:
        contents = file.read()
        if search(r"(?<!#)(?:^|\n\s*)(\bif\b)", contents):
            raise check50.Failure(
                "adventure.py uses if statements",
                help="Be sure only to use match-case structural pattern matching",
            )


@check50.check(test_no_ifs)
def test_invalid_command():
    """adventure.py rejects invalid command"""
    check50.run("python3 adventure.py").stdin("Pet the cat", prompt=True).stdout(
        regex(INVALID), INVALID, regex=True
    ).kill()


@check50.check(test_no_ifs)
def test_invalid_go_command():
    """adventure.py rejects invalid Go direction"""
    NO_GO = "You cannot go left. Valid directions are north, south, east, west, and home.\n> "
    check50.run("python3 adventure.py").stdin("Go left", prompt=True).stdout(
        regex(NO_GO), NO_GO, regex=True
    ).kill()


@check50.check(test_no_ifs)
def test_valid_go():
    """adventure.py accepts valid Go commands"""
    process = check50.run("python3 adventure.py")
    for dir in GO:
        process.stdin(f"Go {dir}", prompt=False).stdout(
            regex(GO[dir]), GO[dir], regex=True
        )
    process.exit(0)


@check50.check(test_no_ifs)
def test_invalid_take_command():
    """adventure.py rejects invalid Take command"""
    check50.run("python3 adventure.py").stdin("Take an arrow", prompt=True).stdout(
        regex(INVALID), INVALID, regex=True
    ).kill()


@check50.check(test_no_ifs)
def test_valid_take():
    """adventure.py accepts valid Take commands"""
    process = check50.run("python3 adventure.py")
    take = f"You take an apple and add to your inventory.\n> "
    process.stdin(f"Take an apple", prompt=False).stdout(regex(take), take, regex=True)
    for item in INVENTORY:
        take = f"You take some {item} and add to your inventory.\n> "
        process.stdin(f"Take some {item}", prompt=False).stdout(
            regex(take), take, regex=True
        )
    process.kill()


@check50.check(test_valid_take)
def test_count_command():
    """adventure.py has correct Count commands"""
    process = check50.run("python3 adventure.py")
    for item in INVENTORY:
        count = f"You have 0 {item} in your inventory.\n> "
        process.stdin(f"Count {item}", prompt=False).stdout(
            regex(count), count, regex=True
        )
    process.stdin(f"Take an apple", prompt=False)
    process.stdin(f"Take an apple", prompt=False)
    count = f"You have 2 apples in your inventory.\n> "
    process.stdin(f"Count apples", prompt=False).stdout(regex(count), count, regex=True)
    process.kill()
