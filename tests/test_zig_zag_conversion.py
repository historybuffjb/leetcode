from problems.zig_zag_conversion import convert


def test_zig_zag_conversion_1():
    s = "PAYPALISHIRING"
    num_rows = 3
    expected = "PAHNAPLSIIGYIR"
    actual = convert(s, num_rows)
    assert actual == expected


def test_zig_zag_conversion_2():
    s = "PAYPALISHIRING"
    num_rows = 4
    expected = "PINALSIGYAHRPI"
    actual = convert(s, num_rows)
    assert actual == expected


def test_zig_zag_conversion_3():
    s = "PAYPALISHIRING"
    num_rows = 5
    expected = "PHASIYIRPLIGAN"
    actual = convert(s, num_rows)
    assert actual == expected


def test_zig_zag_conversion_4():
    s = "PAYPALISHIRING"
    num_rows = 6
    expected = "PRAIIYHNPSGAIL"
    actual = convert(s, num_rows)
    assert actual == expected


def test_zig_zag_conversion_5():
    s = "PAYPALISHIRING"
    num_rows = 7
    expected = "PNAIGYRPIAHLSI"
    actual = convert(s, num_rows)
    assert actual == expected


def test_zig_zag_conversion_6():
    s = "PAYPALISHIRING"
    num_rows = 8
    expected = "PAGYNPIARLIIHS"
    actual = convert(s, num_rows)
    assert actual == expected


def test_zig_zag_conversion_7():
    s = "A"
    num_rows = 1
    expected = "A"
    actual = convert(s, num_rows)
    assert actual == expected
