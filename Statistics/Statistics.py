from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.SampleMean import sample_mean
import pprint
from CsvReader.CsvReader import CsvReader

class Statistics:
    data = []

    #def __init__(self, filepath):
        #self.data = CsvReader(filepath)
        #super().__init__()

    def mean(self, a, b):
        self.result = mean(a, b)
        return self.result

    def median(self, a, b, c, d):
        self.result = median(a, b,c, d)
        return self.result

    #def sample_mean(self, sample_size):
        #self.result = sample_mean(self.data, sample_size)
        #return self.result