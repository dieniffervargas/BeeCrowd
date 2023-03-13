import cmath
val = input()

a,b,c = val.split(" ")
a = float(a)
b = float(b)
c = float(c)

if a < 0:
    print("Impossivel calcular")
else:
    delta = (b*b)-(4*a*c)
    raiz = sqrt(delta)
    # x1 = -b + sqrt((b*b)-(4*a*c)) / (2 * a)
    # x2 = -b - sqrt((b*b)-(4*a*c)) / (2 * a)


    # print("R1 = %0.5f" % x1)
    # print("R2 = %0.5f" % x2)