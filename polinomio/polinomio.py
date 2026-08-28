from estruturas.lista_encadeada import Lista

class Polinomio:
    def __init__(self):
        self.termos = Lista()

    def inserirTermo(self, coeficiente:float, grau:int):
        '''Insere um termo dado um coeficiente real e um grau natural no polinômio.'''
        self.termos.inserir(coeficiente, grau)

    def excluirTermo(self, coeficiente:float, grau:int):
        '''Exclui o termo com o mesmo coeficiente e grau do polinômio.'''
        self.termos.excluir(coeficiente, grau)

    def grau(self):
        '''Retorna o grau do polinômio'''
        return self.termos.header.grau

    def tamanho(self):
        '''Retorna a quantidade de termos do polinômio.'''
        return self.termos.tamanho()

    def definirX(self, valor_de_x:float|int):
        '''Recebe um valor para a variável X e retorna o resultado do polinômio.'''
        resultado = 0
        termo = self.termos.header
        while termo:
            resultado += termo.coeficiente * (valor_de_x ** termo.grau)
            termo = termo.next
        return resultado

    def simplificar(self):
        '''Simplifica o polinômio em termos com coeficiente 0 e iguais.'''
        # termo = self.termos.header
        # while termo:
        #     if termo.coeficiente == 0:
        #         self.termos.excluir(termo.coeficiente, termo.grau)
        #         termo = termo.next
        #         continue
        #     termo = termo.next
        termos = self.termos.mostrarAll()
        termos_reduzida = termos[:]
        for termo1 in termos:
            if termo1.coeficiente == 0:
                self.termos.excluir(termo1.coeficiente, termo1.grau)
                continue
            termos_reduzida.remove(termo1)
            for termo2 in termos_reduzida:
                if termo1.grau == termo2.grau:
                    # print(termo1.grau, termo2.grau)
                    termo1.coeficiente += termo2.coeficiente
                    self.termos.excluir(termo2.coeficiente, termo2.grau)
        # print(self.termos.mostrarAll())

    def __merge(self, polinomio):
        import copy
        polinomio_merged = copy.deepcopy(self)
        polinomio_merged.termos.mostrarAll()[-1].next = copy.deepcopy(polinomio).termos.header

        return polinomio_merged

    def __add__(self, polinomio):
        polinomio_merged = self.__merge(polinomio)
        polinomio_merged.simplificar()
        return polinomio_merged

    def __str__(self):
        polinomio = ""
        termos = self.termos.mostrarAll()
        for termo in termos:
            if termo.coeficiente > 0:
                polinomio += f"+ {termo.coeficiente}x^{termo.grau} "
                continue

            polinomio += f"- {(termo.coeficiente)*-1}x^{termo.grau} "

        return polinomio

    