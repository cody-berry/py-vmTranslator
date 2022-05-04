
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
            if segment == 'local':
                self._writePushLocal(index)
            if segment == 'argument':
                self._writePushArgument(index)
            if segment == 'temp':
                self._writePushTemp(index)
        if push_or_pop == 'pop':
            if segment == 'static':
                self._writePopStatic(index)
            if segment == 'pointer':
                self._writePopPointer(index)
            if segment == 'this':
                self._writePopThis(index)
            if segment == 'that':
                self._writePopThat(index)
            if segment == 'local':
                self._writePopLocal(index)
            if segment == 'argument':
                self._writePopArgument(index)
            if segment == 'temp':
                self._writePopTemp(index)


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
            f"// push pointer {i}",
            f"@{3 + i}",  # access THIS/THAT
            "D=M",  # D=THIS/THAT
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = THIS/THAT
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

    # PROTECTED
    # write push pointer i
    def _writePushTemp(self, i):
        c = [
            f"// push temp {i}",
            f"@{5 + i}",  # access RAM[5-12]
            "D=M",  # D=RAM[5-12]
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = RAM[5-12]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop pointer i
    def _writePopTemp(self, i):
        c = [
            f"// pop temp {i}",
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            f"@{5 + i}",
            "M=D"  # RAM[5-12] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push this i
    def _writePushThis(self, i):
        c = [
            f"// push this {i}",
            f"@{i}",
            "D=A",  # D=i
            f"@THIS",  # access THIS
            "A=D+M",
            "D=M",  # D=*THIS
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = THIS
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop this i
    def _writePopThis(self, i):
        c = [
            f"// pop this {i}",
            f"@{i}",
            "D=A",  # D=i
            "@THIS",
            "D=D+M",  # D = RAM[THIS] + i
            "@ad",
            "M=D",  # address = RAM[THIS] + i
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            "@ad",
            "A=M",  # A = RAM[THIS] + i
            "M=D",  # RAM[RAM[THIS] + i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push that i
    def _writePushThat(self, i):
        c = [
            f"// push that {i}",
            f"@{i}",
            "D=A",  # D=i
            f"@THAT",  # access THAT
            "A=D+M",
            "D=M",  # D=*THAT
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = THAT
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop that i
    def _writePopThat(self, i):
        c = [
            f"// pop that {i}",
            f"@{i}",
            "D=A",  # D=i
            "@THAT",
            "D=D+M",  # D = RAM[THAT] + i
            "@ad",
            "M=D",  # address = RAM[THAT] + i
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            "@ad",
            "A=M",  # A = RAM[THAT] + i
            "M=D",  # RAM[RAM[THAT] + i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push local i
    def _writePushLocal(self, i):
        c = [
            f"// push local {i}",
            f"@{i}",
            "D=A",  # D=i
            f"@LCL",  # access LCL
            "A=D+M",
            "D=M",  # D=*LCL
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = LCL
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop local i
    def _writePopLocal(self, i):
        c = [
            f"// pop local {i}",
            f"@{i}",
            "D=A",  # D=i
            "@LCL",
            "D=D+M",  # D = RAM[LCL] + i
            "@ad",
            "M=D",  # address = RAM[LCL] + i
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            "@ad",
            "A=M",  # A = RAM[LCL] + i
            "M=D",  # RAM[RAM[LCL] + i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push argument i
    def _writePushArgument(self, i):
        c = [
            f"// push argument {i}",
            f"@{i}",
            "D=A",  # D=i
            f"@ARG",  # access ARG
            "A=D+M",
            "D=M",  # D=*ARG
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = ARG
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop argument i
    def _writePopArgument(self, i):
        c = [
            f"// pop argument {i}",
            f"@{i}",
            "D=A",  # D=i
            "@ARG",
            "D=D+M",  # D = RAM[ARG] + i
            "@ad",
            "M=D",  # address = RAM[ARG] + i
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            "@ad",
            "A=M",  # A = RAM[ARG] + i
            "M=D",  # RAM[RAM[ARG] + i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")
