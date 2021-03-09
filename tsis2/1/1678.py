def interpret(command):
    return command.replace('()','o').replace('(al)','al')
a=str(input())
print(interpret(a))
#G()(al)
#Goal