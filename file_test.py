import urllib.request
import os
import time


class File:
    def __init__(self, href_file):
        self.href = href_file
        self.name = href_file.split('/')[-1]

    def download(self):
        urllib.request.urlretrieve(self.href, self.name)
        while not os.path.isfile(self.name):
            time.sleep(1)
        status = os.path.isfile(self.name)
        return status

    def file_size(self):
        return round(os.path.getsize(self.name) / (1024 * 1024), 2)

    def remove_file(self):
        return os.remove(self.name)