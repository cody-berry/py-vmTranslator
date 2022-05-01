
import enum


class Command(enum.Enum):
    C_ARITHMETIC = 1
    C_PUSH = 2
    C_POP = 3
    C_LABEL = 4
    C_GOTO = 5
    C_IF = 6
    C_FUNCTION = 7
    C_RETURN = 8
    C_CALL = 9





class Parser:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        self.file = []

        for line in file:
            c = line

            if (len(c) > 2 and c[0] != ' ' and c[0] != '/'):
                self.file.append(c)



        self.lineNumber = -1
        self.lineContent = ' '

    def hasMoreLines(self):
        return self.lineNumber < len(self.file)

    def advance(self):
        self.lineNumber += 1
        print(self.lineNumber)
        self.lineContent = self.file[self.lineNumber]
        print(self.lineContent)

        command = self.lineContent.strip().split(' ')

        return command

