import requests
from bs4 import BeautifulSoup
from comunicacao_banco import criar_conexao

def ajustar_valor(valor_inicial: str) -> float:
    return  float(valor_inicial.replace(',','.').replace('R$',''))

url = 'https://www.stuttgart.com.br/bebidas/cervejas.html'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    for i,card in enumerate(soup.select('#layer-product-list .product-item-details'), start=1):
        descricao = card.select_one('.product-item-link')
        estilo = card.select_one('.german_name')
        codigo = card.select_one('.sku')
        valor = card.select_one('.price')
        valor_caixa = card.select_one('.minimal-price-link .price-wrapper')
        if valor is None:
            continue
        else:
            valor = ajustar_valor(valor.text)
            if valor_caixa is None:
                sql = 'INSERT INTO cervejas (descricao, estilo, codigo, valor) VALUES (%s, %s, %s, %s);'
                dados = (descricao.text.strip(), estilo.text, codigo.text, valor)
            else:
                sql = 'INSERT INTO cervejas (descricao, estilo, codigo, valor, valor_caixa) VALUES (%s, %s, %s, %s, %s);'
                valor_caixa = ajustar_valor(valor_caixa.text)
                dados = (descricao.text.strip(), estilo.text, codigo.text, valor, valor_caixa)

            with criar_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, dados)
                conn.commit()
                cursor.close()
else:
    pass
    #TODO criar lógica para enviar email com aviso de falha
