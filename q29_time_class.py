

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def add(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes
        hours = self.hours + other.hours

        if seconds >= 60:
            seconds -= 60
            minutes += 1
        if minutes >= 60:
            minutes -= 60
            hours += 1

        return Time(hours, minutes, seconds)

time1 = Time(2, 45, 50)
time2 = Time(1, 30, 20)

print("Time 1:", end=" ")
time1.display()
print("Time 2:", end=" ")
time2.display()

result_time = time1.add(time2)
print("Time 1 + Time 2 =", end=" ")
result_time.display()
