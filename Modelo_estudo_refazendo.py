class programas:
    def __init__(self, nome, ano):
       self._nome = nome
       self.ano = ano
       self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # def __str__(self):
    #     return f'{self.nome - self.ano - self.likes}'

    # def imprime(self):
    #     print(f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}')

class filmes(programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # def imprime(self):
    #     print(f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes}')

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes}'

class series(programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # def imprime(self):
    #     print(f"Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes:{self.likes}")

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.temporadas} - Likes: {self.likes}'

class playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        # super().__init__(programas)
        self._programas = programas

    # @property
    # def listagem(self):
    #     return self._programas

    # @property
    # def tamanho(self):
    #     return len(self._programas)

    def __len__(self):
        return len(self._programas)

    def __getitem__(self, item):
        return self._programas[item]


vingadores = filmes("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

# print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} minutos - Likes:{vingadores.likes}")

demolidor = series("demolidor", 2016, 3)
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

# print(f"Nome: {demolidor.nome} - Ano: {demolidor.ano} - Temporadas: {demolidor.temporadas} - Likes:{demolidor.likes}")

tmep = filmes('todo mundo em pânico', 1999, 100)
tmep.dar_like()
tmep.dar_like()

atlanta = series('atlanta', 2016, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, demolidor, atlanta,tmep]

# for programas in filmes_e_series:
#     detalhes = programas.duracao if hasattr(programas, "duracao") else programas.temporadas
#     print(f"{programas.nome} - {programas.ano} - {detalhes} - {programas.likes}")

# for programa in filmes_e_series:
#     print(programa)


playlist_fim_de_semana = playlist('fim de semana', filmes_e_series)
print(f'Tamanho da playlis: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)