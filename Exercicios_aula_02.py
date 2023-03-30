#Faça um programa que peça quatro número e imprima o maior deles.

num1 = int(input("insira o primeiro número: "))
num2 = int(input("insira o segundo número: "))
num3 = int(input("insira o terceiro número: "))
num4 = int(input("insira o quarto número: "))
           
if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"O maior número é o {num1}")
    
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"O maior número é o {num2}")

elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"O maior número é o {num3}")

elif num4 > num1 and num4 > num2 and num4 > num3:
    print(f"O maior número é o {num4}")
    
else:
    print("Aí não, né?")
    
################################################################################################
#Monte um programa que permita o uso de um elevador com capacidade máxima para 8 pessoas.

pessoas = int(input("Quantas pessoas entraram no elevador? "))

if pessoas > 0 and pessoas < 9:
    print("Cabe sim, podem usar suave")

elif pessoas == 0:
    print("Elevador parado")

else:
    print("Uso proibido ou impossível")
    
################################################################################################
#Monte um programa que cadastre uma senha, e depois valide essa senha cadastrada com 3 tentativas; caso erre 3 vezes, o usuário terá o celular bloqueado.

senha = int(input("Cadastre sua primeira senha: "))
  print("senha cadastrada")

for tentativa in range(3):
    login = int(input("Informe sua senha cadastrada: "))
    if login == senha:
        print("Senha correta!")
        break
    elif tentativa in range(2):
        print("Senha incorreta. Tente novamente!")
        
if login != senha:
      print ("Celular Bloqueado. Procure contato com o suporte!")
    
##################################################################################################
#Monte um somador onde a quantidade de somas que vão acontecer seja inserida pelo usuário; e depois, os números a serem somados também.

n = int(input("Digite a quantidade de vezes que você vai somar números: " ))
soma = 0

for boiDePiranha in range(n):
    var1 = int(input("Digite um número a somar: "))
    soma = soma + var1
    #soma += var1
    print(soma)

print(f"O resultado da sua soma foi {soma}")
print("Fim de jogo!")

#Outra alternativa:

senha = int(input('cadastre sua primeira senha:'))
print('senha cadastrada')
cont = 0
for tentativa in range(3):
    conf = int(input('Confirme a senha cadastrada: '))
    if conf == senha:
        print('senha confirmada')
        break
    elif conf != senha:
        cont = cont + 1
        if cont == 3:
            print('celular bloqueado')
            break
        print('Senha incorreta, tente novamente')

print('Saiu')

#################################################################################
#Pra fazer um programa que o usuário insira se é masculino ou feminino; e tentar novamente até conseguir, com 5 tentativas
for tentativa in range(5):
    info = input("Insira (F) pra Feminino e (M) para Masculino: ").upper()
    if info == "F":
        print("É feminino")
        break
    elif info == "M":
        print("É masculino")
        break
    else:
        print("Tente novamente")
        
############################################################################################################
#Pra fazer uma calculadora, com 2 números e o usuário decidindo a operação a ser feita:

var = int(input('informe um numero: '))
var1 = int(input('informe outro numero'))

for calc in range(2):
    op = int(input('Digite:\n1 +\n2 *\n3 /\n4 -\n5 SAIR\nE ai parceiro?'))
    if op == 1:
        print(var + var1)
    elif op == 2:
        print(var * var1)
    elif op == 3:
        print(var / var1)
    elif op == 4:
        print(var - var1)
    elif op == 5:
        print('saiu')
        break
