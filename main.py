class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme("vingadores - guerra infinita", 2019, 160)
vingadores.dar_likes()
vingadores.dar_likes()

print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes {vingadores.likes}")

atlanta = Serie("atlanta", 2017, 2)
atlanta.dar_likes()
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes {atlanta.likes}")