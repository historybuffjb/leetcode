from problems.palindrome_number import is_palindrome


def test_palindrome_number_1():
    x = 121
    expected = True
    actual = is_palindrome(x)
    assert actual == expected


def test_palindrome_number_2():
    x = -121
    expected = False
    actual = is_palindrome(x)
    assert actual == expected


def test_palindrome_number_3():
    x = 10
    expected = False
    actual = is_palindrome(x)
    assert actual == expected


def test_palindrome_number_4():
    x = -101
    expected = False
    actual = is_palindrome(x)
    assert actual == expected


def test_palindrome_number_5():
    x = 123
    expected = False
    actual = is_palindrome(x)
    assert actual == expected


def test_palindrome_number_6():
    x = 6666
    expected = True
    actual = is_palindrome(x)
    assert actual == expected


def test_palindrome_number_7():
    x = 0
    expected = True
    actual = is_palindrome(x)
    assert actual == expected


def test_palindrome_number_8():
    x = 6
    expected = True
    actual = is_palindrome(x)
    assert actual == expected


def test_palindrome_number_9():
    x = 17371
    expected = True
    actual = is_palindrome(x)
    assert actual == expected
