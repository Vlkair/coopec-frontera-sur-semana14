from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
costos = pd.read_csv(ROOT / "PF02_tco.csv")
ruta = pd.read_csv(ROOT / "PR05_hoja_ruta.csv").dropna(subset=["codigo"])
proyectos = ruta.merge(costos, on="codigo", validate="one_to_one", how="left")
if proyectos[["inv_inicial", "opex_min", "opex_max"]].isna().any().any():
    raise ValueError("Faltan datos de costo de un proyecto programado.")
historico = pd.read_csv(ROOT / "presupuesto_ti.csv")
referencia = historico.loc[historico.tipo.eq("Inversión"), "planificado"].sum()
filas = []
for anio in (1, 2, 3):
    capex = proyectos.loc[proyectos.anio.eq(anio), "inv_inicial"].sum()
    cambio = capex * .10
    contingencia = (capex + cambio) * .15
    entregados = proyectos.loc[proyectos.anio.le(anio)]
    minimo = entregados.opex_min.sum()
    maximo = entregados.opex_max.sum()
    implantacion = capex + cambio + contingencia
    filas.append(dict(anio=anio, capex=capex, cambio=cambio, contingencia=contingencia,
                      opex_min=minimo, opex_max=maximo, total_min=implantacion + minimo,
                      total_max=implantacion + maximo, referencia_inversion=referencia,
                      margen_escenario=referencia - implantacion - maximo))
p = pd.DataFrame(filas)
p["opex_acumulado_min"] = p.opex_min.cumsum()
p["opex_acumulado_max"] = p.opex_max.cumsum()
p.round(2).to_csv(ROOT / "PR06_presupuesto.csv", index=False)
print(p.round(2).to_string(index=False))
if p.margen_escenario.lt(0).any():
    raise ValueError("El escenario supera la referencia histórica anual.")
print("Tres años dentro de la referencia histórica; presupuesto futuro pendiente de aprobación.")
fig, (presupuesto, opex) = plt.subplots(1, 2, figsize=(10, 4))
presupuesto.bar(p.anio, p.total_max, color="#156776", label="Máximo anual estimado")
presupuesto.axhline(referencia, color="#ae5d16", linestyle="--", label="Referencia histórica")
presupuesto.legend(fontsize=8)
opex.fill_between(p.anio, p.opex_acumulado_min, p.opex_acumulado_max, color="#9bc9cd")
opex.plot(p.anio, p.opex_acumulado_max, "o-", color="#156776")
presupuesto.set_title("Gasto incremental anual")
opex.set_title("Rango de OPEX acumulado")
for ax in (presupuesto, opex):
    ax.set(xlabel="Año", ylabel="S/", xticks=[1, 2, 3])
fig.tight_layout()
fig.savefig(ROOT / "graficos" / "PR_presupuesto.png", dpi=160)
