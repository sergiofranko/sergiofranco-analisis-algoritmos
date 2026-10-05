# 39. Combination Sum

## Enlace del ejercicio

[LeetCode - Combination Sum](https://leetcode.com/problems/combination-sum/)

## Familia algorítmica

Backtracking.

## Idea de la solución

Se construyen las combinaciones mediante una búsqueda recursiva.

En cada nivel se elige uno de los candidatos disponibles y se resta su valor de la cantidad que falta para llegar al objetivo.

Un candidato puede utilizarse varias veces. Por esta razón, después de elegir `candidates[index]`, la siguiente llamada recursiva puede continuar desde el mismo índice.

Para evitar combinaciones repetidas con distinto orden, la búsqueda nunca vuelve a índices anteriores. Así, si se genera `[2, 2, 3]`, no se genera también `[3, 2, 2]`.

## Estado de la búsqueda

Cada llamada mantiene los siguientes datos:

- `start_index`: primer índice que se puede elegir.
- `remaining`: cantidad que falta para alcanzar el objetivo.
- `current`: combinación construida hasta ese momento.

## Elección

Para explorar una rama se agrega el candidato actual a la combinación:

```text
current.append(candidate)
```

Luego se continúa la búsqueda desde el mismo índice:

```text
search(index, remaining - candidate)
```

Conservar el mismo índice permite reutilizar el candidato las veces que sea necesario.

## Caso exitoso

Cuando `remaining` llega a cero, la combinación suma exactamente el objetivo.

Se almacena una copia de la combinación actual:

```text
result.append(current[:])
```

Es necesario guardar una copia porque `current` continúa cambiando durante el resto de la búsqueda.

## Poda

Cuando `remaining` es menor que cero, la combinación superó el objetivo.

Esa rama se detiene porque todos los candidatos son positivos y agregar más valores no puede convertir el resultado en una suma válida.

## Backtracking

Después de regresar de la llamada recursiva, se deshace la última elección:

```text
current.pop()
```

Esto restaura la combinación al estado anterior y permite probar el siguiente candidato.

## Complejidad

Sean:

- `n` la cantidad de candidatos.
- `t` el valor objetivo.
- `minimum` el menor valor de `candidates`.
- `d = t / minimum` la profundidad máxima aproximada de la búsqueda.
- `S` la cantidad de combinaciones encontradas.

La complejidad es:

- Tiempo: `O(n^d × d)` en el peor caso. El árbol de búsqueda puede tener hasta `n` decisiones por nivel y cada solución puede requerir una copia de hasta `d` elementos.
- Espacio auxiliar: `O(d)` por la pila de recursión y la combinación actual.
- Espacio de salida: `O(S × d)` para almacenar todas las combinaciones encontradas.

La complejidad es exponencial porque el algoritmo debe enumerar las combinaciones posibles.

## Evidencias

### Ejercicio, cuenta de LeetCode y código

![Ejercicio, cuenta y código](../evidencias/09-combination-sum-codigo.png)

### Resultado Accepted

![Resultado Accepted](../evidencias/10-combination-sum-accepted.png)