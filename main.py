from CodeWriter import *
from Parser import *


parser = Parser('StackArithmetic/StackTest/StackTest.vm')
code_writer = CodeWriter('StackArithmetic/StackTest/StackTest.asm')


while parser.hasMoreLines():
    if parser.lineNumber != -1:
        match parser.commandType():
            case Command.C_POP:
                code_writer.writePushPop('pop', parser.arg1(), parser.arg2())
            case Command.C_PUSH:
                code_writer.writePushPop('push', parser.arg1(), parser.arg2())
            case Command.C_ARITHMETIC:
                code_writer.writeArithmetic(parser.arg1())
            case _:
                print('not found')

    print("_______________________ₓ_________________ₓ__________ₓ____________ₑ____________")

    parser.advance()
    print(parser.lineContent)

    # if commandType == Command.C_POP or commandType == Command.C_PUSH:
    #     code_writer.writePushPop(parser.lineContent[0], parser.arg1(), parser.arg2())
    # if commandType == Command.C_ARITHMETIC:
    #     code_writer.writeArithmetic(parser.arg1())


match parser.commandType():
    case Command.C_POP:
        code_writer.writePushPop('pop', parser.arg1(), parser.arg2())
    case Command.C_PUSH:
        code_writer.writePushPop('push', parser.arg1(), parser.arg2())
    case Command.C_ARITHMETIC:
        code_writer.writeArithmetic(parser.arg1())
    case _:
        print('not found')
