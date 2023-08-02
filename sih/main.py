import load as ld 
import transf as tf 
import extract as ext 
from sqlalchemy import create_engine

meses=[1]
estado='es'
anos=[2021]
dic={}

ext.extract_sih(estado=estado, anos=anos, meses=meses, aux=dic)
sih_es = ext.concat(dic)
tf.transf(sih_es)
conection = create_engine('postgresql+psycopg2://postgres:0807@host.docker.internal:5432/sih_es')
ld.load(df=sih_es, conection=conection)
print("carregou")
