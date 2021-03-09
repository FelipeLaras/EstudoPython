print('calculando o IMC')
print('-' * 20)

#dados sendo informado pelo usuário
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso'))


#realizando o calculo

imc = (altura * altura) / peso


#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#ACima dos 40: Obesidade mórbida

#mostrando pro usuário