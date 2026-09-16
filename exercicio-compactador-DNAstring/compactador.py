class Compactador:
    genes_values = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }

    def __init__(self, file):
        from pathlib import Path
        self.file = Path(file)
        self.__string = None
        self.__bytes = None

    def readBin(self):
        print(self.file)
        if self.file.suffix == '.bin':
            with open(self.file, 'rb') as file:
                self.__bytes = file.read()
            return self.__bytes
        else: raise FileNotFoundError("File extension must be '.bin'.")

    def readTxt(self):
        if self.file.suffix == '.txt':
            with open(self.file) as file:
                self.__string = file.read().strip()
            self.__string = self.__string.replace('\n', '').replace(' ', '')
            return self.__string
        else: raise FileNotFoundError("File extension must be '.txt'.")

    def writeBin(self):
        file = self.file.with_name(self.file.stem + '_compressed.bin')
        with open(file, 'wb') as file:
            file.write(self.__bytes)

    def __createHeader(self, genes_counter: int):
        return genes_counter.to_bytes(4, 'big')

    def compress(self):
        self.readTxt()
        
        binary_values = []
        binary_value = 0b00000000
        left_deloc = 6
        genes_counter = 0
        for gene in self.__string:
            gene_values = self.genes_values.get(gene.upper())
            if gene_values is not None:
                genes_counter += 1
                binary_value |= (gene_values << left_deloc)
                if left_deloc == 0:
                    left_deloc = 6
                    binary_values.append(binary_value)
                    binary_value = 0b00000000
                    continue
                left_deloc -= 2

        if not left_deloc == 6:
            binary_values.append(binary_value)
        
        self.__bytes = self.__createHeader(genes_counter) + bytes(binary_values)
        self.writeBin()
        return True
        
    

    