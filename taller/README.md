# Taller · Cinco familias en LeetCode

**Curso:** Análisis de algoritmos · ITM · 2026-2  
**Tipo:** clase taller (evaluación)  
**Presentado por:** Sergio Esteban Franco Agudelo

---

## Ejercicio 1 · [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

## Familia algorítmica

**Ordenamiento — Merge Sort**

Se implementa Merge Sort manualmente para ordenar los intervalos según su valor inicial. No se utilizan las funciones `.sort()` ni `sorted()`.

Después de ordenar los intervalos, se realiza un recorrido lineal. Si el intervalo actual se superpone o se conecta con el último intervalo guardado, ambos se fusionan. De lo contrario, el intervalo se agrega al resultado.

## Complejidad

- **Tiempo:** `O(n log n)`, debido al ordenamiento mediante Merge Sort. El recorrido para fusionar los intervalos toma `O(n)`.
- **Espacio:** `O(n)`, por las listas auxiliares utilizadas durante el ordenamiento y la fusión.

## Evidencias

### Ejercicio, cuenta de LeetCode y código

![Ejercicio, cuenta y código](./evidencias/01-merge-intervals-codigo.png)

### Resultado Accepted

![Resultado Accepted](./evidencias/02-merge-intervals-accepted.png)

---

## Ejercicio 2 · [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

## Familia algorítmica

**Grafos — recorrido en profundidad (DFS)**

## Modelo del grafo

La grilla representa un grafo implícito:

- **Vértice:** cada celda cuyo valor sea `"1"`.
- **Arista:** existe entre dos celdas de tierra vecinas en dirección horizontal o vertical.
- **Tipo de grafo:** no dirigido, porque la conexión entre dos celdas funciona en ambos sentidos.
- Las celdas con `"0"` representan agua y no forman parte del grafo.
- Las celdas diagonales no se consideran vecinas.

## Idea de la solución

Se recorren todas las celdas de la grilla. Cada vez que se encuentra una celda de tierra que no ha sido visitada, se incrementa el número de islas y se inicia un DFS iterativo.

El DFS utiliza una pila para recorrer toda la componente conexa. Cada celda visitada se cambia de `"1"` a `"0"`, evitando que vuelva a ser procesada.

Al finalizar, el contador contiene el número de componentes conexas de tierra, es decir, el número de islas.

## Complejidad

Sea `m` la cantidad de filas y `n` la cantidad de columnas:

- **Tiempo:** `Θ(m × n)`, porque cada celda se procesa como máximo una vez.
- **Espacio:** `O(m × n)` en el peor caso, porque la pila puede almacenar una gran cantidad de celdas de una misma isla.

## Evidencias

### Ejercicio, cuenta de LeetCode y código

![Ejercicio, cuenta y código](./evidencias/03-number-of-islands-codigo.png)

### Resultado Accepted

![Resultado Accepted](./evidencias/04-number-of-islands-accepted.png)