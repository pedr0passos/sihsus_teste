import pandas as pd
from pysus.online_data.SIH import download

def extract(uf, years):
    months = [1,2]
    parquet_list = download(states=uf, years=years, months=months)
    return pd.concat([pd.read_parquet(parquet) for parquet in parquet_list])
