#dados atribuidos pelo imput e reservado em listas correspondente ao espaço dado em cada sequência de número
linha1 = input().split(" ")
linha2 = input().split(" ")

#dados devidamente correspondidos ao decorrer da lista gerada nos imputs
cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2

#total recebe os valores atribuídos da lista 1 somado pela lista 2
total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

#aqui o resultado é apresentado
print(f'VALOR A PAGAR: R$ {total:.2f}')
