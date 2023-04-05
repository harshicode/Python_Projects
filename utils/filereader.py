# how to write a file reader which identifies csv and sas in python

import os
import pandas as pd

class FileReader(abc.ABC):
    @abc.abstractmethod
    def read(self, path):
        pass

class CsvReader(FileReader):
    def read(self, path):
        return pd.read_csv(path)
    
class SasReader(FileReader):
    def read(self, path):
        return pd.read_sas(path)
    
class ReaderFactory:
    def get_reader(self, path):
        _, ext = os.path.splitext(path)
        if ext == '.csv':
            return CsvReader()
        elif ext == '.sas':
            return SasReader()
        else:
            raise ValueError(f'Unsupported file type: {ext}')
        
def get_attributes():
    return ['a', 'b', 'c']

def get_data():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def main():
    reader = ReaderFactory().get_reader('data.csv')
    df = reader.read('data.csv')
    print(df)
    
    reader = ReaderFactory().get_reader('data.sas')
    df = reader.read('data.sas')
    print(df)
    
    reader = ReaderFactory().get_reader('data.txt')
    df = reader.read('data.txt')
    print(df)

if __name__ == '__main__':
    main()

    