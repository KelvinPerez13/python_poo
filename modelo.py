class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    #property serve para que eu possa exibir os atributos restritos da classe

    @property
    def ano(self):
        return self._ano
    
    # e o setter para que eu possa altera-los
    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano.title()


    @property    
    def likes(self):
        return self._likes
    
    def input_like(self):
        self._likes += 1


class filme(programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
class serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
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

        