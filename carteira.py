valor = int(input())

n = [100,50,20,10,5,2,1]
hip = []
aux = valor

for i in range(7):
    if aux >= n[i]:
        hip.insert(i, aux // n[i])
        aux = aux % n[i]
    else:
        hip.insert(i,0)

print(valor)

for i in range(7):
    n[i] = f"{n[i]:.2f}"
    n[i] = n[i].replace('.',',')
    print(hip[i],"nota(s) de R$",n[i])
