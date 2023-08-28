CREATE TABLE IF NOT EXISTS d_sexo (
    int cod_sexo PRIMARY KEY, 
    text desc_sexo 
);

CREATE TABLE IF NOT EXISTS d_raca_cor (
    int cod_raca_cor PRIMARY KEY,
    text desc_raca_cor
);

CREATE TABLE IF NOT EXISTS d_cid (
    int cod_cid PRIMARY KEY,
    text categoria, 
    text subcategoria
);

CREATE TABLE IF NOT EXISTS d_ocupacao (
    int cod_ocupacao PRIMARY KEY,
    text desc_ocupacao
);

CREATE TABLE IF NOT EXISTS d_procedimento (
    int cod_procedimento PRIMARY KEY,
    text desc_procedimento
);

CREATE TABLE IF NOT EXISTS d_municipio (
    int cod_municipio PRIMARY KEY,
    text nome_municipio,
    int cod_munic_normalizado, 
    int cod_uf,
    text desc_uf, 
    text nome_uf,
    int cod_regiao, 
    text desc_regiao
);

CREATE TABLE IF NOT EXISTS d_especialidade ( 
    int cod_especialidade, 
    text desc_especiliade
);