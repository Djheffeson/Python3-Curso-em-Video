print('-'*23)
print('Sequência de fibonacci')
print('-'*23)
termos = int(input('Quantos termos você quer mostrar? '))
x = 3
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1, t2), end='')
while x <= termos:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    x += 1
print('→ FIM')
print('~'*30)
