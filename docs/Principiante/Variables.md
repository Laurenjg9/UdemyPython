# *Variables en PYTHON*

__Las variables son un concepto en programacion que nos permite darle una etiqueta a un dato asi de esta forma podemos referirnos o referenciar ese dato usando la variable o "etiqueta" elegida para el.__

## Crear y guardar variables 

```python
name = input("Cual es tu nombre?: ")
name = "Lauren"
```
- Podemos adquirir los datos que se almacenaran en la variable
- Podemos crear variables con datos predefinidos

> __*Nota:*__ Es posible sobre escribir una variable ya definida, dependera del uso que le demos.

## Asignacion y reasignacion de variables

Es importante recordar que la asignacion de variables cumple la siguiente sintaxis:

> *Nombre de la variable* __=__ *Valor de la bariable*

Todo lo que yo ponga despues del igual "*=*" se asignara a la variable. Asi, a una variable ya existente, puedo reasignarle un nuevo valor.

```python
vaso1 = "Leche"
vaso2 = "Jugo"

vaso1, vaso2 = vaso2, vaso1

print(vaso1)  # Nuevo nombre "Jugo"
print(vaso2)  # Nuevo nombre "Leche"
```
- Para este ejemplo, se intercambio el contenido de las variables entre ellas. 
