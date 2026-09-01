from polinomio import Polinomio

polinomio = Polinomio()

polinomio.inserirTermo(1, 3)
polinomio.inserirTermo(0, 2)
polinomio.inserirTermo(-1, 3)
polinomio.inserirTermo(5, 0)
polinomio.inserirTermo(-1, 3)
polinomio.inserirTermo(2, 1)

print(polinomio)

# polinomio2 = Polinomio()

# polinomio2.inserirTermo(-1, 3)
# polinomio2.inserirTermo(2, 1)

# print(polinomio)
# print(polinomio2)
# print()

# #teste adição via sobrecarga de __add__
# polinomio3 = polinomio + polinomio2
# print(polinomio3)
# print()