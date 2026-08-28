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
print(polinomio.definirX(2))
print()

#teste simplificação para coeficiente 0
polinomio.inserirTermo(0, 6)
print(polinomio, '\n')
polinomio.simplificar()
print(polinomio)
print()

#teste para termos de mesmo grau
polinomio.inserirTermo(2, 5)
polinomio.inserirTermo(6, 1)
polinomio.inserirTermo(-1, 5)
polinomio.inserirTermo(3.5, 1)
print(polinomio, '\n')
polinomio.simplificar()
print(polinomio)

