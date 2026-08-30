from polinomio import Polinomio

def lerArquivo(arquivo:str = "entrada.txt"):
    instrucoes = {}
    comandos = ('g', 't', '+', '-', '*', 'a', 'p')
    with open(rf"data/{arquivo}") as arquivo:
        instrucao_prev = ''
        for index, line in enumerate(arquivo):
            if line.strip().lower() in comandos:
                instrucoes[f"instrucao{index}"] = {
                    'comando': line.strip().lower(), 
                    'polinomios': []
                    }
                instrucao_prev = f"instrucao{index}"
                continue
            instrucoes[instrucao_prev]['polinomios'].append(line.rstrip('\n'))

