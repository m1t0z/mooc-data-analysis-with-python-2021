#!/usr/bin/env python3

import pandas as pd


def suicide_fractions() -> pd.Series:
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df["fraction"] = df["suicides_no"] / df["population"]
    return df.groupby("country")["fraction"].mean()


def get_suicides() -> pd.Series:
    s = suicide_fractions()
    return s


def get_temperatures() -> pd.Series:
    df = pd.read_html(
        "src/List_of_countries_by_average_yearly_temperature.html", index_col="Country"
    )[0]

    s = df.iloc[:, 0]

    # Convert unicode minus sign to normal minus sign.
    s = s.str.replace("\u2212", "-")

    s = pd.to_numeric(s)

    return s


def suicide_weather():
    s_suicide = get_suicides()
    s_weather = get_temperatures()
    df_joined = pd.concat([s_suicide, s_weather], axis="columns", join="inner")

    # print(s_suicide)
    # print(s_weather)
    # print(df_joined)

    corr = s_weather.corr(s_suicide, method="spearman")
    return (len(s_suicide), len(s_weather), len(df_joined), corr)


def main():
    (
        suicide_rows,
        temperature_rows,
        common_rows,
        spearman_correlation,
    ) = suicide_weather()

    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {spearman_correlation:.1f}")


if __name__ == "__main__":
    main()
