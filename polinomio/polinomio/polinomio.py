from estruturas.lista_encadeada import Lista

class Polinomio:
    def __init__(self):
        self.termos = Lista()

    def inserirTermo(self, coeficiente:float, grau:int):
        self.termos.inserir(coeficiente, grau)

    def excluirTermo(self, coeficiente:float, grau:int):
        self.termos.excluir(coeficiente, grau)

    def __str__(self):
        #polinomio = ""
        termos = self.termos.mostrarAll()
        for termo in termos:
            if termo.coeficiente > 0:
                polinomio += f"+ {termo.coeficiente}x^{termo.grau} "
                continue

            polinomio += f"- {(termo.coeficiente)*-1}x^{termo.grau} "

        return polinomio

    