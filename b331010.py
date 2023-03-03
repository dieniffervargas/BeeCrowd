entrada_a = input().split(" ")
entrada_b = input().split(" ")

cod_a,qnt_a,val_a = entrada_a
cod_b,qnt_b,val_b = entrada_b

total = (int(qnt_a) * float(val_a)) + (int(qnt_b) * float(val_b))
texto = "VALOR A PAGAR: R$ %0.2f" % (total)

print(texto)


//sdkajsdkjashdakjhdkajs

x = input().split(" ")
y= input().split(" ")
a,b,c = x
d,e,f= y
total = (int(b) * float(c)) + (int(e) * float(f))
print("VALOR A PAGAR: R$ %0.2f" %total)