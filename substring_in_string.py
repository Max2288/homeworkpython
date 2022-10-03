"""Find percents substtrings."""


def find_big_letters(string: str) -> bool:
    """Takes string_with_letters and returns True if number of capital letters bigger than small.

    Args:
        string : str - string where we count big letter.
    Returns:
        bool - True if number of capital letters bigger than small.
    """
    big_letters = 0
    for letter in string:
        if letter.isupper():
            big_letters += 1
    return True if big_letters > len(string) - big_letters else False


def fifth_task(string_with_substrings: str) -> float:
    """Takes string with capitals letter and small letters, counts substrings which are more.

    Args:
        string_with_substrings : str - string with substrings.

    Returns: float - percentage of substrings with more capitals letter.
    """
    strings = string_with_substrings.split()
    string_len = len(strings)
    big_str = 0
    for string in strings:
        if find_big_letters(string):
            big_str += 1
    return big_str / string_len * 100
