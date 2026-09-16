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

    def _readBin(self):
        if self.file.suffix == '.bin':
            with open(self.file, 'rb') as file:
                self.__bytes = file.read()
            return self.__bytes
        else: raise FileNotFoundError("File extension must be '.bin'.")

    def _readTxt(self):
        if self.file.suffix == '.txt':
            with open(self.file) as file:
                self.__string = file.read().strip()
            self.__string = self.__string.replace('\n', '').replace(' ', '')
            return self.__string
        else: raise FileNotFoundError("File extension must be '.txt'.")

    def _writeBin(self):
        """Writes a file with the same name as the prev file plus '_compressed.bin'. Returns the file path."""
        file = self.file.with_name(self.file.stem + '_compressed.bin')
        with open(file, 'wb') as file:
            file.write(self.__bytes)
        return file

    def save(self):
        file_suffix = self.file.suffix
        if file_suffix == '.txt':
            return self._writeBin()
        elif file_suffix == '.bin':
            return self._writeTxt()
        raise FileNotFoundError("No file .bin or .txt to save was found.")

    def __createHeader(self, genes_counter: int):
        return genes_counter.to_bytes(4, 'big')

    def compress(self):
        """Converts the DNA string Genes to Bytes. Returns a bytes object."""
        self._readTxt()
        
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
        return self.__bytes

    def decompress(self):
        pass

        
        
    

    