CREATE TABLE IF NOT EXISTS dw.d_sexo (
    sk_sexo int PRIMARY KEY,
    cod_sexo int,
    desc_sexo text
);

CREATE TABLE IF NOT EXISTS dw.d_raca_cor (
    sk_raca_cor int PRIMARY KEY,
    cod_raca_cor int,
    desc_raca_cor text
);

CREATE TABLE IF NOT EXISTS dw.d_cid (
    sk_cid int PRIMARY KEY,
    cod_cid int,
    categoria  text,
    subcategoria text
);

CREATE TABLE IF NOT EXISTS dw.d_ocupacao (
    sk_ocupacao int PRIMARY KEY,
    cod_ocupacao int,
    desc_ocupacao text
);

CREATE TABLE IF NOT EXISTS dw.d_procedimento (
    sk_procedimento int PRIMARY KEY,
    cod_procedimento int,
    desc_procedimento text
);

CREATE TABLE IF NOT EXISTS dw.d_municipio (
    sk_municipio int PRIMARY KEY,
    cod_municipio int,
    nome_municipio, text
    cod_munic_normalizado int, 
    cod_uf int,
    desc_uf  text,
    nome_uf text,
    cod_regiao int, 
    desc_regiao text
);

CREATE TABLE IF NOT EXISTS dw.d_especialidade ( 
    sk_especialidade int PRIMARY KEY,
    cod_especialidade int, 
    desc_especiliade text
);

CREATE TABLE IF NOT EXISTS dw.d_estabelecimento (
    sk_estabelecimento int PRIMARY KEY,
    nu_cnpj_estabelecimento text,
    desc_regime text,
    desc_natureza_juridica text,
    desc_gestao text
)

CREATE TABLE IF NOT EXISTS dw.f_hospitalizacao (
    
);