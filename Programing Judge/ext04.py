nome = input()
salfixo = float(input())
qtdvendas = float(input())
bonus = float(qtdvendas * (15/100))
total = salfixo + bonus

print(f'TOTAL = R$ {total:.2f}')