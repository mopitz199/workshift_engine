class DifferencesOperator(object):
    """
    Class to check and process the differences
    after all the assigns and unasigns
    """

    def __init__(self, db):
        self.db = db

    def get_all_db_difference_ranges(self):
        """
        Function to get all the range that represent
        a difference of assignation between the data in
        the database and the RAM database
        """

        ranges = []

        for assign in self.db.to_be_updated:
            left, right = assign.get_differences()
            if left:
                ranges.append(left)
            if right:
                ranges.append(right)

        for assign in self.db.to_be_deleted:
            ranges.append(assign.range_mapper)

        for assign in self.db.to_be_created:
            ranges.append(assign.range_mapper)

        return ranges

    def process_diferences(self):
        differences = self.get_all_db_difference_ranges()
