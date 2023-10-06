class Event:

    # constructor for initializing instance members
    def __init__(self, event_name, start_hour, end_hour, event_date):
        self.event_name = event_name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.event_date = event_date

    # overriding __str__ as per requirements
    def __str__(self):
        return self.event_name + ' ' + str(self.start_hour) + ' ' + str(self.end_hour) + ' ' + str(self.event_date)

    # getters and setters for instance members
    def get_event_name(self):
        return self.__event_name

    def set_event_name(self, value):
        self.__event_name = value

    def get_start_hour(self):
        return self.__start_hour

    def set_start_hour(self, value):
        if value < 0 and value > 23:
            raise ValueError('Value of start hour must be batween 0 and 23')
        self.__start_hour = value

    def get_end_hour(self):
        return self.__end_hour

    def set_end_hour(self, value):
        if value < 0 and value > 23:
            raise ValueError('Value of end hour must be batween 0 and 23')
        if value < self.start_hour:
            raise ValueError('Events cannot go past midnight i.e. only single day events are allowed')
        self.__end_hour = value

    def get_event_date(self):
        return self.__event_date

    def set_event_date(self, value):
        self.__event_date = value

    # making properties of the the required instance members
    event_name = property(get_event_name, set_event_name)
    start_hour = property(get_start_hour, set_start_hour)
    end_hour = property(get_end_hour, set_end_hour)
    event_date = property(get_event_date, set_event_date)