from compactador import Compactador

comp = Compactador('arquivos/example2.txt')

byte = comp.compress()

for i in byte:
    print(format(i, '08b'))



