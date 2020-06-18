def exercicio2(valor):
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
exercicio2(n)