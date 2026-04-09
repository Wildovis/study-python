saldo=2000.00
saque=float(input('digite o valor do saque'))
if saque <=0:
    print('valor invalido')
elif saque>saldo:
    print('valor insulficente')
else:
    saldo-=saque#saldo=saldo-saque
    print (f'saldo ={saldo}')


print(f'saldo=){saldo}')



