import pandas as pd 
import dics 

def transf(df):
                                                                                                                                                                                                                                                                                                                                                                       
    if 'SEXO' in df.columns:
        df['SEXO'] = df['SEXO'].replace(dics.sexo)

    if 'RACA_COR' in df.columns: 
        df['RACA_COR'] = df['RACA_COR'].replace(dics.racacor)

    if 'IDENT' in df.columns:
        df['IDENT'] = df['IDENT'].replace(dics.ident)

    if 'MARCA_UTI' in df.columns:
        df['MARCA_UTI'] = df['MARCA_UTI'].replace(dics.marcauti)

    if 'INSTRU' in df.columns:
        df['INSTRU'] = df['INSTRU'].replace(dics.instru)

    if 'MORTE' in df.columns:
        df['MORTE'] = df['MORTE'].replace(dics.morte)
        
    if 'INFE_HOSP' in df.columns:
        df['INFE_HOSP'] = df['INFE_HOSP'].replace(dics.infehosp)

    df.columns = df.columns.str.lower()
    df.reset_index(inplace=True)   
    df.rename(columns={'index':'id'}, inplace=True)
    df.set_index('id', inplace=True)    
    df.drop(columns=['level_0','level_1','level_2'], inplace=True) 