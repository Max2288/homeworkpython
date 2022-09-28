from datetime import date, timedelta
def new_data(cur_date, n):
    """
    :param cur_date : format date(dd.mm.yyyy)
    :param n: decimal number
    :return: datetime time
    
    """
    my_date = [int(i) for i in cur_date.split('.')]
    cur = date(my_date[2],my_date[1],my_date[1])
    interval = timedelta(days=n)
    result = cur + interval
    return result.isoformat()

def captain(lst , date):
    file = open('log.txt','w')
    for i in range(0,len(lst)):
        file.writelines(['\n' + new_data(date,i) + ' : ' + lst[i]])
    file.close()