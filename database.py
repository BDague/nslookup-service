
class DatabaseInterface(object):

    """Docstring for DatabaseInterface. """

    def __init__(self):
        """TODO: to be defined1. """

        self.table = {}


    def add(self, key, value):
        self.table[key] = value
    
    def remove(self, key):
        del self.table[key]
