#Substraccion: Me permite substraer elementos de un caracter segun la posicion que elija
print("Hola"[-1])

#String
print("123"+"456")

#Entero
print(123+345)
print(123_456_3254) #Aun usando guion bajo, lo interpreta como un entero

#Float
print(3.1416)

#Boolean
print(True)
print(False)

Lista_dict = [{"nombre":"Lauren"},{"nombre":"Valeria"},{"nombre":"Maria"},{"nombre":"Juliana"}]
print(type(Lista_dict))
print(Lista_dict[2])

#lenght
len("hello")
len("65468798")

# CastingL

print(int("123")+int("234"))

print(f"Number fo letters in your name: {len(input("Enter your name: ").strip())}")

Nombre = input("Cual es tu nombre?: ")
letras = len(Nombre.strip())

print("Numero de letras en tu nombre: " + str(letras))

print(3 * (3 + 3) / 3 - 3)