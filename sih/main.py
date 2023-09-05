from etl import *

# comandos: 
# docker image build -t sihsus .
# docker container run --network=host -it  sihsus

ufs='es'
years=[2021]

sih = extract(uf=ufs, years=years)
print('Extração Concluída')
transf(sih)
treat_na(sih)

conection = conect( 
    host='host.docker.internal',
    passr='0807',
    port='5432', 
    user='postgres', 
    data='sih_es'
)

print('Conexao com o Banco Concluida')
load_sih(df=sih, conn=conection)
print('Carregamento no Banco Concluido')
