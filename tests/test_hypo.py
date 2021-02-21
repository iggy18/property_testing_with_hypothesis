from hypo import encode, decode, add_two_numbers
from hypothesis import given, example
from hypothesis.strategies import text, integers
from hypothesis.extra.ghostwriter import magic as make

def test_encode():
    assert encode

def test_decode():
    assert decode

def test_add_two_():
    assert add_two_numbers

def test_encode_works():
    x = "this is a test"
    actual = encode(x)
    expected = [('t', 1), ('h', 1), ('i', 1), ('s', 1), (' ', 1), ('i', 1), ('s', 1), (' ', 1), ('a', 1), (' ', 1), ('t', 1), ('e', 1), ('s', 1), ('t', 1)]
    assert actual == expected

def test_decode_works():
    x = [('t', 1), ('h', 1), ('i', 1), ('s', 1), (' ', 1), ('i', 1), ('s', 1), (' ', 1), ('a', 1), (' ', 1), ('t', 1), ('e', 1), ('s', 1), ('t', 1)]
    actual = decode(x)
    expected = "this is a test"
    assert actual == expected

# these pytests check that if you encode something and decode it you get the same value back, which you do.

@given(text())
@example(string="") # shows this edge case is explicidly tested, and is tested every time
def test_decode_inverts_encode(string):
    assert decode(encode(string)) == string

# the above test fails with (UnboundLocalError: local variable 'character' referenced before assignment) even though the funtions passed the encode/decode test with a speciafied payload. why? hypothesis throws an error with the falsifying example being an empty string... now if we write a pytest code for this we will see if the test will pass...

def test_decode_inverts_encode_with_pytest():
    x = ""
    assert decode(encode(x)) == x

# the test fails! hypothesis helped discover this edge case. if we add if not string: return [] to the begining of the funtion all tests will pass.


# the function being tested has been rigged to pass for the following two tests, but it only passes in these two cases.
def test_add_two_numbers_works():
    actual = add_two_numbers(4,5)
    expected = 9
    assert actual == expected

def test_add_two_numbers_works():
    actual = add_two_numbers(4,5)
    expected = 9
    assert actual == expected

# hypothesis catches sneaky function and lets me know that 0 + 1 == -1, so somthing is wrong.
@given(integers(), integers())
def test_add_two_numbers_works(a,b):
    assert add_two_numbers(a,b) == a + b
