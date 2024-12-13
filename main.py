
def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.
    """
    pass


def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    """
    nRomano = input("")
    nRomano = nRomano.upper()
    nArabico = 0

    for i in range(len(nRomano)):
        if nRomano[i] == "I":
            nArabico += 1
        elif nRomano[i] == "V":
            nArabico += 5
            if i > 0 and nRomano[i - 1] == "I":
                nArabico -= 2
        elif nRomano[i] == "X":
            nArabico += 10
            if i > 0 and nRomano[i - 1] == "I":
                nArabico -= 2
        elif nRomano[i] == "L":
            nArabico += 50
            if i > 0 and nRomano[i - 1] == "X":
                nArabico -= 20
        elif nRomano[i] == "C":
            nArabico += 100
            if i > 0 and nRomano[i - 1] == "X":
                nArabico -= 20
        elif nRomano[i] == "D":
            nArabico += 500
            if i > 0 and nRomano[i - 1] == "C":
                nArabico -= 200
        elif nRomano[i] == "M":
            nArabico += 1000
            if i > 0 and nRomano[i - 1] == "C":
                nArabico -= 200
                
    print(nArabico)

pass

def q3():
    """
    Quantidade de divisores de um número (incluindo 1 e o próprio número)
    """
    num = int(input(""))
    divs = 0
    for i in range(1, num +1):
        if num % i == 0 and i % 3 == 0:
            div += 1
    if div == 0:
        print(False)
    else:
        print(True)

    pass

def q4():
    """
    Soma dos números positivos no intervalo definido
    """
    num1 = int(input(""))
    num2 = int(input(""))

    soma = 0

    if num1 < num2:
        for i in range(num1, num2 + 1):
            if i > 0:
                soma += i

    else:
        for i in range(num2, num1 + 1):
            if i > 0:
                soma += i

    print(soma)

    pass