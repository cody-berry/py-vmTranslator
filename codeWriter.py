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


class CodeWriter:
    def __init__(self, file_name):
        self.file = open(file_name, 'w')

    # write an arithmetic command like add or subtract
    def writeArithmetic(self, command):
        if command == 'add':
            self._writeAdd()
        if command == 'sub':
            self._writeSub()
        if command == 'neg':
            self._writeNeg()
        if command == 'not':
            self._writeNot()

    # PROTECTED
    # write an add command
    def _writeAdd(self):
        c = [
            "// add",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=D+M",
            "M=D"
            ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write a subtract command
    def _writeSub(self):
        c = [
            "// sub ",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=D-M",
            "M=D"
            ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write a neg command
    def _writeNeg(self):
        c = [
            "// neg ",
            "@SP",
            "A=M-1",
            "M=-M"
        ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write a 'not' command
    def _writeNot(self):
        c = [
            "// not ",
            "@SP",
            "A=M-1",
            "M=!M"
        ]

        for line in c:
            print(line)
            self.file.write(line + "\n")
