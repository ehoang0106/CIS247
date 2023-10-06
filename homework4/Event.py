class Event:
    def __init__(self, event_name, event_date, start_hour, end_hour):
        self._event_name = event_name
        self._event_date = event_date
        self._start_hour = start_hour
        self.valid_hour(start_hour)
        self._end_hour = end_hour
        self.valid_hour(end_hour)
        """For the check_overnight, please see the note below"""
        #self.check_overnight(end_hour)
        

    @property
    def event_name(self):
        return self._event_name
    @event_name.setter
    def event_name(self, new_event_name):
        self._event_name = new_event_name

    @property
    def event_date(self):
        return self._event_date
    @event_date.setter
    def event_date(self, new_event_date):
        self.event_date = new_event_date

    @property
    def start_hour(self):
        return self._start_hour
    @start_hour.setter
    def start_hour(self, new_start_hour):
        self.valid_hour(new_start_hour)
        self._start_hour = new_start_hour
    
    @property
    def end_hour(self):
        return self._end_hour
    
    @end_hour.setter
    def end_hour(self, new_end_hour):
        self.valid_hour(new_end_hour)
        #self.check_overnight(new_end_hour)
        self._end_hour = new_end_hour   
        
        

    def valid_hour(self, hour):
        if hour < 0 or hour > 23:
            raise ValueError("Invalid value. Value should be between 0 and 23")
           
    """
    Dear professor,

    I do not know that we should rasie an ValueError or just let the user input enter the correct value
    So I create this method in case you won't grade.

    """
    # def check_overnight(self, hour):
    #     if hour < self._start_hour:
    #         raise ValueError("Events not go past midnight. End hour must be great than start hour") 
    
    def __str__(self):
        return f'\nEvent name: {self._event_name}\nEvent start from {self._start_hour}:00 to {self._end_hour}:00\nEvent date: {self._event_date}\n'
    
    def has_overlap(self, other):
        
            if self._event_date == other._event_date:
                if (self._start_hour == other._start_hour or self._end_hour == other._end_hour) \
                    or (other._start_hour < self._end_hour and other._start_hour > self._start_hour) \
                    or (other._end_hour > self._start_hour and other._end_hour < self._end_hour) \
                    or (other._start_hour > self._start_hour and other._end_hour < self._end_hour) \
                    or (other._start_hour == self._end_hour ):
                    return True
                else:
                    return False
            else:
                return False
        
