"""
class Carro():
  pass

####################
#classe estudante

class Estudante:
  pass

obj = Estudante()
obj2 = Estudante()
"""
####################
# class carro com um attribute 
class Mota:
  cor = "vermelho"
""""""  
nomevar = Mota()

####################
# class carro com um attributo aceder a valores da classe 
class Carro:
  cor = "vermelho"
  
""""""  

objectoCarro = Carro()
obj2 = Carro()


objectoCarro.cor = "azul"
obj2.cor = "branco"

nomevar.cor = "cinza"
####################
# imprimir valores
#print (" imprimir cor da mota ", nomevar.cor)
#print (" imprimir cor do carro  ", objectoCarro.cor)


####################
# class carro com mais que um attributo
class Carro:
  cor = ""
  km = 0
 

carro1 = Carro ()
carro2 = Carro ()

print (" imprimir cor do carro1 ", carro1.cor)
print (" imprimir km do carro1  ", carro1.km)

carro1.cor = "amarelo"
carro1.km = 10

print (" imprimir cor do carro1 ", carro1.cor)
print (" imprimir km do carro1  ", carro1.km)


####################
# class carro mas aumentar km
class Carro:
  cor = ""
  km = 0 

  def aumentarkmPara10(self):
    self.km = 10        

  def aumentarkm (self, kml):
    self.km = self.km + kml
  
carro3 = Carro()

carro3.aumentarkmPara10()

carro3.aumentarkm(33)
carro3.aumentarkm(10)

#carro3.km = carro3.km + 10 
#carro3.km = 10 