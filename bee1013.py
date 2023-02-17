a = int(input())
b = int(input())
c = int(input())

maior_ab = int((a+b+abs(a-b)) / 2)

if maior_ab > c:
    print("%d eh o maior" % maior_ab)
else:
    print("%d eh o maior" % c)
