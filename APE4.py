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
