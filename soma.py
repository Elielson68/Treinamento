# Esse arquivo vai executar uma soma
def checar_valor(entrada):
    correcao = entrada
    teste = entrada.isdigit()
    if not teste:
        while type(entrada) is not int:
            correcao = input('Corrige aí: ')
            if correcao.isdigit():
                return int(correcao)

    return int(correcao)


while True:
    a = input("Digita um valor: ")
    a = checar_valor(a)

    b = input("Digita outro valor: ")
    b = checar_valor(b)

    print("Resultado da soma é: ", a+b)
#sadasdsada