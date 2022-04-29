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

    def writeArithmetic(self, command):
        if command == 'add':
            self._writeAdd()
        if command == 'sub':
            self._writeSub()

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

