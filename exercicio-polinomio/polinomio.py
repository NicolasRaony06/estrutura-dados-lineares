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
        termos = self.termos.mostrarAll()
        for termo1 in termos:
            termo2 = termo1.next
            while termo2:
                if termo1.grau == termo2.grau:
                    termo1.coeficiente += termo2.coeficiente
                    self.termos.excluir(termo2.coeficiente, termo2.grau)
                    termos.remove(termo2)
                termo2 = termo2.next
            if termo1.coeficiente == 0:
                self.termos.excluir(termo1.coeficiente, termo1.grau)
                termos.remove(termo1)
            
    def __merge(self, polinomio):
        import copy
        polinomio_merged = Polinomio()

        nos = copy.deepcopy(self.termos.mostrarAll() + polinomio.termos.mostrarAll())
        for no in nos:
            polinomio_merged.inserirTermo(no.coeficiente, no.grau)

        return polinomio_merged

    def __add__(self, polinomio):
        polinomio_merged = self.__merge(polinomio)
        polinomio_merged.simplificar()
        return polinomio_merged

    def __sub__(self, polinomio):
        import copy
        polinomio = copy.deepcopy(polinomio)

        termos = polinomio.termos.mostrarAll()
        for termo in termos:
            termo.coeficiente *= -1

        polinomio_merged = self.__merge(polinomio)
        polinomio_merged.simplificar()
        return polinomio_merged
          
    def __mul__(self, polinomio):
        polinomio_multiplicado = Polinomio()
        for termo1 in self.termos.mostrarAll():
            for termo2 in polinomio.termos.mostrarAll():
                coeficiente = termo1.coeficiente * termo2.coeficiente
                grau = termo1.grau + termo2.grau
                polinomio_multiplicado.inserirTermo(coeficiente, grau)
        polinomio_multiplicado.simplificar()
        return polinomio_multiplicado

    def __str__(self):
        polinomio = ""
        self.simplificar()
        termos = self.termos.mostrarAll()
        if not termos:
            return "0"

        for termo in termos:
            if termo.coeficiente > 0:
                polinomio += f"+ {termo.coeficiente if termo.coeficiente != 1 else ''}{f"x{f"^{termo.grau}" if termo.grau != 1 else ''}" if termo.grau else ''} "
                continue

            polinomio += f"- {((termo.coeficiente)*-1) if (termo.coeficiente * -1) != 1 else ''}{f"x{f"^{termo.grau}" if termo.grau != 1 else ''}" if termo.grau else ''} "
        return polinomio

    