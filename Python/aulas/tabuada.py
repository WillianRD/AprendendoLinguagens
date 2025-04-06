inicio = int(input('Digite um número:\n'))

print('--- TABUADA ---')
for i in range(1,11):
    resultado = inicio * i
    print(f"{inicio} x {i} = {resultado}")