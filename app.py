n = int(input('Entrer un nombre:'))

if n / 2 == n // 2:
    print('Le nombre est divisible par 2.')
elif n / 3 == n // 3 and n / 5 == n // 5:
    print('Le nombre est divisible par 3 et par 5')
elif n / 3 == n // 3:
    print('Le nombre est divisible par 3')
elif n / 5 == n // 5:
    print('Le nombre est divisible par 5')
else:
    print("Le nombre n'est ni divisible par 2 ni par 3 ni par 5.")
