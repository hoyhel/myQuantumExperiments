class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.total_minutes = self.normaliser()
        self.hours = self.total_minutes // 60
        self.minutes = self.total_minutes % 60

    def normaliser(self):
        self.total_minutes = self.hour * 60 + self.minute
        if self.total_minutes < 0:
            self.total_minutes += 1440
        return self.total_minutes % 1440

    def __repr__(self):
        return f"Clock({self.hours}, {self.minutes})"

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(self.hours, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(self.hours, self.minutes - minutes)
