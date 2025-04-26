# This is a function that accepts a given time and day of the week, as well as an amount of time to add, and outputs the new time and day. 

def add_time(start, duration, day=''):

    if duration == '0:00':
        return start
    
    #first lets search until the : and sort this into variables
    AMPM = ''
    for digit in start:
        if digit.isupper():
            AMPM += digit
        index = start.find(':')
        hours = start[:index]
        minutes = start[index+1:5]

    #sorting duration
    for digit in duration:
        durindex = duration.find(':')
        durhours = duration[:durindex]
        durminutes = duration[durindex+1:]
    
    #this finds the remainder, which we need to add before the 12 check.    

    #now adding the times 
    newhours = (int(hours) + (int(durhours)))
    newminutes = (int(minutes) + int(durminutes))
    nextday = 0

    whichday = 0
    day = day.capitalize()
    daysoftheweek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day != '':
        whichday = daysoftheweek.index(day)

    #rules for hours and AM/PM
    #nextday = int(durhours) // 24

    while newhours > 12:
        if AMPM == 'AM':
            newhours = newhours - 12
            AMPM = 'PM'

        else:
            newhours = newhours - 12
            AMPM = 'AM'
            #also make it the next day here
            nextday += 1
            whichday += 1
            if whichday == 7:
                whichday = 0

    #rules for mintes
    if newminutes >= 60:
        newminutes = ('0' + str(newminutes - 60))
        if newhours == 11 and AMPM == 'PM':
            nextday += 1
            AMPM = 'AM'
            whichday += 1
        elif newhours == 11 and AMPM == 'AM':
            AMPM = 'PM'
        newhours += 1


    #formatting our output
    if day == '':
        if nextday == 0:
            new_time = f'{str(newhours)}:{str(newminutes)} {AMPM}'
        elif nextday == 1:
            new_time = f'{str(newhours)}:{str(newminutes)} {AMPM} (next day)'
        else:
            new_time = f'{str(newhours)}:{str(newminutes)} {AMPM} ({nextday} days later)'
    
    else:
        if nextday == 0:
            new_time = f'{str(newhours)}:{str(newminutes)} {AMPM}, {daysoftheweek[whichday]}'
        elif nextday == 1:
            new_time = f'{str(newhours)}:{str(newminutes)} {AMPM}, {daysoftheweek[whichday]} (next day)'
        else:
            new_time = f'{str(newhours)}:{str(newminutes)} {AMPM}, {daysoftheweek[whichday]} ({nextday} days later)'

    return new_time

print(add_time('11:43 PM', '24:20', 'tueSday'))
