import pandas as pd 
from sqlalchemy import create_engine

def conect(host, user, passr, port, data):
    conn = f'postgresql+psycopg2://{user}:{passr}@{host}:{port}/{data}'
    return create_engine(conn)

def load(df, conection):
    df.to_sql('sih', con=conection, if_exists='append', chunksize=5000, method='multi')

