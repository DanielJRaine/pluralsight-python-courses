"""reader reads files"""

class Reader(object):
    """Opens, reads, and closes files"""
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'rt')

    def close(self):
        """Closes file"""
        self.file.close()

    def read(self):
        """Reads file"""
        return self.file.read()
