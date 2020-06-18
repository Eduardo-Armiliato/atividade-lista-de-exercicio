def exercicio5():
    imp = float(input('digite a taxa de imposto: '))
    custo = float(input('digite o custo: '))
    função = (1 + imp/100)*custo
    print(f'o valor  com imposto é {função} ')

exercicio5()