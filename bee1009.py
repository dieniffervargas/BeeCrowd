nome = input()
salario = float(input())
total_vendas = float(input())

total_a_receber = (total_vendas * 0.15) + salario

print("TOTAL = R$ %0.2f" % (total_a_receber))