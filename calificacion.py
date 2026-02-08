calificaciones = []
cantidad = int(input("¿Cuántas calificaciones tienes? "))

for i in range(cantidad):
    nota = float(input(f"Ingresa la calificación {i+1}: "))
    calificaciones.append(nota)

promedio = sum(calificaciones) / len(calificaciones)

print(f"\nTus calificaciones: {calificaciones}")
print(f"Tu promedio es: {promedio:.2f}")

if promedio >= 7:
    print("¡Excelente trabajo! 🎉")
else:
    print("Sigue esforzándote 💪")