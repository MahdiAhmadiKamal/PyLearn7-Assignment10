class Date:
    def __init__(self, y, m, d):
        #properties
        self.year = y
        self.month = m
        self.day = d

    #methods
    def format(self):  #day.month.year or month.day.year
        ...
    def conversion(self): #AD to Hijri
        ...
    def day_count(self):
        ...