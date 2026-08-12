import datetime
class mydate:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def show_date(self):
        print(self.date," /",self.month," /",self.year)
    def show_day(self):
        print(self.date)
    def show_month(self):
        print(self.month)
    def show_year(self):
        print(self.year)
    def is_leap(self):
        if(self.year%4==0):
            print("Leap Year")
        else:
            print("Not A Leap Year")
m=mydate(19,7,2006)
m.show_date()
m.show_day()
m.show_month()
m.show_year()
m.is_leap()
