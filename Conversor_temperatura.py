# Função que apenas exibe o menu de opções na tela

def exibir_menu():
    print("\n--- CONVERSOR DE TEMPERATURA ---")
    print("1. Fahrenheit para Celsius")
    print("2. Celsius para Fahrenheit")
    print("3. Sair")
    
# Loop infinito para manter o programa rodando até que o usuário decida sair

while True:
# Chama a função para mostrar o menu na tela    
  exibir_menu ()
# Solicita que o usuário escolha uma das opções do menu
    
  opcao = input("\nEscolha uma opção (1-3): ")
    
# Se a opção for 3, o programa exibe uma mensagem e encerra o loop (break)
    
  if opcao == "3":
      print ("Programa encerrado. Até Logo!")
      break
      
# Verifica se a opção digitada é uma das opções válidas de cálculo (1 ou 2) 
    
  if opcao in ['1', '2']:
       temp= float (input ('Digite a temperatura:'))

# Se a opção for 1, faz o cálculo de Fahrenheit para Celsius
   
       if opcao == '1':
              resultado = (temp- 32) * 5 / 9
              print ( f'{temp} ºF é equivalente {resultado:.2f} ºC')
# Se a opção for 2, faz o cálculo de Celsius para Fahrenheit  
      
       elif opcao == '2':
              resultado = temp * 1.8 + 32
              print ( f'{temp} ºC é equivalente {resultado:.2f} ºF') 
              break
       else:
        print ('Opção invalida- Digite a opção 1,2 ou 3')
         
