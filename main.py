from CodeWriter import CodeWriter
from Parser import Parser


parser = Parser('MemoryAccess/BasicTest/BasicTest.vm')
code_writer = CodeWriter('MemoryAccess/BasicTest/BasicTest.asm')


for code in parser.file:
    if parser.hasMoreLines():
        command = parser.advance()
        print(command)
        if len(command) == 1:
            code_writer.writeArithmetic(command[0])

        print('----------------')




