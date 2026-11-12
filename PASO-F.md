# Paso F — Validar y corregir

## COOPAC FRONTERA SUR

Se revisan las tres comprobaciones del taller con los archivos disponibles. Los resultados distinguen entre datos verificados y evidencia que todavía falta.

| Comprobación | Resultado | Corrección o evidencia pendiente |
|---|---|---|
| Los pesos suman 1 y tienen justificación basada en el diagnóstico | **No validado para la organización.** La tabla de pesos de la guía es un ejemplo y no demuestra un acuerdo con esta gerencia. | Crear `PR02_pesos.md`, acordar y justificar cada peso antes de calcular. Verificar que la suma sea 1,00. |
| Ningún proyecto se programa antes de sus dependencias | **No verificable.** No están disponibles la lista de dependencias ni `PR05_hoja_ruta.csv`. | Ejecutar la revisión de dependencias y corregir fechas u olas antes de aprobar el cronograma. |
| El presupuesto anual respeta la capacidad real de gasto | **Validación histórica parcial.** En 2025 se planificaron S/ 1 240 000,00 y se ejecutaron S/ 1 144 727,35: 92,32 % de ejecución y S/ 95 272,65 por debajo del plan. | Esto confirma el cierre de 2025, no la capacidad de años futuros. Comparar el presupuesto de cada año del plan con su límite aprobado; esos límites aún no fueron proporcionados. |

## Evidencia presupuestal disponible

Según `presupuesto_ti.csv`, los subtotales de 2025 son:

| Tipo registrado | Planificado | Ejecutado |
|---|---:|---:|
| Operación | S/ 1 140 800,00 | S/ 1 030 973,58 |
| Inversión | S/ 99 200,00 | S/ 113 753,77 |
| **Total** | **S/ 1 240 000,00** | **S/ 1 144 727,35** |

La categoría «Inversión» es una aproximación a CAPEX y debe confirmarse con Contabilidad. El presupuesto histórico no sustituye los límites anuales aprobados para el periodo plurianual.

## Problemas y mejoras

Faltan los archivos del portafolio y del TCO, el acuerdo de pesos con gerencia, la hoja de ruta, el presupuesto plurianual y los límites presupuestales futuros. Sin ellos no se pueden cerrar PR07 ni certificar las dependencias y la capacidad del plan.

Antes de aprobar inversiones, establecer medición posterior de beneficios, actas de aceptación y control de desviaciones: los tres expedientes revisados carecen de medición del beneficio y registran desviaciones de hasta +46,6 %.