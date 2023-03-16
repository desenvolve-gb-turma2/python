import uuid
import os

class Utils:
    """ 
    Class utils. This class store methods used by different classes
    """
    def get_unique_file_name(self):
        """Generate unique sequence. I will use this unique sequence as a filename"""
        return str(uuid.uuid4())

    def get_current_directory(self):
        """Get current directory path"""
        return os.getcwd()
