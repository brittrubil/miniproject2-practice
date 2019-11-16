from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Deviation import deviation
from Statistics.Variance import variance
from Statistics.PopulationDeviation import population_deviation
from Statistics.Zscore import zscore
from Statistics.Proportion import proportion
from Statistics.Pvalue import pvalue
from Statistics.SampleMean import sample_mean
from Statistics.StandardScore import standardscore
from Statistics.VariancePopulationProportion import populationproportion
from Statistics.Sample_Proportion import sample_proportion
from Statistics.Correlation_Coefficient import correlation_coefficient
from Statistics.Confidence_Interval import confidence_interval

class Statistics(Calculator):
    result = 0
    
     def __init__(self):
        super().__init__()

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

    def sample_proportion(self, a, b, c):
        self.result = sample_proportion(a, b, c)
        return self.result

    def correlation_coefficient(self, a):
        self.result = correlation_coefficient(a)
        return self.result

    def confidence_interval(self, a):
        self.result = confidence_interval(a)
        return self.result
