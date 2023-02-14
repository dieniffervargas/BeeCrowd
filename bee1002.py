PI = 3.14159

in_raio = input()

def calcula_area(raio):
    quadrado = raio * raio
    return PI * quadrado

area = calcula_area(float(in_raio))

texto = "A= %.4f" % (area)

print(texto)