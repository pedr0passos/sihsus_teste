import pandas as pd

aux = pd.read_csv("./bases_auxiliares/MUNIC_BR.csv", sep=';')
colunas = ['cod', 'text']
df = pd.DataFrame([[110034, 'text'],[539999,'text']], columns=colunas)
aux.rename(columns={'value':'value1'}, inplace=True)
df = pd.merge(df, aux, how='left', on=['cod'])
print(df)

