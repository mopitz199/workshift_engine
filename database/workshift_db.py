from database.generic_database import DB


class WorkshiftDB(DB):
    """
    Class to operate instances of WorkshiftMapper class as a RAM database
    """

    def hash_function(self, element):
        """A function to et the key from where we must save and get the data"""

        return '{}_{}'.format(element.id, element.company_id)
