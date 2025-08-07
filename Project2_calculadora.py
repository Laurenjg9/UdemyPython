# Hacer un programa que permita calcular cuando debe pagar una persona al dividir la factura
print("Vamos a dividir esa factura de forma facil!")
total = float(input("Cuanto es el total de la factura?: "))
propina = int(input("Van a dejar propina? 0%, 4%, 10%: "))
num_personas = int(input("Cuantos estuvieron en el parche?: "))

tip = float(total/100 * propina)
total_factura = total+tip
print(f"El total de tu factura con una propina de ${tip}, seria: ${total_factura}")

total_pagar = int(total_factura/num_personas)
print(f"Cada persona debe de pagar: ${total_pagar}")


