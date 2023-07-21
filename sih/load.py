import pandas as pd 
from sqlalchemy import create_engine

def conect(server, user, passr, port, data):
    conn = f'postgresql+psycopg2://{user}:{passr}@{server}:{port}/{data}'
    return create_engine(conn)

def load(df):
    df.to_sql('sih', con=engine, if_exists='append', chunksize=5000, method='multi')

#def create_database():
