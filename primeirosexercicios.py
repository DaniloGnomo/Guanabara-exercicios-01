# EXERCICIOS DAS PRIMEIRAS AULAS DE PYTHON DO CURSO DO GUANABARA

# ordem procedencia
# 1 ()
# 2 ** pow raiz quadrada
# 3 * / //divisao inteira %resto divisao
# 4 + -

# *******************************#

#numero ant e susc
num = int(input('Digite um numero inteiro:'))

print('Seu numero é {}, o antecessor a ele é {} e sucessor é {}'.format(num, num-1, num+1))


#dobro triplo raiz
ndt = int(input('Digite um numero: '))
print('Voce digitou: {}\n o dobro deste numero é: {}\n o triplo é: {}\n sua raiz quadrada é: {:.2f}'
      .format(ndt, ndt*2, ndt*3, ndt**(1/2)))


#Media de nota
nota = float(input('Digita a primeira nota do Aluno: '))
nota2 = float(input('Digite a Segunda nota do Aluno: '))

print('A media das notas {} e {} do aluno é: {:.2f}'.format(nota, nota2, (nota+nota2)/2))


#converter
med = float(input('Digite o valor em metros  a ser covertido: '))
print('{} metros são: {} centimetros ou {} milimetros'.format(med, med*100, med*1000))


#tabuada
tab = int(input('Digite qual a tabuada desejada: '))
print(tab, ' x 1 = ', tab*1, ' \n',
      tab,  ' x  2 = ', tab*2, ' \n',
      tab,  ' x  3 = ', tab*3, ' \n',
      tab,  ' x  4 = ', tab*4, ' \n',
      tab,  ' x  5 = ', tab*5, ' \n',
      tab,  ' x  6 = ', tab*6, ' \n',
      tab,  ' x  7 = ', tab*7, ' \n',
      tab,  ' x  8 = ', tab*8, ' \n',
      tab,  ' x  9 = ', tab*9, ' \n',
      tab,  ' x 10 = ', tab*10)

#dolar real
va = float(input('Quantos reais voce quer coverter em dolares: '))
print('Com seus R$ {:.2f} voce consegue comprar: {:.2f} dolares'.format(va, va/3.27))

#tinta
alt = float(input('Digite a altura da area a ser pintada: '))
lar = float(input('Digite a largura da area a ser pintada: '))
print('A area total de {:.2f} por {:.2f} a ser pintada é {:.2f} metros quadrados \n'
      'voce ira usar um total de {:.2f} litros de tinta para pintar'.format(alt, lar, alt*lar, alt*lar/2))


#desconto
pr = float(input('Qual o valor antes do desconto do produto: R$ '))
ds = int(input('Quantos porcetos de descontos voce recebeu: '))
print('O valor anterior do produto era: R$ {:.2f}\n Com o desconto de {}%\n'
      ' Voce ira pagar o total de: R$ {:.2f}\n Tendo um desconto de: R${}'.format(pr, ds, pr-(pr*ds/100), pr*ds/100))



#Salario
sal = int(input('Qual o salario: '))
aum = float(input('Qual a porcentagem de aumento: '))
nv = sal*aum/100
print('O novo salario sera de R$ {:.2f}'.format(sal+nv))


#temperatura
temp = float(input('Digite o valor da temperatura em graus Celsius a ser covertida para fahrenheit: '))
print('{:.1f}º Graus Celsius são {:.1f}º Graus Fahrenheint'.format(temp, (temp*9/5)+32))

#aluguel
kmi = float(input('KM iniciais? '))
kmf = float(input('KM finais? '))
kmt = kmf-kmi
di = int(input('Quantidade de dias que foi alugado? '))

print('O total de dias alugado foi {} dias\n'
      'E um total de {:.2f}km rodados, gerando um total de R$ {:.2f} a pagar \n'
      'Sendo um total de R$ {:.2f} por dias alugado\n'
      'E um total de R$ {:.2f} por km rodados'.format(di, kmt, di*60+kmt*0.15, di*60, kmt*0.15))
