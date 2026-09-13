def exibir_menu():
    print("\n--- CONVERSOR DE TEMPERATURA ---")
    print("1. Fahrenheit para Celsius")
    print("2. Celsius para Fahrenheit")
    print("3. Sair")

while True:
  exibir_menu ()
  opcao = input("\nEscolha uma opção (1-3): ")

  if opcao == "3":
      print ("Programa encerrado. Até Logo!")
      break

  
  if opcao in ['1', '2']:
       temp= float (input ('Digite a temperatura:'))
     
       if opcao == '1':
              resultado = (temp- 32) * 5 / 9
              print ( f'{temp} ºF é equivalente {resultado:.2f} ºC')
             
       elif opcao == '2':
              resultado = temp * 1.8 + 32
              print ( f'{temp} ºF é equivalente {resultado:.2f} ºC') 

       else:
        print ('Opção invalida- Digite a opção 1,2 ou 3')
         