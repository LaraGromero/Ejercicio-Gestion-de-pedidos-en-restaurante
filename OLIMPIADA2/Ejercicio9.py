meseros= ["Camila","David","Esteban"]
platos= ["Hamburguesas","Pizza","Ensalada"]

print ("----EJERCICIOS----")

if "Esteban" in meseros:
    meseros.append("Sofia")
    print (meseros)

if "Pizza" in platos:
    platos.append("Lasaña")
    print (platos)
    
if "David" in meseros:
    meseros.remove("David")
    print (meseros)
    
if len(platos) > 3:
    platos.pop(0)
    print (platos)
    
if "Camila" in meseros:
    meseros.remove("Camila")
    meseros.append("Juliana")    
    print (meseros)

turno_mañana= [meseros[0],meseros[1]]
print (turno_mañana)
menu_dia= [platos[-1],platos[-2]]
print (menu_dia)

if "Lasaña" in menu_dia:
    Plato_Especial=("Lasaña", 18000)
    print (menu_dia)

if "Juliana" in turno_mañana:
    Asignacion= {"Mesero": "Juliana",
                 "Plato": "Ensalada",
                 "Activa": "True"}
    print (Asignacion)
    if Asignacion in globals:
        Asignacion["Horario"]= "11:00 a.m. - 3:00 p.m."
        print (Asignacion)

if "Hamburguesa" not in platos:
    platos.append("Hamburguesa")
    print (meseros)
    
if "Esteban" not in meseros:
    meseros.append("Esteban")
    print (meseros)

else:
    print ("Nadita nada")
    

print ("--- FINAL ----")
print (f"Esta es la lista del personal del restaurantre: {meseros}")

print (f"Esta es la lista de los platos a servir en este restaurante {platos}")

print (f"Este es el turno de la mañana {turno_mañana}")

print (f"Este es el menu que se servira este dia {menu_dia}")

