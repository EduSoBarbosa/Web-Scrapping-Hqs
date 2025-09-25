import requests
from bs4 import BeautifulSoup
from itertools import chain

url = 'https://panini.com.br/desconto-saldao?editorial=DC+Comics&product_list_order=percentage_discount' 
url2 = 'https://panini.com.br/desconto-saldao?editorial=DC+Comics&p=2&product_list_order=percentage_discount'
url3 = 'https://panini.com.br/desconto-saldao?editorial=DC+Comics&p=3&product_list_order=percentage_discount'

response = requests.get(url)
response2 = requests.get(url2)
response3 = requests.get(url3)



soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')
soup3 = BeautifulSoup(response3.text, 'html.parser')
#Procurar links com partes do html
#links_editoriais = soup.select('a[href*="desconto-saldao?editorial="]')
#print(f"Encontrados {len(links_editoriais)} links de editoriais em promoção.")

lista_Produtos = soup.find_all('div', class_="product-item-info")
lista_Produtos2 = soup2.find_all('div', class_="product-item-info")
lista_Produtos3 = soup3.find_all('div', class_="product-item-info")
print(f'Encontramos {len(lista_Produtos) + len(lista_Produtos2) + len(lista_Produtos3)} price box')

dados_produtos = []
def Extrair():    
    for produto_html in chain(lista_Produtos, lista_Produtos2, lista_Produtos3):
        tag_nome = produto_html.find('a', class_='product-item-link') 
        if tag_nome:
            nome = tag_nome.text.strip()
            nome = nome.upper()
            link = tag_nome.get('href', 'x') 
        else:
            continue

        tag_preco = produto_html.find('span', class_='price') 
        if tag_preco:
            preco = tag_preco.text.strip()
            preco = preco.replace("\xa0", '')
        else:
            continue

        tag_preco_antigo = produto_html.find('span', class_='old-price') 
        if tag_preco_antigo:
            preco_antigo = tag_preco_antigo.text.strip()
            preco_antigo = preco_antigo.replace('Preço', '')
            preco_antigo = preco_antigo.replace("\xa0", '')
        else:
            continue

        dados_produtos.append({
            'Nome': nome,
            'Preço': preco,
            'Preço Antigo': preco_antigo,
            'Link': link
        
    })
    print(f'Extração Finalizada')





        


#Extração do nome e link