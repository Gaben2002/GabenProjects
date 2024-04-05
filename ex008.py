m = float(input('Metros: '))

km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print(f'{m}m equivale a:'
      f'\n\033[32m{km}km\033[m'
      f'\n\033[31m{hm}hm\033[m'
      f'\n\033[33m{dam}dam\033[m'
      f'\n\033[34m{dm}dm\033[m'
      f'\n\033[35m{cm}cm\033[m'
      f'\n\033[36m{mm}mm\033[m')
