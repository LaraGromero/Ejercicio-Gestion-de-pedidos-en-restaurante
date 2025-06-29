print ("Verificar si una fecha es válida: Dado día, mes y año, determina si la fecha es válida (sin validar bisiesto).")
Dia= int(input("ingrese el dia en numero: "))
Mes= input("Ingrese el mes en palabra: ").lower()
A= int(input("Ingrese el año en numeros: "))
D1= {
    "enero":31,
     "febrero": 28,
     "marzo": 31,
     "abril": 30,
     "mayo": 31,
     "junio": 30,
     "julio": 31,
     "agosto": 31,
     "septiembre": 30,
     "octubre": 31,
     "noviembre": 30,
     "diciembre": 31
}
Dato= Mes in D1
if Dato:
    if Dia<=D1[Mes] and A<=2025:
        print ("Fecha Valida")
    else: 
        print ("Fecha Invalida")
else:
    print ("El mes registrado no es valido")