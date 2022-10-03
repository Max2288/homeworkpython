def checker(day: int, month: int, year: int) -> bool:
    """Takes year, month, day and checks does the date exist.

    Args:
        year : int - some year.
        month : int - some month.
        day : int - some day.

    Returns: bool - true if the date exist else false.
    """
    if 0 < day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    if 0 < day <= 30 and month in [4, 6, 9, 11]:
        return True
    if month == 2:
        if year % 100 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            if 0 < day <= 29:
                return True
        if 0 < day <= 28:
            return True
    return False
