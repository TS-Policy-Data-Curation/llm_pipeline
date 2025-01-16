import pandas as pd
import argparse
from ast import literal_eval


def split_data(data, frac=0.8):
    d: dict = literal_eval(data)
    items = list(d.items())
    split_point = int(len(items) * frac)
    return pd.Series([items[:split_point], items[split_point:]])


def split(data: pd.DataFrame):
    data[["history", "forecast"]] = data["data"].apply(split_data)
    data.drop(columns=["data", "last_updated"], axis=1, inplace=True)
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fred_path", type=str, help="Path to the FRED data")
    args = parser.parse_args()
    data = pd.read_csv(args.fred_path)
    df = split(data)
    df.to_csv("fred_split.csv")
