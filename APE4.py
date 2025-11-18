#------------------------------------
#-------LO QUE LE TOCA A SAM---------
#------------------------------------

# Entrada de datos básicos
nombre = input("Ingresa tu nombre: ")
ciudad = input("Ingresa tu ciudad: ")
hobby = input("Ingresa tu hobby favorito: ")

# Concatenación y creación de mensajes
mensaje1 = "Hola " + nombre + ", espero que disfrutes tu día en " + ciudad + "!"
mensaje2 = nombre + " disfruta mucho " + hobby + " cuando tiene tiempo libre."
mensaje3 = f"{nombre} vive en {ciudad} y le encanta {hobby}."

#------------------------------------
#-------MENSAJES CONCATENADOS--------
#------------------------------------
print("\n=== MENSAJE CONCATENADO 1 ===")
print(mensaje1, "\n")

print("=== MENSAJE CONCATENADO 2 ===")
print(mensaje2, "\n")

print("=== MENSAJE CONCATENADO 3 ===")
print(mensaje3, "\n")

# Mensajes adicionales combinando diferentes estilos
mensaje4 = f"¿Sabías que {nombre} siempre encuentra tiempo para {hobby} en {ciudad}?"
mensaje5 = f"Si visitas {ciudad}, seguramente te encontrarás con {nombre} disfrutando de {hobby}."
mensaje6 = "Recordatorio: " + nombre + " no olvida nunca disfrutar de " + hobby + " sin importar la ciudad."

print("=== MENSAJE CONCATENADO 4 ===")
print(mensaje4, "\n")

print("=== MENSAJE CONCATENADO 5 ===")
print(mensaje5, "\n")

print("=== MENSAJE CONCATENADO 6 ===")
print(mensaje6, "\n")

# Mensaje aleatorio usando f-string y concatenación
import random
plantillas = [
    f"{nombre} vive aventuras en {ciudad} mientras disfruta de {hobby}.",
    f"En {ciudad}, {nombre} se dedica a {hobby} con pasión.",
    f"{nombre} aprovecha cada momento libre en {ciudad} para {hobby}."
]
mensaje_aleatorio = random.choice(plantillas)
print("=== MENSAJE ALEATORIO ===")
print(mensaje_aleatorio, "\n")

#------------------------------------
#-------LO QUE LE TOCA A ANI---------
#------------------------------------

print("=== EXTRACCIÓN Y FORMATO ===")
# Tomando subcadenas
nombre_extraido = mensaje3[0:len(nombre)]  # corta solo el nombre
print("Nombre extraído:", nombre_extraido, "\n")

# Mayúsculas y minúsculas
print("Mensaje en mayúsculas:")
print(mensaje3.upper(), "\n")

print("Mensaje en minúsculas:")
print(mensaje3.lower(), "\n")

#------------------------------------
#-------LO QUE LE TOCA A JENI--------
#------------------------------------
print("=== CONTEO Y REEMPLAZO ===")
# Contar y reemplazar
veces = mensaje3.count("y")
print(f"La palabra 'y' aparece {veces} veces.\n")

mensaje_final = mensaje3.replace(hobby, "programar")  # reemplaza hobby por otra cosa
print("Mensaje final con reemplazo:")
print(mensaje_final, "\n")
