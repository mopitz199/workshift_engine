from database.generic_database import DB

class AssignationDB(DB):
    """
    Class to operate instances of AssignationMapper class as a RAM database
    """

    def hash_function(self, element):
        """A function to et the key from where we must save and get the data"""
        
        return '{}_{}'.format(element.workshift_id, element.person_id)
