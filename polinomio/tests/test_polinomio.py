from polinomio import Polinomio 

polinomio = Polinomio()


polinomio.inserirTermo(4, 3)
polinomio.inserirTermo(-7, 5)
polinomio.inserirTermo(2, 1)

#teste sobrecarga str
print(polinomio)

#teste grau
print(polinomio.grau())

#teste tamnho
print(polinomio.tamanho())

#teste atribuição de valor X
print(polinomio.avaliacao(2))
