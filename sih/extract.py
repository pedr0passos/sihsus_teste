import pandas as pd
from pysus.online_data.SIH import download

# def download_pys(estado, ano, mes):
#   aux = download(states=estado, years=ano, month=meses)
#   return pd.concat([pd.read_parquet(v) for v in aux])

def extract_sih(estado, anos, meses, aux):
  for ano in anos:
    for mes in meses:
        aux[mes, ano] = pd.read_parquet(download(estado, ano, mes))
        print(f"O Arquivo do Mês {mes} do Ano {ano} do Estado do {estado.upper()} foi Baixado!")

def concat(aux):
  return pd.concat({k:pd.DataFrame.from_dict(v) for k, v in aux.items()}, axis=0).reset_index()