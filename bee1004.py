# -*- coding: utf-8 -*-

def produto(a,b):
    return a*b

entrada_a = input()
entrada_b = input()

prod = produto(int(entrada_b),int(entrada_a))

texto = "PROD = %d" % (prod)

print(texto)