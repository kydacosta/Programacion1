Algoritmo RelojdeArena
	//Gonzalez Acosta Jesus
	//00000278080
	
	Definir num, a, e, espacios, asteriscos Como Entero
	
	Escribir "Ingrese un numero impar."
	Leer num
	
	Mientras num Mod 2 = 0 O num <= 3
		Escribir "El numero debe ser impar. Intente nuevamente."
		leer num
	FinMientras
	
	Para a = num hasta 1 con paso -2
		espacios = (num - a) / 2
		para e = 1 hasta espacios
			escribir sin saltar " " 
		FinPara
		Para e = 1 hasta a
			escribir sin saltar "*"
		FinPara
		Escribir ""
	FinPara
	
	Para a = 3 hasta num con paso 2 
		espacios = (num - a) / 2
		para j = 1 hasta espacios 
			Escribir  sin saltar " "
		FinPara
		Para e = 1 hasta a 
			escribir sin saltar "*" 
		FinPara
		escribir ""
	FinPara
	
FinAlgoritmo
	