# Funcion "Input()"

Esta funcion nos permite adquirir datos del usuario

```python
input("Cuantos años tienes?: ")
```

### Usando concatenacion, print() e input() juntos
Es posible anidar estas dos funciones para capturar informacion al tiempo que mostramos mensajes en la consola:

```python
print("Hola " + input("Cual es tu nombre?: "))
```
> *__Nota:__* Dado que python lee linealmente el codigo y de adentro hacia afuera, primero ejecutara el input y luego el print.