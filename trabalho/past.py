
nota = int(input('Digite su nota: '))
n = bool(input('você é participativo?'))
if nota >= 7:
    print('Você está aprovado')
if(nota== 6) and (n == True):
    print('Parabéns, você está de recuperação')
else :
    print('Você foi reprovado')


