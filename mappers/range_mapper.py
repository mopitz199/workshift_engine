class RangeMapper(object):
    def __init__(self, starting_date, ending_date):
        self.starting_date = starting_date
        self.ending_date = ending_date
        super(RangeMapper, self).__init__()

    def __len__(self):
        return (self.ending_date - self.starting_date).days