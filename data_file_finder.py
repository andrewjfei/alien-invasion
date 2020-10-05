import sys
import os

class DataFileFinder:
    """Helps locate frozen data files."""
    def find_data_file(self, filename, type):
        if getattr(sys, 'frozen', False):
            # The application is frozen.
            datadir = os.path.dirname(sys.executable)
        else:
            # The application is not frozen.
            datadir = os.path.dirname(__file__)
            datadir += f"/assets/{type}/"
        return os.path.join(datadir, filename)