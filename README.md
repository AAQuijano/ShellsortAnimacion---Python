# ShellSort Animación

Proyecto final del curso Análisis y Diseño de Algoritmos - Universidad Tecnológica de Panamá.

## Autor
- Quijano Antonio   8-908-1148

## Profesor
- Samuel Jimenez

## Grupo
- 1SF-121

## Año
- 2019

## Descripción
Animación visual del algoritmo de ordenamiento ShellSort implementada en Python usando Tkinter.

## Requisitos
- Python 3.x
- Tkinter (incluido en Python)

## Archivos

### 1. ShellSort_Animation.py
Versión básica con animación de intercambio únicamente.

**Características:**
- Solo muestra la animación cuando se realiza un intercambio
- Los elementos se mueven y intercambian de posición
- Contador de intercambios

### 2. ShellSort_Animation_withComparison.py
Versión completa con animación de comparación e intercambio.

**Características:**
- **Animación de comparación**: Muestra visualmente cuando se comparan dos elementos (color cyan y símbolo ">" entre ellos)
- **Indicador de resultado**: Color verde si el primer número es mayor, rojo si es menor
- **Animación de intercambio**: Los elementos se mueven y intercambian después de la comparación
- Contador de intercambios

## Uso
1. Ejecutar cualquiera de los archivos `.py`
2. Ingresar números en el campo de texto
3. Click en "Agregar Numero" para agregar a la lista
4. Click en "Ordenar Lista" para ver la animación
5. Click en "Nueva Lista" para reiniciar o detener el ordenamiento

## Controles
- **Agregar Numero**: Ingresa un número entero al arreglo (máximo 11)
- **Ordenar Lista**: Inicia la animación del algoritmo ShellSort
- **Nueva Lista**: Limpia el arreglo actual y detiene el ordenamiento si está activo

## Algoritmo
El programa implementa el algoritmo ShellSort que es una generalización del ordenamiento por inserción. Funciona ordenando el arreglo comparando elementos separados por un gap (intervalo) que se reduce gradualmente hasta llegar a 1.
