from scrapping import dados_produtos

class CategoriaProdutos:
    def __init__(self, nome):
        self.nome = nome
        self.tags = []

    def adicionar_tags(self, produto):
        self.tags.append(produto)

    def mostrar(self):
        texto = ''
        for produto in self.tags:
            texto += f"{produto['Nome']} | Preço: {produto['Preço']} | Preço Antigo: {produto['Preço Antigo']} \n{produto['Link']}\n\n"
        return texto
    

