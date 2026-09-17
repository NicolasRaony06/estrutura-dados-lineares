from compactador import Compactador

# comp = Compactador('arquivos/example2.txt')
# comp.compress()
# comp.save()

comp = Compactador('arquivos/example2_compressed.bin')
print(comp.decompress())


