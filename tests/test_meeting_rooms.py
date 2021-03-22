from problems.meeting_rooms import can_attend_meetings


def test_meeting_rooms_1():
    intervals = [[0, 30], [5, 10], [15, 20]]
    expected = False
    actual = can_attend_meetings(intervals)
    assert actual == expected


def test_meeting_rooms_2():
    intervals = [[7, 10], [2, 4]]
    expected = True
    actual = can_attend_meetings(intervals)
    assert actual == expected


def test_meeting_rooms_3():
    intervals = []
    expected = True
    actual = can_attend_meetings(intervals)
    assert actual == expected


def test_meeting_rooms_4():
    intervals = [[1, 10]]
    expected = True
    actual = can_attend_meetings(intervals)
    assert actual == expected


def test_meeting_rooms_5():
    intervals = [[1, 10], [9, 11]]
    expected = False
    actual = can_attend_meetings(intervals)
    assert actual == expected


def test_meeting_rooms_6():
    intervals = [[12, 15], [18, 25], [30, 32], [33, 41], [42, 48], [70, 90]]
    expected = True
    actual = can_attend_meetings(intervals)
    assert actual == expected
