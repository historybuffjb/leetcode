"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
"""


def convert(s: str, num_rows: int) -> str:
    """
    Explanation:
        * The key here is to know which row you are in as you traverse the string
        * We can make a list of num_rows number of strings and push elements to them as you traverse
        * Then at the end join them together
    """
    if num_rows == 1:
        return s
    final_result = [""] * num_rows
    is_down = False
    cur_row = 0
    for val in s:
        final_result[cur_row] += val
        if cur_row == 0 or cur_row == num_rows - 1:
            is_down ^= True
        cur_row += 1 if is_down else -1
    return ''.join(final_result)


"""
Run DETAILS
Runtime: 44 ms, faster than 98.91% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 14.1 MB, less than 99.66% of Python3 online submissions for ZigZag Conversion.
"""
