from dots import decode

def test_decode_small():
    assert decode("..o...t.d") == "dot"
    assert decode("....k..u.d...c.....y") == "ducky"

def test_decode_numbers():
    assert decode("..S.C...5....0") == "CS50"
    assert decode(".......4.1......c..a...2....b........d.....3") == "1a2b3c4d"

def test_decode_non_alphanumeric():
    assert decode("......,.....o...l..e................y............... ..........w.............r....l..............e.........o........h....... .................o...................?..................u............a........... .H") == "Hello, how are you?"
    assert decode(".,......*....%.. .....$...^") == ", ^%$*"
