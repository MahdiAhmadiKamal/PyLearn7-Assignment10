class Time:
    def __init__(self, h, m, s):
        #properties
        self.hour = h
        self.minute = m
        self.second = s

    #methods
    def format(self):  #am/pm or 24h
        ...
    def time_duration(self):
        ...
    def time_difference(self): #between two regions
        ...