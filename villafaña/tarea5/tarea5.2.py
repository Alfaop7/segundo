# Mensaje original
mensaje = "¡Hola Mundo!"

# Convertir el mensaje a bytes
mensaje_bytes = mensaje.encode()

# Decodificar los bytes a una cadena
mensaje_decodificado = mensaje_bytes.decode()

print(mensaje_bytes)       # Mostrará el mensaje en formato de bytes
print(mensaje_decodificado) # Mostrará el mensaje decodificado de nuevo a cadena
