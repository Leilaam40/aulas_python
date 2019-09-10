a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma}. \nSubtração: {subtracao}.' 
        '\nmultiplicação: {multiplicacao}' 
        '\ndivisão:{divisao} .\nresto: {resto}'
      .format(soma=soma,
              subtracao=subtracao,
              multiplicacao=multiplicacao,
              divisao=divisao,
              resto=resto))
print(resultado)
#print('soma: {}'.format(soma))
#print("soma: " + str(soma))
#print(substracao)
#print(multiplicacao)
#print(int(divisao))
#print(resto)