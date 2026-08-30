from polinomio import Polinomio

def stringParaPolinomio(polinomioStr:str):
    if len(polinomioStr) < 2:
        return polinomioStr

    polinomioStr = polinomioStr.split(' ')
    polinomio = Polinomio()
    for i, numero in enumerate(polinomioStr):
        if i % 2 == 0:
            polinomio.inserirTermo(float(numero), int(polinomioStr[i+1]))
    return polinomio

def lerArquivo(caminho_arquivo:str = None):
    '''Procura por padrão um arquivo .txt em /data, caso não seja especificado um caminho. Retorna um dicionário contendo as instruções e os polinomios.'''
    if not caminho_arquivo:
        from glob import glob
        caminho_arquivo = (glob("data/*.txt"))[0]

    instrucoes = {}
    comandos = ('g', 't', '+', '-', '*', 'a', 'p')
    with open(caminho_arquivo) as arquivo:
        instrucao_prev = ''
        for index, line in enumerate(arquivo):
            if line.strip().lower() in comandos:
                instrucoes[f"instrucao{index}"] = {
                    'comando': line.strip().lower(), 
                    'polinomios': []
                    }
                instrucao_prev = f"instrucao{index}"
                continue
            instrucoes[instrucao_prev]['polinomios'].append(stringParaPolinomio(line.strip().lower().rstrip('\n')))
    return instrucoes

def executar():
    caminho_arquivo = input("Digite o caminho do arquivo .txt (Deixe em branco para o utilizar o padrão em /data):")

    instrucoes = lerArquivo(caminho_arquivo)
    print(instrucoes)
    resultados = []
    for instrucao in instrucoes:
        match instrucao.comando:
            case '+':
                pass

if __name__ == "__main__":
    executar()

