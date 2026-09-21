A = 0
C = 1
G = 2
T = 3

#ACGT
valor = None
valor = A << 6
valor = valor | (C << 4)
valor = valor | (G << 2)
valor = valor | T

byte = bytes([valor])

# print(format(valor, '08b'))
# print(list(byte))
# print(bin(valor))


gene = 'TGCA'
genes_values = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }

# value = 0b00000000
# left_deloc = 6
# for char in gene:
#     value |= (genes_values.get(char) << left_deloc)
#     left_deloc -= 2

# # print(left_deloc)
# # print(format(value, '08b'))

# value = 0b0000000000

# value |= 4028

# b = bytes([value])

# print(format(value, '08b'))

lista = [1,2,3,4,5]
print(lista[1:])