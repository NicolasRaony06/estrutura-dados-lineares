from compactador import Compactador

comp = Compactador('arquivos/example2.txt')

byte = comp.compress()

print(list(byte))

for i in byte:
    print(format(i, '08b'))



