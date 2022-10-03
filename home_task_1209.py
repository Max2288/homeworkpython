def find_big_letters(s: str) -> bool:
    """Takes string and returns True if number of capital letters bigger than small.

    Args:
        s: str - string where we count big letter.
    Returns: True if number of capital letters bigger than small.
    """
    mini_letters = 0
    big_letters = 0
    for letter in s:
        if letter.islower():
            mini_letters += 1
        else:
            big_letters += 1
    if big_letters > mini_letters:
        return True
    else:
        return False


def fifth_task(s: str) -> float:
    """Takes string with capitals letter and small letters, counts substrings which are more.

    Args:
        s : str - string with substrings.

    Returns: float - percentage of substrings with more capitals letter.
    """
    strings = s.split()
    string_len = len(strings)
    big_str = 0
    for string in strings:
        if find_big_letters(string):
            big_str += 1
    return big_str / string_len * 100
