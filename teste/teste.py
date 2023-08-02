import pandas as pd
from pysus.online_data.SIH import download

years = [2020,2021]
path_list = download(states='es', years=years, months=1)
df = pd.concat([pd.read_parquet(path) for path in path_list])
print(df)