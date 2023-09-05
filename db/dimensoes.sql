CREATE TABLE IF NOT EXISTS d_sexo (
    cod_sexo int PRIMARY KEY, 
    desc_sexo text
);

CREATE TABLE IF NOT EXISTS d_raca_cor (
    cod_raca_cor int PRIMARY KEY,
    desc_raca_cor text
);

CREATE TABLE IF NOT EXISTS d_cid (
    cod_cid int PRIMARY KEY,
    categoria  text,
    subcategoria text
);

CREATE TABLE IF NOT EXISTS d_ocupacao (
    cod_ocupacao int PRIMARY KEY,
    desc_ocupacao text
);

CREATE TABLE IF NOT EXISTS d_procedimento (
    cod_procedimento int PRIMARY KEY,
    desc_procedimento text
);

CREATE TABLE IF NOT EXISTS d_municipio (
    cod_municipio int PRIMARY KEY,
    nome_municipio, text
    cod_munic_normalizado int, 
    cod_uf int,
    desc_uf  text,
    nome_uf text,
    cod_regiao, 
    desc_regiao text
);

CREATE TABLE IF NOT EXISTS d_especialidade ( 
    cod_especialidade int PRIMARY KEY, 
    desc_especiliade text
);