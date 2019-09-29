class DayFacade(object):

    def __init__(self, day):
        self.day = day

    def is_working_day(self):
        return (self.day.starting_time is not None and
                self.day.ending_time is not None)
