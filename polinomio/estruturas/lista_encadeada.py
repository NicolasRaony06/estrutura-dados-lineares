class No:
    def __init__(self, coeficiente:float, grau:int, next = None):
        self.coeficiente = coeficiente
        self.grau = grau
        self.next = next

    def __str__(self):
        return f"{self.coeficiente},{self.grau}"

class Lista:
    def __init__(self):
        self.header = None

    def inserir(self, coeficiente:float, grau:int):
        novo_no = No(coeficiente, grau)
        
        if not self.header:
            self.header = novo_no
            return

        no_atual = self.header
        while no_atual:
            if no_atual.grau >= novo_no.grau:
                if not no_atual.next:
                    no_atual.next = novo_no
                    return 
                
                if no_atual.next.grau <= novo_no.grau:
                    novo_no.next = no_atual.next
                    no_atual.next = novo_no
                    return
            else:
                novo_no.next = no_atual
                self.header = novo_no
                return
             
            no_atual = no_atual.next

    def __destrutor(self, no:No):
        del(no)

    def excluir(self, coeficiente:float, grau:int):
        no_atual = self.header
        if no_atual.coeficiente == coeficiente and no_atual.grau == grau:
            self.header = no_atual.next
            self.__destrutor(no_atual)
            return

        while no_atual.next:
            if no_atual.next.coeficiente == coeficiente and no_atual.next.grau == grau:
                no_atual.next = no_atual.next.next
                self.__destrutor(no_atual)
                return

            no_atual = no_atual.next

    def mostrarAll(self):
        nos = []
        no = self.header
        while no:
            nos.append(no)
            no = no.next
        return nos

    def obterProximo(self, no:No):
        return no.next

    def obterValor(self, no:No):
        return no.coeficiente, no.grau, no.next

    def alterarNo(self, no:No, coeficiente:float, grau:int):
        if coeficiente and grau:
            no.coeficiente = coeficiente
            no.grau = grau

    def tamanho(self):
        no = self.header
        contador = 0
        while no:
            contador += 1
            no = no.next

        return contador

    def existe(self, coeficiente:float, grau:int):
        no_atual = self.header
        while no_atual:
            if no_atual.coeficiente == coeficiente and no_atual.grau == grau:
                return no_atual

            no_atual = no_atual.next
        


    


    