"""Import modules."""
from datetime import date, timedelta


def new_data(cur_date: str, number: int) -> str:
    """Adds days to current date.

    Args:
        cur_date : str - current date, format date(dd.mm.yyyy).
        number: int - number of days which we wont to add, decimal number.

    Returns:
        str - new data to which was aded number.
    """
    my_date = [int(d_m_y) for d_m_y in cur_date.split('.')]
    cur = date(my_date[2], my_date[1], my_date[0])
    interval = timedelta(days=number)
    new_date = cur + interval
    return new_date.isoformat()


def captain(lst: list, current_date: str):
    """Keeps a captain's diary. Creates file with notes.

    Args:
        lst : list - list with captain's notes.
        current_date : str - the date the notes started.
    """
    with open('log.txt', 'w') as file_to_open:
        lst_len = len(lst)
        for days in range(lst_len):
            file_to_open.writelines(['{0}{1}:{2}'.format('\n', new_data(current_date, days), lst[days])])
