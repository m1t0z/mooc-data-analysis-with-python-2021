#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def convert_month(month: str) -> int:
    fi_months = [
        "tammi",
        "helmi",
        "maalis",
        "huhti",
        "touko",
        "kesä",
        "heinä",
        "elo",
        "syys",
        "loka",
        "marras",
        "joulu",
    ]
    eng_by_fi = dict(zip(fi_months, range(1, 13)))
    return eng_by_fi[month]


def split_date(s: pd.Series) -> pd.DataFrame:
    df = s.str.split(expand=True)
    df.columns = ["weekday", "day", "month", "year", "hour"]
    df.drop(columns=["weekday"], inplace=True)
    df["day"] = df["day"].astype(int)
    df["month"] = df["month"].map(convert_month)
    df["year"] = df["year"].astype(int)
    df["hour"] = df["hour"].str.split(":", expand=True)[0].astype(int)
    return df


def bicycle_timeseries() -> pd.DataFrame:
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")

    df_dates = split_date(df["Päivämäärä"])
    s = pd.to_datetime(df_dates)

    df.set_index(s, inplace=True)
    df.drop(["Päivämäärä"], axis="columns", inplace=True)
    return df


def commute() -> pd.DataFrame:
    df = bicycle_timeseries()
    df = df.loc["2017-08-01":"2017-08-31", :]
    df["Weekday"] = df.index.to_series().dt.dayofweek + 1
    df = df.groupby(["Weekday"]).sum()
    return df


def main():
    df = commute()
    print(df)

    df.plot()
    weekdays = "x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()


if __name__ == "__main__":
    main()
