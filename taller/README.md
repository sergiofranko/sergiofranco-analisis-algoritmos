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
