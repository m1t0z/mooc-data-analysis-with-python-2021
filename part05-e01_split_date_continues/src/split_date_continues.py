#!/usr/bin/env python3

import pandas as pd


def convert_weekday(weekday: str) -> str:
    eng_by_fi = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun",
    }
    return eng_by_fi[weekday]


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
    df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df["Weekday"] = df["Weekday"].map(convert_weekday)
    df["Day"] = df["Day"].astype(int)
    df["Month"] = df["Month"].map(convert_month)
    df["Year"] = df["Year"].astype(int)
    df["Hour"] = df["Hour"].str.split(":", expand=True)[0].astype(int)
    return df


def split_date_continues() -> pd.DataFrame:
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    df_dates = split_date(df["Päivämäärä"])
    df.drop(["Päivämäärä"], axis="columns", inplace=True)
    df = pd.concat([df_dates, df], axis="columns")
    return df


def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
