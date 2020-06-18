def exercicio4():
    print('O valor é positivo ou negativo? ')
    valor = int(input('digte o valor desejado: '))
    if valor == 0:
        print('este valor é nulo')
    elif valor <= 0:
        print('este valor é Negativo')
    else:
        print('este valor é positivo')

exercicio4()