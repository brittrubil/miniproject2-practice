
import unittest
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from statistics import pvariance

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()


    def test_mean(self):
        test_data = CsvReader("/Tests/Data/Mean.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.mean(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_median(self):
        test_data = CsvReader("/Tests/Data/Median.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.median(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_mode(self):
        test_data = CsvReader("/Tests/Data/mode.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.mode(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_deviation(self):
        test_data = CsvReader("/Tests/Data/deviation.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stdev(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_variance(self):
        test_data = CsvReader("/Tests/Data/variance.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.pvariance(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_population_deviation(self):
        test_data = CsvReader("/Tests/Data/population_deviation.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.pstdev(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_zscore(self):
        test_data = CsvReader("/Tests/Data/zscore.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.zscore(row['Value 1'], row['Value 2'], row['Value 3']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_sample_mean(self):
        test_data = CsvReader("/Tests/Data/samplemean.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.sample_mean(row['Value 1'], row['Value 2'], row['Value 3']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_proportion(self):
        test_data = CsvReader("/Tests/Data/proportion.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.proportion(row['Value 1'], row['Value 2'], row['Value 3']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_pvalue(self):
        test_data = CsvReader("/Tests/Data/pvalue.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.pvalue(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_sample_mean(self):
        test_data = CsvReader("/Tests/Data/samplemean.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.sample_mean(row['Value 1'], row['Value 2'], row['Value 3']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

    def test_standardscore(self):
        test_data = CsvReader("/Tests/Data/standardscore.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.standardscore(row['Value 1'], row['Value 2'], row['Value 3']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))

if __name__ == '__main__':
    unittest.main()