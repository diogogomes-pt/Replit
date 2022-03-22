
#carro
#mota


class Veiculo:

  marca = ""
  cor = ""
  
  def __init__ (self, varMarca):
    self.marca = varMarca

  def apitar (self):
    print ( " apitou ")

   
class Carro ( Veiculo  ):
  pass

   
class Mota ( Veiculo  ):
  pass

carObj = Carro ( "BMW")
carObj.apitar ( )

motaObj = Mota (" motaXPTO ")
motaObj.apitar()