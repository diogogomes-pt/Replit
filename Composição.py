


class Endereco():
  def __init__ (self, varCodPostal='', varRua='', varPorta = 0):
    self.codPostal = varCodPostal
    self.rua = varRua
    self.porta = varPorta

  def mostrarCodigoPostal (self):
    print (self.codPostal)

  def __str__(self):
    return self.rua


  
class Cliente():

  def __init__(self, varNome, varNumCliente,  varEndereco):
    self.Nome = varNome
    self.numCliente = varNumCliente
    self.endereco = varEndereco
  
end1 = Endereco("2830", "Barreiro", 25)  # instancia


#cliente1 = Cliente ("Ricardo", 12323213, end2 = Endereco("5300", "Bragança", 30))

cliente1 = Cliente ("Ricardo", 12323213, end1)

print (cliente1.endereco)



