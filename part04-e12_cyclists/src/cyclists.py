#!/usr/bin/env python3

import pandas as pd


def cyclists() -> pd.DataFrame:
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df_clean = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    return df_clean


def main():
    df = cyclists()
    print(df)


if __name__ == "__main__":
    main()
