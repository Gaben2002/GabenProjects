n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if n1 > n2:
    print('O \033[34;1mPRIMEIRO\033[m é maior')
elif n2 > n1:
    print('O \033[31;1mSEGUNDO\033[m é maior')
elif n1 == n2:
    print('Os dois valores são \033[36;1mIGUAIS\033[m')
