import pandas as pd
from pysus.online_data.SIH import download

def extract(uf, years):
    months = [i for i in range(1,12+1)]
    parquet_list = download(states=uf, years=years, months=months)
    return pd.concat([pd.read_parquet(parquet) for parquet in parquet_list])

    