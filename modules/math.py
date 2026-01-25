
import pandas as pd


def count_(col):
    count = 0
    for value in col:
        if pd.notna(value):
            count += 1
    return count

def sum_(col):
    total = 0
    for value in col:
        if pd.notna(value):
            total += value
    return total

def mean_(col):
    return sum_(col)/count_(col)

def sort_(col):
    values = [value for value in col if pd.notna(value)]
    for i in range(count_(col)):
        for j in range(count_(col) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    return values

def quantile_(col, fraction):
    values = sort_(col)
    n = len(values)
    index = (n - 1) * fraction
    low = int(index)
    high = low + 1
    frac = index - low

    if frac == 0:
        return values[low]
    return values[low] + (values[high] - values[low]) * frac

def std_(col):
    mean = mean_(col)
    values = [value for value in col if pd.notna(value)]
    squared_diffs = [(value - mean) ** 2 for value in values]
    variance = sum(squared_diffs) / (len(squared_diffs) - 1)
    return variance ** 0.5

def min_(col):
    min_val = float("inf")
    for value in col:
        if pd.notna(value) and value < min_val:
            min_val = value
    return min_val

def max_(col):
    max_val = float("-inf")
    for value in col:
        if pd.notna(value) and value > max_val:
            max_val = value
    return max_val