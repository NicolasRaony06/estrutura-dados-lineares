from polinomio import Polinomio

polinomio = Polinomio()

polinomio.inserirTermo(5, 6)
polinomio.inserirTermo(3, 4)
polinomio.inserirTermo(-2, 2)

polinomio2 = Polinomio()

polinomio2.inserirTermo(4, 6)
polinomio2.inserirTermo(-1, 3)
polinomio2.inserirTermo(5, 2)
polinomio2.inserirTermo(1, 0)

print(polinomio)
print(polinomio2)
print()

#teste subtração via sobrecarga de __sub__
polinomio3 = polinomio - polinomio2
print(polinomio3)
print()
