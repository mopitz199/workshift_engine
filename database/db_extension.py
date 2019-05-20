class DBExtension(object):
    """
    Class to add extra functionalities to the objects, related
    to database
    """

    def is_in_real_db(self):
        """
        To check if the element is saved in the real database

        :rtype: Boolean
        """

        id = getattr(self, 'id', None)
        return id is not None
