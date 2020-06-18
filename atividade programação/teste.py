#exercicio 1
def exercicio_1(n):
    for i in range(n):
        i += 1
        print(str(i) * i)

n = int(input('Digite um número: '))
exercicio_1(n)
#--------------------------------------------------
#exercicio 2
def exercicio_2(valor):
    x = 1
    while x <= valor:
        y = 1
        piramide = ''
        while y <= x:
            piramide += str(y) + ', '
            y += 1
        print (piramide)
        x += 1

n = int(input('Digite um número: '))
exercicio_2(n)


#--------------------------------------------------
#exercicio 3 
def exercicio_3 ():

    a = int(input('digite um valor '))
    b = int(input('digite um valor '))
    c = int(input('digite um valor '))

    print('a soma dos valores a, b, c,  é ')

    soma = a + b + c 

    print(f'a soma de {a} com {b} com {c} fica  {soma}')
exercicio_3()

#--------------------------------------------------
#exercicio 4 
def exercicio_4():
    print('O valor é positivo ou negativo? ')
    valor = int(input('digte o valor desejado: '))
    if valor == 0:
        print('este valor é nulo')
    elif valor <= 0:
        print('este valor é Negativo')
    else:
        print('este valor é positivo')

exercicio_4()
#--------------------------------------------------
#exercicio 5 
def exercicio_5():
    imp = float(input('digite a taxa de imposto: '))
    custo = float(input('digite o custo: '))
    função = (1 + imp/100)*custo
    print(f'o valor  com imposto é {função} ')

exercicio_5()
#--------------------------------------------------