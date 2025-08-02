import math

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        earth_seconds = 31_557_600
        earth_years = round(self.seconds / earth_seconds, 2)
        return earth_years

    def on_mercury(self):
        orbital_period = 0.2408467
        earth_years = self.on_earth()
        return round(earth_years / orbital_period, 2)

    def on_venus(self):
        orbital_period = 0.61519726 
        earth_years = self.on_earth()
        return math.floor((earth_years / orbital_period) * 100) / 100

    def on_mars(self):
        orbital_period = 1.8808158
        earth_years = self.on_earth()
        return round(earth_years / orbital_period, 2)

    def on_jupiter(self):
        orbital_period = 11.862615
        earth_years = self.on_earth()
        return round(earth_years / orbital_period, 2)

    def on_saturn(self):
        orbital_period = 29.447498
        earth_years = self.on_earth()
        return round(earth_years / orbital_period, 2)

    def on_uranus(self):
        orbital_period = 84.016846
        earth_years = self.on_earth()
        return round(earth_years / orbital_period, 2)

    def on_neptune(self):
        orbital_period = 164.79132
        earth_years = self.on_earth()
        return round(earth_years / orbital_period, 2)
