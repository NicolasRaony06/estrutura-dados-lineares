from polinomio import Polinomio

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
            instrucoes[instrucao_prev]['polinomios'].append(line.rstrip('\n'))
    return instrucoes

lerArquivo()