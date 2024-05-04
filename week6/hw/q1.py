import jdatetime
from hijri_converter import Hijri, Gregorian


class Date :
    
    def __init__(self, day, month, year) :
        self.day = day
        self.month = month
        self.year = year

    

    def to_shamsi(self) :
        shamsi_date = jdatetime.date.fromgregorian(day=self.day, month=self.month, year=self.year).strftime('%Y/%m/%d')
        print(type(shamsi_date))
        return shamsi_date

    def to_ghamari(self) :
        qamari_date =Gregorian(day=self.day, month=self.month, year=self.year).to_hijri()
        print(type(qamari_date))

        qamari_year = qamari_date.year
        qamari_month = qamari_date.month
        qamari_day = qamari_date.day

        return f"{qamari_year}/{qamari_month}/{qamari_day}"
        
    
    @classmethod
    def is_valid_date(cls, date_str) :
        day, month, year = map(int, date_str.split('-'))

        if day > 31 or day < 1 :
            raise Exception ('not valid date \n The number of days in the month must be between 1 and 31 days')
        if month < 1 or month > 12 :
            raise Exception ('not valid date \n The number of months of the year must be between 1 and 12')
        if year <= 0 :
            raise Exception ('not valid date \n The year must not be zero or negative')

        return cls(day, month, year)
    

    @staticmethod
    def from_string(date_str) :
        while True:
            parts = date_str.split('-')
            
            if len(parts) == 3:
                day, month, year = parts
                
                if day.isdigit() and month.isdigit() and year.isdigit():
                    day = int(day)
                    month = int(month)
                    year = int(year)
                    break
                else:
                    print("The input is invalid. Please try again.")
            else:
                print("The input format is incorrect. Please try again.")
        
            date_str = input('Enter your date :')

        return 'Done'






print(Date.from_string('10-08-2023'))
# date = Date.is_valid_date('10-11-1995')
date = Date.is_valid_date('10-08-2023')

print(date.day)
print(date.month)
print(date.year)

print(date.to_shamsi())
print(date.to_ghamari())


# Date.is_valid_date('54-32-2')

