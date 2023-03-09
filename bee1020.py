idade = int(input())

print("%d ano(s)" % int(idade/365))
aux = (idade%365)
print("%d mes(es)" % int(aux/30))
aux = (aux%30)
print("%d dia(s)" % int(aux))