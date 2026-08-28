from polinomio import Polinomio

polinomio = Polinomio()

polinomio.inserirTermo(4, 3)
polinomio.inserirTermo(-7, 5)
polinomio.inserirTermo(2, 1)

polinomio2 = Polinomio()

polinomio2.inserirTermo(6, 3)
polinomio2.inserirTermo(-1, 0)
polinomio2.inserirTermo(8, 2)

#teste adição via sobrecarga de __add__
polinomio3 = polinomio + polinomio2
print(polinomio3)
print(polinomio)
print(polinomio2)
print()

# #teste sobrecarga str
# print(polinomio)

# #teste grau
# print(polinomio.grau())

# #teste tamnho
# print(polinomio.tamanho())

# #teste atribuição de valor X
# print(polinomio.definirX(2))
# print()

# #teste simplificação para coeficiente 0
# polinomio.inserirTermo(0, 6)
# print(polinomio, '\n')
# polinomio.simplificar()
# print(polinomio)
# print()

# #teste para termos de mesmo grau
# polinomio.inserirTermo(2, 5)
# polinomio.inserirTermo(6, 1)
# polinomio.inserirTermo(-1, 5)
# polinomio.inserirTermo(3.5, 1)
# print(polinomio, '\n')
# polinomio.simplificar()
# print(polinomio)



