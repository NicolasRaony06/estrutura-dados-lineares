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

    