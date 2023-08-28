import pandas as pd 
import sqlalchemy as sa 

def read_cid_csv(file, sep):
    df = pd.read_csv(file, sep=sep)
    df.columns = [col.lower() for col in df.columns]

    return df

def load_cid(df, con, table, chunck):
    df.to_sql(name=table, con=con, if_exists='append', index=False, chuncksize=chunck)

def run_capitulos(con, table, sep=';', chunck=12000):
    file = "https://github.com/bigdata-icict/ETL-Dataiku-DSS/blob/master/SIM/cid10_tabela_capitulos.csv?raw=true"
    df = read_cid_csv(file, sep)
    load_cid(df=df, con=con, table='cid10_capitulos', chunck=chunck)

def run_categorias(con, table, sep=';', chunck=12000):
    file = "https://github.com/bigdata-icict/ETL-Dataiku-DSS/blob/master/SIM/CID-10-CATEGORIAS.CSV.utf8?raw=true"
    df = read_cid_csv(file, sep)
    load_cid(df=df, con=con, table='cid10_categorias', chunck=chunck)

def run_categorias(con, table, sep=';', chunck=12000):
    file = "https://github.com/bigdata-icict/ETL-Dataiku-DSS/blob/master/SIM/CID-10-SUBCATEGORIAS.CSV.utf8?raw=true"
    df = read_cid_csv(file, sep)
    load_cid(df=df, con=con, table='cid10_subcategorias', chunck=chunck)