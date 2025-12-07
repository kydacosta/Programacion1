Algoritmo SucesionFibonacci
	Definir N, a, b, siguiente como entero
	Escribir "Ingresa la cantidad de terminos de la sucesion de Fibonacci que desea ver"
	Leer N
	
	Si N <= 0 Entonces
		Escribir "El numero de terminos debe ser un entero positivo"
	Sino 
		Si N = 1 Entonces 
			Escribir "Los primeros 1 terminos de Fibonacci son:"
			Escribir "0"
		Sino 
			a <- 0
			b <- 1
			
			Escribir "Los primeros", N, "terminos de Fibonacci son:"
			Escribir a
			Escribir b
			
			Para i <- 3 hasta N con paso 1 hacer
				siguiente <- a + b
				escribir siguiente
				
				a <- b
				b <- siguiente
			FinPara
		FinSi
	FinSi
FinAlgoritmo	