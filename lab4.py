import time
import pdb

# Try to use list comprehension and fstring func
# Use PDB
def date_at_hour_offset(h_offset_):
    '''
    Creates a string representation of the date at some specified number of 
    hours from the current time. 

    @param h_offset_ -- int, the hour offset from local time.  Defaults to 168.
    @return -- The string representation of the date at the specified offset 
               from  the local time.  For example:
               "In 4083 hours it will be Saturday, January 4, 2020 
            
    '''


    def is_leap_year(year_):
         ''' 
         Returns True if year_ is a leap year, and False otherwise.
         '''
         if year_ % 4 != 0:
            #leap years are not evenly divisible by 4 
            return False
         if year_ % 400 == 0:
             # but they are evenly diviisble by 400, for example 2000
            return True
         if year_ % 100 == 0:
             # and aside from 400, they are no evenly divisible by
             # multiples of 100
            return False
         
         return True # year_ is a leap year

    # get a collection of time parameters
    t = time.localtime()  
    year       = t[0]
    month      = t[1]   # September is 9
    month_day  = t[2]   # for example, our first midterm is on the 19th
    week_day   = t[6]   # Monday is 0, Thursday 3
    hour       = t[3]   # On a 24-hour clock. Midnight is 0, noon is 12

    weekdays  = ['Monday','Tuesday','Wednesday','Thursday',
                            'Friday','Saturday','Sunday']

    # Months is a complex list representing the names and number of days
    #  of each month. The entry at index 0 is None because time.localtime()
    #  follows the convention of numbering the months starting at 1. Except for
    #  February, the entries are tuples with the format(name,num-days_in_month).
    #  The entry for February is a list, because the number of days changes in
    ### leap years
    months = [None,('January',31),['February',28],('March',31),
      ('April',30),('May',31),('June',30),('July',31),
      ('August',31),('September',30),('October',31),
      ('November',30),('December',31)]

    days = (hour + h_offset_) //24 # It shows how many days
    week_day = (week_day+days) % 7 # How many weekdays


    
    if is_leap_year(year):
        # In leap years Februry has 29 days
        months[2][1] = 29

    while days > 0:
        if  is_leap_year(year):
            if days >= 366:
                year += 1
                days -= 366
            else:
                break
        else:         
            if days >= 365:
                year+=1
                days -= 365
            else:
                if months[month][0] is "January":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "Febuary":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "March":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "April":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "May":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "June":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "July":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "August":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "September":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                    else:
                        break
                elif months[month][0] is "October":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "November":
                    if days > months[month][1]:
                        days -= months[month][1]
                        month += 1
                elif months[month][0] is "December":
                        break
                else: 
                    break




    result = f"In {hour + h_offset_} hours it will be {weekdays[week_day]}, {days} {months[month][0]},{year} "
    print(result)


if __name__ == '__main__':
    #test the function with the cases given below.
    cur_hour = time.localtime()[3]
    base_hour = 23-cur_hour
    print(date_at_hour_offset(base_hour))
    print(date_at_hour_offset(base_hour+1))
    for days in [7,14,70,700, 7000]:
            print(date_at_hour_offset(base_hour+(24*days)))
    