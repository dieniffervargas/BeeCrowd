n = int(input())

horas = n/3600
resto = int(n%3600)
minutos = resto/60
segundos = int(n%60)

print("%d:%d:%d" % (horas,minutos,segundos))