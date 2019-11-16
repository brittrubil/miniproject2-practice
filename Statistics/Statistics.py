from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Deviation import deviation
from Statistics.Variance import variance
from Statistics.PopulationDeviation import population_deviation
from Statistics.Zscore import zscore
from Statistics.SampleMean import sample_mean
from Statistics.Proportion import proportion
from Statistics.Pvalue import pvalue
from Statistics.SampleMean import sample_mean
from Statistics.StandardScore import standardscore
from Statistics.VariancePopulationProportion import populationproportion
import pprint
from CsvReader.CsvReader import CsvReader

class Statistics:
    data = []

    def mean(self, a, b):
        self.result = mean(a, b)
        return self.result

    def median(self, a, b, c, d):
        self.result = median(a, b, c, d)
        return self.result

    def mode(self, a, b, c, d):
        self.result = mode(a, b, c, d)
        return self.result

    def stdev(self, a, b, c, d, e):
        self.result = deviation(a, b, c, d, e)
        return self.result

    def pvariance(self, a, b, c, d, e, f, g, h):
        self.result = variance(a, b, c, d, e, f, g, h)
        return self.result

    def pstdev(self, a, b, c, d, e, f):
        self.result = population_deviation(a, b, c, d, e, f)
        return self.result

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result

    def sample_mean(self, a, b, c):
        self.result = sample_mean(a, b, c)
        return self.result

    def proportion(self, a, b, c):
        self.result = proportion(a, b, c)
        return self.result

    def pvalue(self, a, b, c, d):
        self.result = pvalue(a, b, c, d)
        return self.result

    def sample_mean(self, a, b, c):
        self.result = sample_mean(a, b, c)
        return self.result

    def standardscore(self, a, b, c):
        self.result = standardscore(a, b, c)
        return self.result

    def populationproportion(self, a, b):
        self.result = populationproportion(a, b)
        return self.result

