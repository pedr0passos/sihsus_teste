from teste_load import *
import sqlalchemy as sa

con = conect(
    host='host.docker.internal',
    data='teste',
    passr='0807',
    port='5432',
    user='postgres'
)

df = pd.DataFrame([['pedro',320150],['catterina',320140]], columns=['nome','munic_res'])
aux = pd.read_csv('./MUNIC_BR.csv', sep=';')

aux.rename(columns={'cod':'munic_res', 'value':'nome_munic_res'}, inplace=True)

df = pd.merge(df, aux, on='munic_res')

con.execute(sa.text('ALTER TABLE pessoa ADD nome_munic_res text;'))

load_sih(conn=con, df=df)

