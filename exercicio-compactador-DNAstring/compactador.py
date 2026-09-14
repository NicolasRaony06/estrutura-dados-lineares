class Compactador:
    genes_values = {
        'A': '00',
        'C': '01',
        'G': '10',
        'T': '11'
    }

    def __init__(self, file):
        from pathlib import Path
        self.file = Path(file)
        self.__string = ''
        self.__binaries = ''

    def readFile(self):
        if self.file.suffix == '.txt':
            with open(self.file) as file:
                self.__string = file.read()
        elif self.file.suffix == '.bin':
            with open(self.file, 'rb') as file:
                self.__binaries = file.read()
                print(type(file.read()))

    def getData(self):
        print(self.__string)
        print()
        print(self.__binaries)