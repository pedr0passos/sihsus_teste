from etl import *

ufs='es'
years=[2021]

sih = extract(uf=ufs, years=years)
treat_na(sih)
transf(sih)
treat_municipios(sih)

# conection = conect(
#     host='host.docker.internal',
#     passr='0807',
#     port='5432',
#     user='postgres'
# )

# load(df=sih, conection=conection)

print(sih['munic_res','nome_munic_res'])

