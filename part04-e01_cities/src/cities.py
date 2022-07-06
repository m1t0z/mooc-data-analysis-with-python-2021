#!/usr/bin/env python3

import pandas as pd


def cities() -> pd.DataFrame:
    index = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    s_population = pd.Series([643272, 279044, 231853, 223027, 201810], index)
    s_area = pd.Series([715.48, 528.03, 689.59, 240.35, 3817.52], index)
    return pd.DataFrame({"Population": s_population, "Total area": s_area})


def main():
    print(cities())


if __name__ == "__main__":
    main()
