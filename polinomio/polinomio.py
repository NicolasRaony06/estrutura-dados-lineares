from estruturas.lista_encadeada import Lista

class Polinomio:
    def __init__(self):
        self.termos = Lista()

    def inserirTermo(self, coeficiente:float, grau:int):
        self.termos.inserir(coeficiente, grau)

    def excluirTermo(self, coeficiente:float, grau:int):
        self.termos.excluir(coeficiente, grau)

    def grau(self):
        return self.termos.header.grau

    def tamanho(self):
        return self.termos.tamanho()

    def avaliacao(self, valor_de_x:float|int):
        '''Recebe um valor para a variável X e retorna o resultado do polinômio.'''
        resultado = 0
        termo = self.termos.header
        while termo:
            resultado += termo.coeficiente * (valor_de_x ** termo.grau)
            termo = termo.next
        return resultado

    def __str__(self):
        polinomio = ""
        termos = self.termos.mostrarAll()
        for termo in termos:
            if termo.coeficiente > 0:
                polinomio += f"+ {termo.coeficiente}x^{termo.grau} "
                continue

            polinomio += f"- {(termo.coeficiente)*-1}x^{termo.grau} "

        return polinomio

    