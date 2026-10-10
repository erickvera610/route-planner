# Evidencia de validación automatizada

Se ejecutaron diez escenarios diferentes con datos ficticios o sintéticos. Este informe describe ejecuciones reales del código mediante un script automatizado. No representa tráfico de usuarios, experiencia laboral ni contribuciones realizadas manualmente por Erik.

Resultado: **10 de 10 escenarios aprobados**.

Consulta `validation-results.json` para ver cada entrada, resultado y fecha UTC de ejecución.

## Repetir las ejecuciones

Desde la carpeta del repositorio ejecuta:

```bash
python validate_scenarios.py
```

En Mercado Aprende instala primero las dependencias del README. En los otros cinco proyectos basta Python. El script utiliza almacenamiento temporal: no cambia registros personales ni realiza compras reales. Regenera el informe local; para conservar nuevos resultados en GitHub debes revisarlos y hacer un commit.

## Qué se comprobó

| Escenario | Entrada | Resultado |
|---|---|---|
| 1 | {"blocked": [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11]]} | Aprobado |
| 2 | {"blocked": [[2, 0], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11]]} | Aprobado |
| 3 | {"blocked": [[3, 0], [3, 1], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11]]} | Aprobado |
| 4 | {"blocked": [[4, 0], [4, 1], [4, 2], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11]]} | Aprobado |
| 5 | {"blocked": [[5, 0], [5, 1], [5, 2], [5, 3], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11]]} | Aprobado |
| 6 | {"blocked": [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11]]} | Aprobado |
| 7 | {"blocked": [[7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11]]} | Aprobado |
| 8 | {"blocked": [[8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 8], [8, 9], [8, 10], [8, 11]]} | Aprobado |
| 9 | {"blocked": [[9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 9], [9, 10], [9, 11]]} | Aprobado |
| 10 | {"blocked": [[10, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 10], [10, 11]]} | Aprobado |
