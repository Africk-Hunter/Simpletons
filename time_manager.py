import time

class TimeManager:
    
    def __init__(self, start_time=480):
        self.current_time = start_time
    
    def advance_time(self):
        if self.current_time == 1440:
            self.current_time = 0
        else:
            self.current_time += 1
            
        time.sleep(.05)
        return self.current_time
    
    def stringify_minutes(self, minutes):
        if minutes < 10:
            minute_string = '0' + str(minutes)
            return minute_string
        else:
            minute_string = str(minutes)
            return minute_string
        
    def create_current_time_for_printing(self, message):
        signifier = ' AM'
        minutes = 0
        if self.current_time < 60:
            hour = 12
            minutes = int(self.current_time)
        elif self.current_time > 720 and self.current_time < 780:
            hour = 12
            minutes = int((self.current_time - (60 * hour)))
            signifier = ' PM'
        elif self.current_time > 779:
            hour = int(self.current_time / 60) - 12
            minutes = int((self.current_time - (60 * (hour + 12))))
            signifier = ' PM'
        else: 
            hour = int(self.current_time / 60)
            minutes = int((self.current_time - (60 * hour)))
        
        statement = "[" + str(hour) + ":" + self.stringify_minutes(minutes) + signifier +  "]: " + message
        print(statement, '\n')
        return

    
