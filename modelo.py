class filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


    @property    
    def likes(self):
        return self.__likes
    
    def input_like(self):
        self.__likes += 1

class serie:
    
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas

vingadores = filme('vingadores - guerra infinita', 2018, 160)
suits = serie('suits - homens de terno', 2010, 2)

for t in range(5):
    vingadores.input_like()
    print(f'likes aplicados {t+1}')

vingadores.nome = 'vingadores - ultimato'

print(f"""
    Nome: {vingadores.nome}
    Ano: {vingadores.ano}
    Duração: {vingadores.duracao}
    likes: {vingadores.likes}
""")
print('--'*20)
print(f"""
    Nome: {suits.nome}
    Ano: {suits.ano}
    Duração: {suits.temporadas}
""")

        