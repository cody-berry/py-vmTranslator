
class CodeWriter:
    def __init__(self, file_name):
        self.file = open(file_name, 'w')
        self.counter = -1

    # write an arithmetic command like add or subtract
    def writeArithmetic(self, command):
        if command == 'add\n':
            self._writeAdd()
        if command == 'sub\n':
            self._writeSub()
        if command == 'neg\n':
            self._writeNeg()
        if command == 'not\n':
            self._writeNot()
        if command == 'and\n':
            self._writeAnd()
        if command == 'or\n':
            self._writeOr()
        if len(command) == 3 and command != 'or\n':
            operator = ' '
            if command == 'lt\n':
                operator = 0
            if command == 'eq\n':
                operator = 1
            if command == 'gt\n':
                operator = 2
            self._writeEqGtLt(operator)

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
            "D=M-D",
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

    # PROTECTED
    # write an and command
    def _writeAnd(self):
        c = [
            "// and",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=D&M",
            "M=D"
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write an or command
    def _writeOr(self):
        c = [
            "// or ",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=D|M",
            "M=D"
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write an equality command
    def _writeEqGtLt(self, operator):
        self.counter += 1

        jump_type = ""
        if operator == 0:  # lt
            jump_type = "LT"
        if operator == 1:  # eq
            jump_type = "EQ"
        if operator == 2:  # gt
            jump_type = "GT"

        c = [
            "// " + jump_type.lower(),
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=M-D",
            f"@TRUE{self.counter}",
            f"D;J{jump_type}",
            "@SP",
            "A=M-1",
            "M=0",
            f"@STOP{self.counter}",
            f"D;JMP",
            f"(TRUE{self.counter})",
            "@SP",
            "A=M-1",
            "M=-1",
            f"(STOP{self.counter})"
        ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write a push or pop command like push constant i
    def writePushPop(self, push_or_pop, segment, index):
        if push_or_pop == 'push':
            if segment == 'constant':
                self._writePushConstant(index)
            if segment == 'static':
                self._writePushStatic(index)
            if segment == 'pointer':
                self._writePushPointer(index)
            if segment == 'this':
                self._writePushThis(index)
            if segment == 'that':
                self._writePushThat(index)
        if push_or_pop == 'pop':
            if segment == 'static':
                self._writePopStatic(index)
            if segment == 'pointer':
                self._writePopPointer(index)
            if segment == 'this':
                self._writePopThis(index)
            if segment == 'that':
                self._writePopThat(index)

    # PROTECTED
    # write push constant i
    def _writePushConstant(self, i):
        c = [
            f"// push constant {i}",
            f"@{i}",
            "D=A",  # D=i
            "@SP",
            "M=M+1",  # SP++
            "A=M-1",  # A=originalSP
            "M=D"  # RAM[SP] = i
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push static i
    def _writePushStatic(self, i):
        c = [
            f"// push static {i}",
            f"@static.{i}",  # access static i
            "D=M",  # D = RAM[variable at i]
            "@SP",
            "M=M+1",  # SP++
            "A=M-1",  # A=originalSP
            "M=D"  # RAM[SP] = i
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop static i
    def _writePopStatic(self, i):
        c = [
            f"// pop static {i}",
            "@SP",
            "AM=M-1",  # SP--, A=SP
            "D=M",  # D=RAM[SP]
            f"@static.{i}",
            "M=D"  # RAM[variable at i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push pointer i
    def _writePushPointer(self, i):
        c = [
            f"// pop pointer {i}",
            f"@{3 + i}",  # access THIS/THAT
            "D=M",  # D=THIS/THAT
            "@SP",
            "M=M+1",
            "A=M-1",
            "D=M",  # RAM[SP] = THIS/THAT
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop pointer i
    def _writePopPointer(self, i):
        c = [
            f"// pop pointer {i}",
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            f"@{3 + i}",
            "M=D"  # THIS/THAT = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")
