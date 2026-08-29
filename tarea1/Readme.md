# Tarea 1 · Algoritmos greedy en LeetCode

## ![Lemonade Change](evidencias/lemonade-change-accepted.png) 

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
