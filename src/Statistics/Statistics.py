from Calculator.Calculator import Calculator
from Statistics.Mean import get_mean
from Statistics.Median import get_median
from Statistics.Mode import get_mode
from Statistics.Variance import get_variance
from Statistics.StandardDeviation import get_standard_deviation
from CSVReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = get_mean(data)
        return self.result

    def median(self, data):
        self.result = get_median(data)
        return self.result

    def mode(self, data):
        self.result = get_mode(data)
        return self.result

    def variance(self, data):
        self.result = get_variance(data)
        return self.result

    def standard_deviation(self, data):
        self.result = get_standard_deviation(data)
        return self.result

    pass