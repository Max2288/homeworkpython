def checker(day:int,month:int,year:int):
    if month < 1 or month >12:
        return False
    if day < 1 or day >31:
        return False
    flag = True
    if year %4 == 0 and year %100!=0 or (year % 100 == 0 and year % 400 == 0):
        flag = False 
    if flag == False and month == 2:
        if day <1 or day >29:
            return False
    if month == 1:
        if day <1 or day>31:
            return False
    if month ==2 and flag ==True:
        if day <1 or day >28:
            return False
    if month ==3:
        if day <1 or day >31:
            return False
    if month ==4:
        if day <1 or day >30:
            return False
    if month ==5:
        if day <1 or day >31:
            return False
    if month ==6:
        if day <1 or day >30:
            return False
    if month ==7:
        if day <1 or day >31:
            return False
    if month ==8:
        if day <1 or day >31:
            return False
    if month ==9:
        if day <1 or day >30:
            return False
    if month ==10:
        if day <1 or day > 31:
            return False
    if month ==11:
        if day <1 or day >30:
            return False
    if month ==12:
        if day <1 or day > 31:
            return False
    else:
        return True
