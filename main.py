class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)



vingadores = Filme("vingadores - guerra infinita", 2019, 160)
tmep = Filme("todo mundo em pânico", 1999, 100)
tmep.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta = Serie("atlanta", 2017, 2)
demolidor = Serie("demolidor", 2016, 3)
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, tmep, demolidor]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"Tamanhao da playlist: {len(playlist_fim_de_semana)}")

for Programa in playlist_fim_de_semana:
    print(Programa)