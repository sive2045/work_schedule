import datetime
 
def what_day_is_today():
    now = datetime.datetime.now()
    t = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday()
    day = str(now.year) + '-' + str(now.month).rjust(2, '0') + '-' + str(now.day).rjust(2, '0') + '\n' + t[r] + '요일'
    return day

if __name__ == "__main__":
    day = what_day_is_today()
    print(day)