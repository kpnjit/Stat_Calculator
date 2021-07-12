import math
from Statistics.Variance import variance


def standard_deviation(data):
    var1 = variance(data)
    sta_dev = math.sqrt(var1)
    return sta_dev