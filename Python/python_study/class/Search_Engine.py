import os
from Document import Document
import math

class SearchEngine:
    def __init__(self, directory):
        self.directory = directory
        self.dir_len = len(os.listdir(self.directory))
        self.c = {}
        for file_name in os.listdir(self.directory):
            a = Document(self.directory + "/" + file_name)
            for i in a.dic.keys():
                if i not in self.c.keys():
                    self.c[i] = [self.directory + "/" + file_name]
                elif i in self.c.keys():
                    self.c[i].append(self.directory + "/" + file_name)
                    
    
    def _calculate_idf(self, word):
        count = len(self.c[word])
        return math.log(self.dir_len / count)
    
    