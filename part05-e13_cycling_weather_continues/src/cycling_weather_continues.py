#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


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


def cycling_weather_continues(station):
    df_weather = pd.read_csv("src/kumpula-weather-2017.csv")

    df_cycling = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Basic cleanup of the cycling table.
    df_cycling = df_cycling.dropna(axis=0, how="all").dropna(axis=1, how="all")

    # Restructure the date-time infomation of the cycling.
    df_cycling_dt: pd.DataFrame = df_cycling["Päivämäärä"].str.split(expand=True)
    df_cycling_dt.columns = ["weekday", "d", "m", "Year", "Time"]
    df_cycling.drop("Päivämäärä", axis=1, inplace=True)
    df_cycling = pd.concat([df_cycling_dt, df_cycling], axis=1)
    df_cycling["Year"] = pd.to_numeric(df_cycling["Year"])
    df_cycling["m"] = pd.to_numeric(df_cycling["m"].map(convert_month))
    df_cycling["d"] = pd.to_numeric(df_cycling["d"])

    # Limit cycling table to 2017 year only.
    df_cycling = df_cycling[df_cycling["Year"] == 2017]

    # Sums of cycling counts for each day.
    df_cycling = df_cycling.groupby(["Year", "m", "d"], as_index=False).sum()

    # Merge 2 dataframes.
    df = df_cycling.merge(df_weather, on=["Year", "m", "d"])

    # Fill missing values with forward fill.
    df.fillna(method="ffill", inplace=True)

    # Use linear regression to explain the dependency between number of stops (for specific stations) and weather conditions.
    explanatory_columns = [
        "Precipitation amount (mm)",
        "Snow depth (cm)",
        "Air temperature (degC)",
    ]
    explained_column = station

    model = LinearRegression(fit_intercept=True)
    X = df[explanatory_columns]
    Y = df[explained_column]
    coeff = model.fit(X, Y).coef_
    score = model.score(X, Y)
    return (coeff, score)


def main():
    station = "Baana"
    ((c_p, c_sd, c_t), score) = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {c_p:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {c_sd:.1f}")
    print(f"Regression coefficient for variable 'temperature': {c_t:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
