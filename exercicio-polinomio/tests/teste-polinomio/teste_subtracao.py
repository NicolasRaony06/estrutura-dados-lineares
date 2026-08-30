from polinomio import Polinomio

polinomio = Polinomio()

polinomio.inserirTermo(4, 3)
polinomio.inserirTermo(-7, 5)
polinomio.inserirTermo(2, 1)

polinomio2 = Polinomio()

polinomio2.inserirTermo(6, 3)
polinomio2.inserirTermo(-1, 0)
polinomio2.inserirTermo(8, 2)

#teste subtração via sobrecarga de __sub__
polinomio3 = polinomio - polinomio2
print(polinomio3)
print()
print(polinomio)
print(polinomio2)
