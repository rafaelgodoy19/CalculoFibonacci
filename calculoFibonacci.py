#Rafael Richard Alves de Godoy / Vida Nova Tec
#Fibonacci / exercicio 02 python
quantidade = 1
   
print("Bem vindo ao programa de calculo de fibonacci!")

while (quantidade != 0): #Repeticao ate o usuario digitar 0 (zero)
   
    quantidade = int(input("\n\nDigite a quantidade que deseje calcular ou 0 (zero) para finalizar: "))
    num1 = 0
    num2 = 1
    aux = 0
    contador = 0
   
    print("Sequencia fibonacci ->", end = " ") 
    while(contador < quantidade):  #Repeticao até a quantidade que o usuario digitou
        print(aux, end = " ")	 #Imprime a sequencia fibonacci
       	
	#Calculo do fibonacci
	
        num1 = num2
        num2 = aux
        aux = num1 + num2
        contador += 1