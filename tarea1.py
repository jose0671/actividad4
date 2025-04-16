estudiantes = []
may = 0
men = 0
cantidad = int(input("¿Cuántos estudiantes va a registrar? "))
for i in range(cantidad):
        print(f"\nRegistro del estudiante {i+1}:")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))

        if edad >= 18:
            print(f"{nombre} es **mayor de edad**.")
            may += 1
        else:
            print(f"{nombre} es **menor de edad**.")
            men += 1

        edad_futura = edad + 5
        print(f"En 5 años, {nombre} tendrá {edad_futura} años.")

        estudiantes.append((nombre, edad))

print("\n RESUMEN DEL REGISTRO")
print(f"Total de estudiantes registrados: {cantidad}")
print(f"Mayores de edad: {may}")
print(f"Menores de edad: {men}")


numero = int(input("\nIngresa un número para ver su tabla de multiplicar: "))
print("\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")



