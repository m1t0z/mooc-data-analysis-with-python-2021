#!/usr/bin/env python3

import pandas as pd


def best_record_company() -> pd.DataFrame():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df_grouped_by_publisher = df.groupby("Publisher")
    best_publisher_idx = df_grouped_by_publisher["WoC"].sum().idxmax()
    return df_grouped_by_publisher.get_group(best_publisher_idx)


def main():
    print(best_record_company())


if __name__ == "__main__":
    main()
