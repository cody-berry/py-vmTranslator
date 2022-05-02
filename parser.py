
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
        return self.lineNumber < len(self.file) - 1

    def advance(self):
        self.lineNumber += 1
        print(self.lineNumber)
        self.lineContent = self.file[self.lineNumber]
        print(self.lineContent)

    def commandType(self) -> Command:
        command = self.lineContent.split(' ')

        print(command)

        if command[0] in ['add\n', 'sub\n', 'neg\n', 'or\n', 'and\n', 'not\n', 'lt\n', 'eq\n', 'gt\n']:
            return Command.C_ARITHMETIC
        if command[0] == 'push':
            return Command.C_PUSH
        if command[0] == 'pop':
            return Command.C_POP
        if command[0] == 'label':
            return Command.C_LABEL
        if command[0] == 'goto':
            return Command.C_GOTO
        if command[0] == 'if':
            return Command.C_IF
        if command[0] == 'function':
            return Command.C_FUNCTION
        if command[0] == 'return\n':
            return Command.C_RETURN
        if command[0] == 'call':
            return Command.C_CALL

    def arg1(self) -> str:
        command = self.lineContent.split(' ')
        if len(command) == 1:
            return self.lineContent
        else:
            return command[1]

    def arg2(self) -> int:
        command = self.lineContent.split()
        return int(command[2])



