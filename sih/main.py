import pandas as pd
import load as ld 
import transf as tf 
import extract as ext 
from pysus.online_data.SIH import download
from sqlalchemy import create_engine

meses=[1]
estado='es'
anos=[2021]
dic={}

ext.extract_sih(estado=estado, anos=anos, meses=meses, aux=dic)
sih_es = ext.concat(dic)
sih_es.to_csv('sih_es.csv')
#sih_es = pd.read_csv('sih_es.csv')
tf.transf(sih_es)
print(sih_es)
#ld.load(sih_es)
