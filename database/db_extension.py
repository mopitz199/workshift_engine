class DBExtension(object):
    """
    Class to extend the functionalities of a mapper
    in order to work with a database class
    """

    def is_in_real_db(self):
        """
        To check if the element is saved in the real database

        :rtype: Boolean
        """

        id = getattr(self, 'id', None)
        return id is not None