Algoritmo Registro
	//00000278080 Gonzalez Acosta Jesus
	
	Definir numDias, diaMayorC, dia como entero 
	Definir consumoDia, mayorConsumo, totalLitros, totalKm, distanciaP, rendimiento como real 
	
	totalLitros <- 0
	totalKm <- 0 
	mayorConsumo <- 0
	diaMayorC <- 0
	
	Escribir "Ingrese el numero de dias a registrar:"
	Leer numDias
	
	para dia <- 1 hasta numDias Con Paso  1 Hacer
		Escribir "Dia", dia, ":" 
		Escribir "Kilometros recorridos:"
		Leer kilometrosDia
		Escribir "Consumo del combustible (Litros):"
		Leer consumoDia
		
		totalKm <- totalKm + kilometrosDia
		totalLitros <- totalLitros + consumoDia
		
		Si consumoDia > mayorConsumo entonces 
			mayorConsumo <- consumoDia
			diaMayorC <- dia 
		FinSi
	FinPara
	
	distanciaP <- totalKm / numDias
	
	si totalKm > 0 Entonces
		rendimiento <- totalKm / totalLitros
	Sino 
		rendimiento <- 0
	FinSi
	
	Escribir "Resultados del mes:"
	Escribir "Dia con mayor consumo:", diaMayorC
	Escribir "Total de Kilometros recorridos:", totalKm
	Escribir "Total Litros consumidos:", totalLitros
	Escribir "Distancia promedio por dia:", distanciaP
	Escribir "Rendimiento del vehiculo:", rendimiento
	
FinAlgoritmo
