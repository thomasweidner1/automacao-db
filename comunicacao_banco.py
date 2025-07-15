import pymysql

def criar_conexao():
    return pymysql.connect(
    host='yamanote.proxy.rlwy.net',
    user='root',
    password='ImDgrtWBmDmisAfAvOFxVrwJsGazWLyi',
    port=24227,
    database='railway'
    )

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
