import check50


@check50.check()
def exists():
   """dots.py exists"""
   check50.exists("dots.py")
   check50.include("tests.py")


@check50.check(exists)
def test_decode_small():
   """decode successfully returns a simple one word decoded string."""
   # decode successfully returns
   exit = check50.run("pytest tests.py -k 'test_decode_small'").exit()
   if exit == 1:
       raise check50.Failure(f"Decode doesn't successfully decodes a simple string.")


@check50.check(exists)
def test_decode_small_numbers():
   """decode successfully returns a simple decoded string with numbers."""
   exit = check50.run("pytest tests.py -k 'test_decode_numbers'").exit()
   if exit == 1:
       raise check50.Failure(f"Decode doesn't successfully decodes a simple string with numbers.")


@check50.check(exists)
def test_decode_repeated_chars():
   """decode successfully returns a simple decoded with repeated characters."""
   exit = check50.run("pytest tests.py -k 'test_decode_double'").exit()
   if exit == 1:
       raise check50.Failure(f"Decode doesn't successfully decodes a simple string with repeated characters.")


@check50.check(exists)
def test_decode_small_non_alphanumerical():
   """decode successfully returns a simple decoded string with non alphanumeric characters."""
   exit = check50.run("pytest tests.py -k 'test_decode_non_alphanumeric'").exit()
   if exit == 1:
       raise check50.Failure(f"Decode doesn't successfully decodes a simple string with non alphanumeric characters.")


@check50.check(exists)
def test_decode_advanced():
   """decode successfully returns an advanced decoded string."""
   exit = check50.run("pytest tests.py -k 'test_decode_advanced'").exit()
   if exit == 1:
       raise check50.Failure(f"Decode doesn't successfully decodes an advanced string.")