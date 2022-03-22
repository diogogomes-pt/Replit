class Filme:

  def __init__(self, nome, duracao, ano, artistaPrincipal):
    self.__nome = nome
    self.__duracao = duracao
    self.__ano = ano
    self.__artistaPrincipal = artistaPrincipal
  
  def printFilme (self):
    print("  Filme é ", self.__nome )

  def __MudaNome (self, novo):    
    self.__nome = "StarWars II"


varfilme = Filme ("asd", 2, 2,"asd")