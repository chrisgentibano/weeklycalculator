import datetime

def calc_hrs():
    time_dict = 
    {
        "monday": ["8:30","12:30","1:30","5:30"],
        "tuesday": ["8:30","12:30","1:30","5:30"],
        "wednesday": ["8:30","12:30","1:30","5:30"],
        "thursday": ["8:30","12:30","1:30","5:30"],
        "friday": ["8:30","12:30","1:30","5:30"],
    }
    hours = 0
    for day in time_dict:
        ctr = 0
        for time in time_dict[day]:
            ctr += 1
            if ctr%2 == 1:
                start_time = time
            elif ctr%2 == 0:
                end_time = time

            if (ctr %2 == 0 and end_time):
                time_diff = datetime.datetime.strptime(end_time, '%H:%M') - datetime.datetime.strptime(start_time, '%H:%M')
                hours += (int(time_diff.total_seconds()/60))/60
                print (hours)

calc_hrs()