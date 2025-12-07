#Reloj Kyd
#GonzalezAcosta Jesus 278080

Horas = 00,24
Minutos = 00, 60
Segundos = 00, 60

for hora in range (0,24):
    for minutos in range (0,60):
        for segundos in range (00,60):
            if hora < 10:
                if segundos <10:
                    print (f"0{hora}:{minutos}:{segundos}")
        else:
            print (f"{hora}:{minutos}:{segundos}")