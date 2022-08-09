## Fill in the following methods for the class 'Clock'


class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        disp_min = self.minutes
        disp_hr = self.hour
        if len(str(disp_min)) == 1:
            disp_min = "0" + str(disp_min)
        if len(str(disp_hr)) == 1:
            disp_hr = "0" + str(disp_hr)
        return f"{disp_hr}:{disp_min}"

    ## Add time
    ## Don't return anything
    def __add__(self, minutes):
        if self.minutes + minutes < 60 and minutes < 60:
            self.minutes += minutes
        else:
            if minutes > 1440:
                minutes = minutes % 1440
            total_time = self.hour * 60 + self.minutes
            total_time += minutes

            self.hour = total_time // 60
            self.minutes = total_time % 60

        if self.hour > 23:
            self.hour = self.hour - 24
        elif self.minutes < 0:
            self.hour = 24 + self.hour

    ## Subtract time
    ## Don't return anything
    def __sub__(self, minutes):
        if minutes < self.minutes:
            self.minutes -= minutes
        else:
            if minutes > 1440:
                minutes = minutes % 1440
            total_time = self.hour * 60 + self.minutes
            total_time -= minutes

            self.hour = total_time // 60
            self.minutes = total_time % 60
        if self.hour > 23:
            self.hour = self.hour - 24
        elif self.hour < 0:
            self.hour = 24 + self.hour
            # fix 4:05 - 6

    ## Are two times equal?
    def __eq__(self, other):
        return f"{self.hour}:{self.minutes}" == other

    ## Are two times not equal?
    def __ne__(self, other):
        return f"{self.hour}:{self.minutes}" != other


# You should be able to run these
clock1 = Clock(23, 5)
print(clock1)  # 23:05
clock2 = Clock(12, 45)
print(clock2)  # 12:45
clock3 = Clock(12, 45)
print(clock3)  # 12:45

print(clock1 == clock2)  ## False
print(clock1 != clock2)  ## True
print(clock2 == clock3)  ## True

print("testing addition")
clock1 + 60
print(clock1)  # 00:05
print(clock1 == Clock(0, 5))  # True

print("testing subtraction")
clock1 - 100
print(clock1)  # 22:25
