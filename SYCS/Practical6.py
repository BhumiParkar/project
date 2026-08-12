from datetime import datetime
class mydate:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def calculations(self):
        year=datetime.now().year
        if(year-self.year)>18:
            print("Eligible To Vote")
        elif(year-self.year)>=18:
            print("Not Eligible To Vote")
        else:
            print("Please Input Correct Value")
m=mydate(19,7,2008)
m.calculations()
m=mydate(1,12,2007)
m.calculations()
