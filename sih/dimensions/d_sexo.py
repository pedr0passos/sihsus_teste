import pandas as pd
import sqlalchemy as sa

# corrigir leitura do sql 
def extract_d_sexo(con):
    query = """
            WITH sexo as (
                SELECT DISTINCT 
                    NULLIF(sih.sexo, '')::INTEGER AS cod_sexo,
                    CASE NULLIF(sih.sexo,'')::INTEGER
                        WHEN 1 THEN 'Masculino'
                        WHEN 2 THEN 'Feminino'
                        ELSE NULL 
                    END AS desc_sexo,
                FROM sih
                WHERE NULLIF(sih.sexo,'')::INTEGER IN (1,2)
            )
            SELECT * FROM sexo
            LEFT JOIN d_sexo ON (sexo.cod_sexo = d_sexo.cod_sexo)
            WHERE d_sexo.cod_sexo IS NULL
            """
    query = sa.text(query)
    return pd.read_sql_query(query, con)

def treat_d_sexo(df):
    df=df.astype({'cod_sexo':'Int64'})
    # tratar valores nulos 

# def run_d_sexo(con, chunck=12000):


    