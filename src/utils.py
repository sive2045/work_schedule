import datetime
 
def what_day_is_today():
    now = datetime.datetime.now()
    t = ['Monday', 'Tuseday', 'Wednseday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    r = datetime.datetime.today().weekday()
    day = str(now.year) + '-' + str(now.month).rjust(2, '0') + '-' + str(now.day).rjust(2, '0') + '\n' + t[r]
    return day

def cal_achievement_rate(total_time, goal_time):
    ach_time = str(round(total_time/goal_time, 2) * 100).rjust(2, '0') + ' %'
    return ach_time

if __name__ == "__main__":
    day = what_day_is_today()
    print(day)