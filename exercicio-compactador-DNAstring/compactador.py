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
        self.__binary = None

    def readBin(self):
        with open(self.file, 'rb') as file:
            self.__binary = file.read()

    def readTxt(self):
        with open(self.file) as file:
            self.__string = file.read().strip()
        self.__string = self.__string.replace('\n', '').replace(' ', '')

    def getData(self):
        print(self.__string)
        print()
        print(self.__binaries)