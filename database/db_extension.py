class DBExtension(object):

    def is_in_real_db(self):
        """
        To check if the element is saved in the real database

        :rtype: Boolean
        """

        id = getattr(self, 'id', None)
        return id is not None
