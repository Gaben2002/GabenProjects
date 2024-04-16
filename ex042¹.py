s1 = float(input('Segmento 1: '))
s2 = float(input('Segmento 2: '))
s3 = float(input('Segmento 3: '))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print('Pode fazer triangulo')
    if s1 == s2 == s3:
        print('\033[1;34mEQUILATERO.\033[m')
    elif s1 != s2 != s3 != s1:
        print('\033[1;35mESCALENO.\033[m')
    else:
        print('\033[1;36mISÓSCELES.\033[m')
else:
    print('Não pode fazer triangulo')
