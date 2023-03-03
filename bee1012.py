# -*- coding: utf-8 -*-

entrada = input().split(" ")

a,b,c = entrada
a = float(a)
b = float(b)
c = float(c)

print("TRIANGULO: %0.3f" % (a * (c/2)))
print("CIRCULO: %0.3F" % ((c * c) * 3.14159))
print("TRAPEZIO: %0.3f" % ((( a + b ) * c ) / 2))
print("QUADRADO: %0.3f" % (b * b))
print("RETANGULO: %0.3f" % (a * b))