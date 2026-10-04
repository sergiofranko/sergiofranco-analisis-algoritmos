# 1143. Longest Common Subsequence

## Enlace del ejercicio

[LeetCode - Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

## Familia algorítmica

Programación dinámica.

## Idea de la solución

Se construye una tabla que guarda la longitud de la subsecuencia común más larga para cada combinación de prefijos de las dos cadenas.

La solución utiliza tabulación de abajo hacia arriba. Primero se resuelven los prefijos más pequeños y luego se utilizan esos resultados para calcular los prefijos más grandes.

No se reconstruye la subsecuencia porque el ejercicio únicamente solicita su longitud.

## Estado

Se define:

```text
dp[i][j]
```

como la longitud de la subsecuencia común más larga entre los prefijos:

```text
text1[0..i)
text2[0..j)
```

Esto significa que se consideran los primeros `i` caracteres de `text1` y los primeros `j` caracteres de `text2`.

## Caso base

Si uno de los prefijos está vacío, no puede existir una subsecuencia común:

```text
dp[0][j] = 0
dp[i][0] = 0
```

Por esta razón, la primera fila y la primera columna de la tabla se inicializan con cero.

## Recurrencia

Si los caracteres actuales son iguales:

```text
text1[i - 1] == text2[j - 1]
```

se incluye ese carácter en la subsecuencia:

```text
dp[i][j] = 1 + dp[i - 1][j - 1]
```

Si los caracteres son diferentes:

```text
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

Se escoge el mejor resultado entre ignorar el carácter actual de `text1` o ignorar el carácter actual de `text2`.

La respuesta final queda almacenada en:

```text
dp[n][m]
```

## Complejidad

Sean `n` la longitud de `text1` y `m` la longitud de `text2`:

- Tiempo: `Θ(n × m)`, porque se calculan todas las posiciones de la tabla.
- Espacio: `Θ(n × m)`, porque se almacena una tabla de `(n + 1) × (m + 1)` posiciones.

## Evidencias

### Ejercicio, cuenta de LeetCode y código

![Ejercicio, cuenta y código](../evidencias/05-longest-common-subsequence-codigo.png)

### Resultado Accepted

![Resultado Accepted](../evidencias/06-longest-common-subsequence-accepted.png)