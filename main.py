from CodeWriter import CodeWriter
from Parser import Parser


parser = Parser('StackArithmetic/StackTest/StackTest.vm')
code_writer = CodeWriter('StackArithmetic/StackTest/StackTest.asm')


for code in parser.file:
    print(parser.hasMoreLines())


print(parser.file)




