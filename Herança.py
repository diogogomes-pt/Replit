class Carro: 
    
    cor = "Vermelho"
    modelo = "bmw"

### Object instantiation
carInstancia1 = Carro ()
print ("imprime fora da class cor ", carInstancia1.cor)
print ("imprime fora da class nova modelo ", carInstancia1.modelo)

carInstancia2 = Carro ()
print ("imprime carInstancia2 fora da class nova modelo ", carInstancia2.modelo)

carInstancia2.cor = "blue"

print ("imprime carInstancia2 fora da class cor ", carInstancia2.cor)