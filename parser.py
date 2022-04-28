
class Parser:
    def __init__(self, fileName):
        file = open(fileName, 'r')
        self.file = []

        print(file)

        for line in file:
            c = line
            print(c)

            if (len(c) > 2 and c[0] != ' ' and c[0] != '/'):
                self.file.append(c)



        self.lineNumber = -1
        self.lineContent = ' '


    def hasMoreLines(self):
        self.lineNumber += 1
        print(self.lineNumber)
        self.lineContent = self.file[self.lineNumber]
        print(self.lineContent)
        return self.lineNumber < len(self.file)


