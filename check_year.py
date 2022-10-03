"""Checks date."""
DAY_IN_MOUTH = 30
HUNDRED = 100
MONTH_ONE = [1, 3, 5, 7, 8, 10, 12]
MONTH_TWO = [4, 6, 9, 11]


def check_date(year: int, month: int, day: int) -> bool:
    """Takes year, month, day and checks does the date exist.

    Args:
        year : int - some year.
        month : int - some month.
        day : int - some day.

    Returns:
        bool :  true if the date exist else false.
    """
    if month in MONTH_ONE and 0 < day <= DAY_IN_MOUTH + 1:
        return True
    elif month in MONTH_TWO and 0 < day <= DAY_IN_MOUTH:
        return True
    elif month == 2:
        if abs(year) % HUNDRED == 0 and abs(year) % HUNDRED * 4 == 0 or abs(year) % 4 == 0 \
                and abs(year) % HUNDRED != 0:
            if 0 < day <= DAY_IN_MOUTH - 1:
                return True
        elif 0 < day <= DAY_IN_MOUTH - 2:
            return True
    return False
