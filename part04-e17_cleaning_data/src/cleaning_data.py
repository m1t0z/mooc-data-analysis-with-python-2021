#!/usr/bin/env python3

import numpy as np
import pandas as pd


def digit_in_words_to_digit(digit_in_words: str) -> int:
    digits_in_words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    digits = range(1, 11)
    digit_by_digit_in_words = dict(zip(digits_in_words, digits))
    return digit_by_digit_in_words[digit_in_words]


def clean_digit_value_column(df: pd.DataFrame, col_name: str):
    m = ~df[col_name].str.isdigit()
    df.loc[m, col_name] = df.loc[m, col_name].map(digit_in_words_to_digit)
    df[col_name] = pd.to_numeric(df[col_name])


def clean_year_value_column(df: pd.DataFrame, col_name: str):
    year = df[col_name].str.split(expand=True)[0]
    df[col_name] = year
    df[col_name] = pd.to_numeric(df[col_name], errors="coerce")


def clean_name_like_column(df: pd.DataFrame, col_name: str):

    # Correct order: <name> <surname>
    m = df[col_name].str.contains(",")
    tmp = df.loc[m, col_name].str.split(",", expand=True)
    df.loc[m, col_name] = tmp[1].str.strip() + " " + tmp[0].str.strip()

    # Correct capitalization.
    name_surname = df[col_name].str.split(expand=True)
    df[col_name] = (
        name_surname[0].str.capitalize() + " " + name_surname[1].str.capitalize()
    )


def cleaning_data() -> pd.DataFrame:
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    clean_name_like_column(df, "President")
    clean_year_value_column(df, "Start")
    clean_year_value_column(df, "Last")
    clean_digit_value_column(df, "Seasons")
    clean_name_like_column(df, "Vice-president")
    return df


def main():
    df = cleaning_data()
    print(df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
