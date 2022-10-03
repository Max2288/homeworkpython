from datetime import date, timedelta


def new_data(cur_date: str, n: int) -> str:
    """Adds days to current date.

    Args:
        cur_date : str, current date, format date(dd.mm.yyyy).
        n: int, number of days which we wont to add, decimal number.

    Returns: str - new data to which was aded number.
    """
    my_date = [int(i) for i in cur_date.split('.')]
    cur = date(my_date[2], my_date[1], my_date[1])
    interval = timedelta(days=n)
    result = cur + interval
    return result.isoformat()


def captain(lst: list, date: str):
    """Keeps a captain's diary. Creates file with notes.

    Args:
        lst : list with captain's notes.
        date : the date the notes started.
    """
    file = open('log.txt', 'w')
    for i in range(0, len(lst)):
        file.writelines(['\n' + new_data(date, i) + ' : ' + lst[i]])
    file.close()
