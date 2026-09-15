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
        if self.file.suffix == '.txt':
            with open(self.file, 'rb') as file:
                self.__bytes = file.read()
        else: raise FileNotFoundError("File extension must be '.bin'.")

    def readTxt(self):
        if self.file.suffix == '.txt':
            with open(self.file) as file:
                self.__string = file.read().strip()
            self.__string = self.__string.replace('\n', '').replace(' ', '')
        else: raise FileNotFoundError("File extension must be '.txt'.")

    def __addHeader(self):
        pass

    def compress(self):
        self.readTxt()

        binary_values = []
        binary_value = 0b00000000
        left_deloc = 6
        for gene in self.__string:
            binary_value |= (self.genes_values.get(gene.upper()) << left_deloc)
            if left_deloc == 0:
                left_deloc = 6
                binary_values.append(binary_value)
                # print(format(binary_value, '08b'))
                binary_value = 0b00000000
                continue
            left_deloc -= 2

        self.__bytes = bytes(binary_values)
        return self.__bytes
        

    def getData(self):
        print(self.__string)
        print()
        print(self.__binaries)