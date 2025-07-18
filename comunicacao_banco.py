import pymysql

def criar_conexao():
    return pymysql.connect(
    host='tramway.proxy.rlwy.net',
    user='root',
    password='UqGjLPfUGrROCWvyeAmICcWNtKCwpgek',
    port=19958,
    database='railway'
    )

with criar_conexao() as conn:
    cursor = conn.cursor()
    sql = '''
    create table if not exists cervejas(
        id int primary key auto_increment,
        descricao varchar(255) not null,
        estilo varchar(255) not null,
        codigo varchar(255) not null,
        valor decimal(10,2) not null,
        valorCaixa decimal(10,2));
    '''
    cursor.execute(sql)
    conn.commit()
    cursor.close()

#cursor = conn.cursor()
#sql_dropar_tabela = 'DROP TABLE cervejas;'
#sql_criacao_tabela = '''
##id INT PRIMARY KEY AUTO_INCREMENT,
#descricao VARCHAR(255) NOT NULL,
#estilo VARCHAR(255) NOT NULL,
#codigo VARCHAR(255) NOT NULL,
#valor DECIMAL(10,2) NOT NULL,
#valor_caixa DECIMAL(10,2),
#dataCadastro DATETIME default NOW()
#);
#'''
#cursor.execute(sql_criacao_tabela)
#conn.commit()
#cursor.close()
#conn.close()
