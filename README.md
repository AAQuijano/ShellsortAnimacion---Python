# ShellSort Animación

Proyecto final del curso Análisis y Diseño de Algoritmos — Universidad Tecnológica de Panamá.

| | |
|---|---|
| **Autor** | Antonio Quijano |


## Descripción

Animación visual del algoritmo de ordenamiento **ShellSort** implementada en Python con Tkinter. Los números se representan como círculos en un canvas y la aplicación muestra gráficamente el proceso de comparación e intercambio paso a paso.

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `ShellSort_Animation.py` | Versión básica — animación de intercambio únicamente |
| `ShellSort_Animation_withComparison.py` | Versión completa — animación de comparación e intercambio |


### 1. ShellSort_Animation.py

Versión básica que solo anima el intercambio entre elementos.

- Los elementos involucrados cambian a color **dorado** (`gold4`)
- Se separan verticalmente y luego se intercambian horizontalmente
- Contador de intercambios en pantalla

### 2. ShellSort_Animation_withComparison.py

Versión completa que agrega una animación previa de comparación antes del intercambio.

- **Comparación**: los dos elementos se pintan de **cyan** y aparece el símbolo `>` entre ellos
- **Resultado**: ambos bajan juntos y el símbolo `>` se vuelve **verde** si el primero es mayor, o **rojo** si es menor
- **Intercambio**: si corresponde, se ejecuta la misma animación de la versión básica
- Contador de intercambios en pantalla

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)

No requiere librerías externas.

## Uso

```bash
python ShellSort_Animation.py
# o
python ShellSort_Animation_withComparison.py
```

1. Aparece una **pantalla de presentación** con los datos del proyecto
2. Haz clic en **"Cerrar Ventana"** para ir al programa principal
3. Escribe un número entero en el campo de texto
4. Presiona **"Agregar Numero"** para añadirlo a la lista (máx. 11 elementos)
5. Presiona **"Ordenar Lista"** para iniciar la animación
6. Presiona **"Nueva Lista"** para reiniciar o detener el ordenamiento en cualquier momento

## Controles

| Botón | Función |
|---|---|
| **Agregar Numero** | Agrega el número ingresado a la lista (máx. 11) |
| **Ordenar Lista** | Inicia la animación del algoritmo |
| **Nueva Lista** | Limpia la lista y detiene el algoritmo si está en ejecución |

## Algoritmo

El programa implementa un algoritmo **híbrido ShellSort + BubbleSort**:

1. **Fase ShellSort**: comienza con un `gap = n // 2` y se reduce recursivamente dividiendo entre 2. En cada paso se comparan e intercambian elementos separados por el gap actual.
2. **Fase BubbleSort**: cuando `gap = 0` se ejecuta un BubbleSort estándar (`n` pasadas en la versión básica, `n // 2` en la versión con comparación) para finalizar el ordenamiento.

La animación se realiza mediante `canvas.move()` con `time.sleep()` para controlar la velocidad.

## Notas técnicas

- El protocolo de cierre de ventana contiene un typo: `"WN_DELETE_WINDOW"` en lugar de `"WM_DELETE_WINDOW"` (no afecta el funcionamiento en Windows).
- Los números se representan como óvalos (`create_oval`) con texto superpuesto (`create_text`).
- El algoritmo utiliza recursión para reducir el gap progresivamente.
- El hilo de la interfaz se bloquea durante la animación (`time.sleep()` en el main loop), por lo que no se puede interactuar con la ventana mientras ordena.
