import check50

@check50.check()
def exists():
    """dots.py exists"""
    check50.exists("dots.py")

@check50.check(exists)
def test_decode_small():
    """decode successfully returns a simple decoded string."""
    exit = check50.run("pytest tests.py -k 'test_decode_small'").exit()
    if exit == 1:
        raise check50.Failure(f"Decode doesn't  successfully decodes a simple string.")

@check50.check(exists)
def test_decode_small():
    """decode successfully returns a simple decoded string."""
    exit = check50.run("pytest tests.py -k 'test_decode_numbers'").exit()
    if exit == 1:
        raise check50.Failure(f"Decode doesn't  successfully decodes a simple string with numbers.")

@check50.check(exists)
def test_decode_small():
    """decode successfully returns a simple decoded string."""
    exit = check50.run("pytest tests.py -k 'test_decode_non_alphanumeric'").exit()
    if exit == 1:
        raise check50.Failure(f"Decode doesn't  successfully decodes a simple string with non alphanumarical charachters.")
