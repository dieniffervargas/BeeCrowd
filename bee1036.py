# val = input()
# a,b,c = val.split(" ")
# a = float(a)
# b = float(b)
# c = float(c)

a, b, c = map(float, input().split())

delta = ((b**2)-4*a*c)

if a == 0 or delta < 0:
    print("Impossivel calcular")
elif (delta == 0):
    x1 = (-b + delta**(1/2)) / (2 * a)
    x2 = x1
    print("R1 = %0.5f" % (x1))
    print("R2 = %0.5f" % (x2))
else:
   x1 = (-b + delta**(1/2)) / (2 * a)
   x2 = (-b - delta**(1/2)) / (2 * a)
   print("R1 = %0.5f" % (x1))
   print("R2 = %0.5f" % (x2))