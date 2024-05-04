import time


class BirthDay:
    def __init__(self, year, month, day, hour, minute, second):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def calculate_age(self):
        current_time = time.localtime()
        current_year = current_time.tm_year
        # current_month = current_time.tm_mon
        # current_day = current_time.tm_mday
        # current_hour = current_time.tm_hour
        # current_minute = current_time.tm_min
        # current_second = current_time.tm_sec

        return current_year - self.year
        
    
    def calculate_time_remaining(self):
        current_time = time.localtime()
        current_year = current_time.tm_year
        current_month = current_time.tm_mon
        current_day = current_time.tm_mday
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        current_second = current_time.tm_sec

        remaining_years = abs(current_year -self.year)
        remaining_months = abs(current_month - self.month)
        remaining_days = abs(current_day - self.day)
        remaining_hours = abs(current_hour - self.hour)
        remaining_minutes = abs(current_minute - self.minute)
        remaining_seconds = abs(current_second - self.second)


        return remaining_years, remaining_months, remaining_days, remaining_hours, remaining_minutes, remaining_seconds


    @classmethod
    def is_valid_date(cls, year, month, day, hour, minute, second) :

        if year > 2023 or year <= 0 :
            raise Exception ('not valid date \n The year must not be zero or negative')
        if month < 1 or month > 12 :
            raise Exception ('not valid date \n The number of months of the year must be between 1 and 12')
        if day > 31 or day < 1 :
            raise Exception ('not valid date \n The number of days in the month must be between 1 and 31 days')
        if hour >= 24 :
            raise ValueError('House number should be less than 23.')
        if minute >= 60 :
            raise ValueError('minute number should be less than 60.')
        if second >= 60 :
            raise ValueError('second number should be less than 60.')
        
        return cls(year, month, day, hour, minute, second)


while True :
    try: 
        year = int(input("Please enter the year of birth : "))
        month = int(input("Please enter the month of birth: "))
        day = int(input("Please enter the day of birth: "))
        hour = int(input("Please enter the hour of birth: "))
        minute = int(input("Please enter the minute of birth: "))
        second = int(input("Please enter the second of birth: "))
        break
    except ValueError as e :
        print('Invalid input. please try again.')


birthday = BirthDay.is_valid_date(year, month, day, hour, minute, second)
age = birthday.calculate_age()
remaining_time = birthday.calculate_time_remaining()

print(f"Age: {age} years")
print(f"Remaining Time: {remaining_time[0]} years, {remaining_time[1]} months, {remaining_time[2]} days, {remaining_time[3]} hours, {remaining_time[4]} minutes, {remaining_time[5]} seconds")





# روش دوم
# class BirthDay:
    

#     def __init__(self, year, month, day, hour, minute, second, wday, yday, isdst):
#         self.birth_time = time.mktime((year, month, day, hour, minute, second, wday, yday, isdst))
#         print(self.birth_time)

    

#     def calculate_age(self):
#         current_time = time.time()
#         age_in_seconds = current_time - self.birth_time
#         age_in_years = age_in_seconds / (365 * 24 * 60 * 60)  
#         return int(age_in_years)


#     def time_to_birthday(self):
#         current_time = time.time()
#         print(f'current {current_time}')
#         next_birthday = self.birth_time
#         print(f'nextbirth {next_birthday}')

#         if next_birthday < current_time:
#             next_birthday += (365.25 * 24 * 60 * 60)  
#             print(f'next {next_birthday}')

#         time_left = current_time - next_birthday
#         print(f'time left{time_left}')
#         return time_left


#     @classmethod
#     def is_valid_date(cls, year, month, day, hour, minute, second, wday, yday, isdst) :

#         if year <= 0 :
#             raise Exception ('not valid date \n The year must not be zero or negative')
#         if month < 1 or month > 12 :
#             raise Exception ('not valid date \n The number of months of the year must be between 1 and 12')
#         if day > 31 or day < 1 :
#             raise Exception ('not valid date \n The number of days in the month must be between 1 and 31 days')
#         if hour >= 24 :
#             raise ValueError('House number should be less than 23.')
#         if minute >= 60 :
#             raise ValueError('minute number should be less than 60.')
#         if second >= 60 :
#             raise ValueError('second number should be less than 60.')
        
#         return cls(year, month, day, hour, minute, second, wday, yday, isdst)


# while True :
#     try: 
#         year = int(input("Please enter the year of birth : "))
#         month = int(input("Please enter the month of birth: "))
#         day = int(input("Please enter the day of birth: "))
#         hour = int(input("Please enter the hour of birth: "))
#         minute = int(input("Please enter the minute of birth: "))
#         second = int(input("Please enter the second of birth: "))
#         break
#     except ValueError as e :
#         print('Invalid input. please try again.')


# wday = time.localtime().tm_wday
# yday = time.localtime().tm_yday
# isdst = time.localtime().tm_isdst


# date = BirthDay.is_valid_date(year, month, day, hour, minute, second, wday, yday, isdst)
# age = date.calculate_age()
# print(f'your age : {age}')



# time_left = date.time_to_birthday()
# days_left = time_left // (24 * 60 * 60)
# print(f" Time left until birth: {days_left} day")
