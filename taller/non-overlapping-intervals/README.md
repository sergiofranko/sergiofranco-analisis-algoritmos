# 435. Non-overlapping Intervals

## Enlace del ejercicio

[LeetCode - Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

## Familia algorítmica

Greedy.

## Idea de la solución

El problema se puede interpretar como una selección de actividades.

Minimizar la cantidad de intervalos eliminados equivale a maximizar la cantidad de intervalos que pueden conservarse sin solaparse.

Primero se ordenan los intervalos según su punto de finalización. Después se recorren en ese orden y se seleccionan los que no se solapan con el último intervalo aceptado.

La respuesta se calcula de la siguiente manera:

```text
intervalos eliminados = total de intervalos - intervalos seleccionados
```

## Criterio greedy

En cada paso se selecciona, entre los intervalos disponibles, el que termina primero.

Este criterio deja libre la mayor cantidad de espacio posible para aceptar otros intervalos posteriormente.

Después de seleccionar un intervalo, el siguiente se acepta únicamente cuando:

```text
inicio del siguiente >= final del último seleccionado
```

La igualdad está permitida. Por ejemplo, `[1, 2]` y `[2, 3]` no se solapan.

Si el siguiente intervalo comienza antes de que termine el último seleccionado, se descarta porque ambos se solapan.

## Complejidad

Sea `n` la cantidad de intervalos:

- Tiempo: `O(n log n)`, debido al ordenamiento. El recorrido greedy posterior toma `O(n)`.
- Espacio: `O(n)` en el peor caso por el espacio auxiliar que puede utilizar el algoritmo de ordenamiento de Python. El recorrido greedy utiliza `O(1)` de espacio adicional.

## Evidencias

### Ejercicio, cuenta de LeetCode y código

![Ejercicio, cuenta y código](../evidencias/07-non-overlapping-intervals-codigo.png)

### Resultado Accepted

![Resultado Accepted](../evidencias/08-non-overlapping-intervals-accepted.png)