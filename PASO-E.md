# Paso E — Declarar lo que no se hará y redactar

## COOPAC FRONTERA SUR

> **Alcance del desarrollo.** Este borrador usa `FICHA.md`, `presupuesto_ti.csv`, `inversiones_cerradas.csv` y `expedientes-de-inversion.md`. No están disponibles `PF01_portafolio_candidatos.csv`, `PF02_tco.csv` ni los resultados de los pasos A-D. Por eso no se inventan proyectos descartados, puntajes, cuadrantes, dependencias, fechas ni acuerdos con gerencia.

## PR07_no_se_hara.csv

Con la información recibida no se puede completar de forma responsable el registro de proyectos que no se ejecutarán: faltan el portafolio de candidatos priorizado y la matriz esfuerzo-impacto. La tabla final deberá incluir los proyectos del cuadrante ④ cuando se genere `PR03_priorizado.csv` y la Gerencia General acuerde aceptar cada riesgo.

No se debe registrar como descartado el proyecto para implementar el sistema de gestión de seguridad de la información (SGSI). La ficha identifica el incumplimiento de la Resolución SBS 504-2021 como un riesgo conocido y no tratado, y establece la implementación del sistema como objetivo de TI.

## Redacción para el PETI

### 7.2.5 Proyectos que no se ejecutarán y riesgo asumido

> A la fecha de esta revisión no se declara ningún proyecto como definitivamente descartado, porque no se cuenta con el portafolio de candidatos puntuado ni con la matriz esfuerzo-impacto aprobada. La decisión se completará después de identificar los proyectos del cuadrante ④ y documentar, para cada uno, el objetivo que quedaría sin cumplir, el riesgo aceptado, el responsable y la fecha de revisión. La Gerencia General deberá aceptar expresamente cada riesgo. No se recomienda postergar la implementación del SGSI requerido por la Resolución SBS 504-2021; la organización reconoce que el incumplimiento sigue sin tratarse.

### 7.3 Hoja de ruta

- **7.3.1 Restricciones:** el equipo de TI tiene cinco personas; por tanto, la capacidad simultánea debe comprobarse antes de fijar las olas. También deben considerarse la resistencia que impidió activar el segundo factor, la falta de política de seguridad y de continuidad probada, y el incidente de acceso indebido a expedientes de socios. La ficha no proporciona dependencias técnicas ni plazos normativos detallados; deben confirmarse con los responsables y el regulador.
- **7.3.2 Olas, 7.3.3 cronograma y 7.3.4 verificación:** pendientes de los resultados de priorización, dependencias, duración y capacidad trimestral. No se puede certificar todavía que existan tres olas ni que se respeten precedencias.

### 7.4 Presupuesto

- **7.4.1 Estructura presupuestal:** el presupuesto 2025 registra S/ 1 140 800,00 como operación y S/ 99 200,00 como inversión planificada. La inversión es solo una aproximación a CAPEX y requiere confirmación contable. Las partidas no separan gestión del cambio ni contingencia.
- **7.4.2 Presupuesto por año:** el único límite documentado es el presupuesto de TI de 2025, S/ 1 240 000,00. No se entregaron límites aprobados para años futuros ni el presupuesto plurianual por proyecto.
- **7.4.3 Curva de OPEX acumulado:** no se puede calcular sin el OPEX proyectado por proyecto y año. La curva debe elaborarse cuando se complete `PR06_presupuesto.csv`.
- **7.4.4 Supuestos e incertidumbre:** las inversiones cerradas muestran desviaciones de -5,0 % (videovigilancia), +46,6 % (servidores) y +31,7 % (respaldo); los beneficios de las tres no se midieron. Son antecedentes de variabilidad y debilidad de control, no un rango estadístico suficiente para pronosticar el nuevo portafolio. Cada estimación debe incluir cotizaciones, supuestos y contingencia justificada.

## Pendiente antes de entregar

Completar `PR07_no_se_hara.csv` con los datos del portafolio, obtener la aceptación de riesgos de Gerencia General y añadir la hoja de ruta y el presupuesto plurianual calculados. Sin esos insumos, este paso queda como desarrollo parcial y no como resultado final validado.