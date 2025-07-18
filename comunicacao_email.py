import yagmail
import pandas as pd
from comunicacao_banco import criar_conexao

with criar_conexao() as conn:
    sql = '''
        SELECT descricao, estilo, codigo, valor, valorCaixa FROM cervejas
    '''
    df = pd.read_sql(sql, conn)

df = df.fillna('')

tabela = df.to_html(border=False, index=False)
df.to_csv('cervejas.csv')

senha_app = 'krya tfya zywb tabq'
email = yagmail.SMTP('thomas.jdweidner@gmail.com', senha_app)
#html = 'Olá!<p>Seguem as nossas <strong>ofertas:</strong></p>'+tabela
email.send(
    to='thomas.jdweidner@gmail.com',
    subject='Email com Yagmail',
    contents=tabela,
    attachments='cervejas.csv',
)