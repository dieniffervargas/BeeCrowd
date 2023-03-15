cod, qnt = map(int, input().split())

total = 0

match cod:
    case 1:
        val = 4.00
    case 2:
        val = 4.50
    case 3:
        val = 5.00
    case 4:
        val = 2.00
    case 5:
        val = 1.50

print("Total: R$ %0.2f" % (val*qnt))