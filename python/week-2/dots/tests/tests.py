from dots import decode

# letters
def test_decode_small():
    assert decode("..o...t.d") == "dot"
    assert decode("....k..u.d...c.....y") == "ducky"

# numbers
def test_decode_numbers():
    assert decode("..2.1.....5...3....4") == "12345"


# non alphanumeric charachters
def test_decode_non_alphanumeric():
    assert decode(".,......*....%.. .....$...^") == ", ^%$*"

# test for repeated charachters
def test_decode_double():
    assert decode(".......l......o........l..i.....r....k.r...c") == "rickroll"
    assert decode("..,.... ... .,") == ",,  "
    assert decode("..2.1.....2....1......3...3") == "123123"

# mixed 
def test_decode_advanced():
    assert decode("......,.....o...l..e................y............... ..........w.............r....l..............e.........o........h....... .................o...................?..................u............a........... .H") == "Hello, how are you?"
    assert decode(".......4.1......c..a...2....b........d.....3") == "1a2b3c4d"
    assert decode("..S.C...5....0") == "CS50"

