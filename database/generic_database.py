from operators.assignation_operator import AssignationOperator


class DB(object):
    """
    A base class to operate a class with a lot of instances
    as a random access memory database
    """

    def __init__(self, elements, base_class):
        self.elements = elements
        self.base_class = base_class
        self.db = {}

        self.to_be_updated = []
        self.to_be_created = []
        self.to_be_deleted = []

        self.build_database()

    def hash_function(self, element):
        return ""

    def build_database(self):
        """
        Function to build the database of all given elements
        according to the hash_function
        """

        for element in self.elements:
            self.add(element)

    def add(self, element):
        """
        To add an element in the RAM database

        :param element: The element to add
        :type element: Class
        """

        hash_str = self.hash_function(element)
        if hash_str not in self.db:
            self.db[hash_str] = []
        self.db[hash_str].append(element)
        if not element.is_in_real_db():
            self.to_be_created.append(element)

    def remove(self, element):
        """
        To remove an element in the RAM database

        :param element: The element to remove
        :type element: Class
        """

        hash_str = self.hash_function(element)
        hash_elements = self.db.get(hash_str, [])
        if element in hash_elements:
            hash_elements.remove(element)
        if not hash_elements:
            del self.db[hash_str]
        if element.is_in_real_db():
            self.to_be_deleted.append(element)
            if element in self.to_be_updated:
                self.to_be_updated.remove(element)
        else:
            self.to_be_created.remove(element)

    def update(self, element):
        """
        To update an element in the RAM database

        :param element: The element to update
        :type element: Class
        """
        if element.is_in_real_db():
            self.to_be_updated.append(element)
