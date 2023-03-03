entrada_a = input().split(" ")
entrada_b = input().split(" ")

cod_a,qnt_a,val_a = entrada_a
cod_b,qnt_b,val_b = entrada_b

print(cod_a)
total = (int(qnt_a) * float(val_a)) + (int(qnt_b) * float(val_b))
texto = "VALOR A PAGAR: R$ %0.2f" % (total)

print(texto)