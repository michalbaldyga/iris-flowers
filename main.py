import pandas as pd
from data_processing import parse_data


if __name__ == '__main__':
    raw_data = pd.read_csv('iris.data', header=None)
    flowers = parse_data(raw_data)
