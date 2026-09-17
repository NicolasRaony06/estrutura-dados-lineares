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
        self.__string = ''
        self.__bytes = None

    def _readBin(self):
        """Reads a file .bin. Returns a bytes object."""
        if self.file.suffix == '.bin':
            with open(self.file, 'rb') as file:
                self.__bytes = file.read()
            return self.__bytes
        else: raise FileNotFoundError("File extension must be '.bin'.")

    def _readTxt(self):
        """Reads a file .txt. Returns a formated string."""
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

    def _writeTxt(self):
        """Writes a file with the same name as the prev file plus '_decompressed.txt'. Returns the file path."""
        file = self.file.with_name(self.file.stem + '_decompressed.txt')
        with open(file, 'w') as file:
            file.write(self.__string)
        return file

    def save(self):
        """Saves the compress/decompress content. Controls whether the file will be a .txt or .bin."""
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

    def __getHeader(self, detach=True):
        header = self.__bytes[:4]
        if detach:
           self.__bytes = self.__bytes[4:]
        return header

    def __genesValuesInverter(self):
        inverted_dict = {}
        for key, value in self.genes_values.items():
            inverted_dict[value] = key
        return inverted_dict

    def decompress(self):
        """Converts DNA bytes back to string. Returns a string containing the DNA sequence."""       
        self._readBin()
        max_genes = int.from_bytes(self.__getHeader(), 'big')
        genes_values_inverted = self.__genesValuesInverter()

        mask = 0b11
        genes = []
        left_shifts = [6,4,2,0]
        for byte in self.__bytes:
            for shift in left_shifts:
                genes.append(genes_values_inverted[(byte >> shift) & mask])
                if len(genes) >= max_genes: 
                    break
            
        self.__string = ''.join(genes)
        return self.__string

        
        
    

    