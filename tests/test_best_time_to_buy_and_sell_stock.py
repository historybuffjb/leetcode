from problems.best_time_to_buy_and_sell_stock import max_profit


def test_best_time_to_buy_and_sell_stocks_1():
    prices = [7, 1, 5, 3, 6, 3]
    expected = 5
    actual = max_profit(prices)
    assert actual == expected


def test_best_time_to_buy_and_sell_stocks_2():
    prices = [7, 6, 4, 3, 1]
    expected = 0
    actual = max_profit(prices)
    assert actual == expected


def test_best_time_to_buy_and_sell_stocks_3():
    prices = [1]
    expected = 0
    actual = max_profit(prices)
    assert actual == expected


def test_best_time_to_buy_and_sell_stocks_4():
    prices = [1, 2, 3, 4, 5, 6, 7]
    expected = 6
    actual = max_profit(prices)
    assert actual == expected


def test_best_time_to_buy_and_sell_stocks_5():
    prices = [1, 2]
    expected = 1
    actual = max_profit(prices)
    assert actual == expected


def test_best_time_to_buy_and_sell_stocks_6():
    prices = [20, 5, 100, 7, 1, 20, 100]
    expected = 99
    actual = max_profit(prices)
    assert actual == expected
