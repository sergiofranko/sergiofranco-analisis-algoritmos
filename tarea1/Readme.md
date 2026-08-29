# Tarea 1 · Algoritmos greedy en LeetCode

## ![Lemonade Change](https://leetcode.com/problems/lemonade-change/description/) 

### Criterio greedy:
Aquí el punto clave es como manejar la devuelta cuando el pago es con un billete de $20, puesto que hay que devolver $15.
- *Prioridad 1:* Devolver un billete de $10 y uno de $5, los billetes de $10 solo sirven para devolver de un billete de $20, por eso, hay que soltarlos a la menor oportunidad.
- *Prioridad 2:* Devolver 3 billetes de $5, los billetes de 5 son los más valiosos en este caso, pues nos sirven para devolver tanto para billetes de $10, como para billetes de $20. La idea es solo devolver 3 billetes de $5 si no hay otra opción.

### Rendimiento:
- *Complejidad de tiempo:* O(n) porque solo se recorre la lista de clientes o billetes una sola vez.
- *Complejidad de espacio:* O(1) porque solo son utilizadas dos variables tipo int fijas para el conteo.

### Evidencia:
- ![Statement and resolution code — Lemonade Change](evidencias/01-lemonade-change-statement-and-code.png)
- ![Accepted and runtime — Lemonade Change](evidencias/02-lemonade-change-accepted-runtime.png)
- ![Accepted and memory — Lemonade Change](evidencias/03-lemonade-change-accepted-memory.png)


## ![455. Assign Cookies](https://leetcode.com/problems/assign-cookies/description/) 

### Criterio greedy:
Aquí el ordenamiento es clave, de esta manera evitamos desperdiciar una galleta grande en un niño que se hubiese satisfecho con una más pequeña.
También el uso de los punteros es fundamental. Avanzar el puntero de galleta en cada iteración es primordial, pues si la galleta actual, no satisface al niño actual, tampoco satisfará al niño siguiente, pues este tiene más hambre (esto garantizado por el ordenamiento), por lo que es lógico descartar esta galleta.

### Rendimiento:
- *Complejidad de tiempo:* O(nlog n + mlog m), donde n es el número de niños y m el de galletas. Esto se debe al paso inicial de ordenar las listas (El loop siguiente al ordenamiento es lineal solamente O(n + m)).
- *Complejidad de espacio:* O(1) puesto que el ordenamiento se hace sobre los mismos arreglos, entonces no usamos memoria extra.

### Evidencia:
- ![Statement and resolution code — Assign Cookies](evidencias/04-assign-cookies-statement-and-code.png)
- ![Accepted and runtime — Assign Cookies](evidencias/05-assign-cookies-accepted-runtime.png)
- ![Accepted and memory — Assign Cookies](evidencias/06-assign-cookies-accepted-memory.png)
