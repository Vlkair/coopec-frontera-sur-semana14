from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
PESOS = dict(contribucion=25, beneficio=10, urgencia=15, habilitacion=10,
             riesgo=15, facilidad=10, aceptacion=5, impacto_social_ambiental=10)
if sum(PESOS.values()) != 100 or PESOS["impacto_social_ambiental"] < 10:
    raise ValueError("Revisar la suma de pesos y el mínimo del criterio social y ambiental.")
notas = pd.DataFrame([
    ("PR-01", 3, 4, 2, 3, 2, 2, 3, 5),
    ("PR-02", 4, 3, 2, 5, 4, 1, 2, 4),
    ("PR-03", 2, 1, 1, 1, 2, 3, 4, 3),
    ("PR-04", 5, 2, 5, 4, 5, 4, 4, 4),
    ("PR-05", 3, 4, 2, 2, 3, 3, 3, 3),
    ("PR-06", 3, 4, 3, 2, 3, 5, 4, 1),
], columns=["codigo", *PESOS])
cartera = pd.read_csv(ROOT / "PR01_portafolio_marcado.csv")
costos = pd.read_csv(ROOT / "PF02_tco.csv")
r = cartera.loc[~cartera.no_negociable, ["codigo", "nombre"]]
r = r.merge(notas, on="codigo", how="left", validate="one_to_one")
r = r.merge(costos[["codigo", "inv_inicial"]], on="codigo", how="left", validate="one_to_one")
if not r[list(PESOS)].apply(lambda col: col.between(1, 5)).all().all() or r.inv_inicial.isna().any():
    raise ValueError("Faltan notas válidas o importes en el portafolio.")
r["puntaje"] = (r[list(PESOS)].mul(pd.Series(PESOS)).sum(axis=1) / 100).round(2)
r["impacto"] = (r.contribucion * .5 + r.beneficio * .3 + r.riesgo * .2).round(2)
r["esfuerzo"] = 6 - r.facilidad
r["cuadrante"] = r.apply(
    lambda p: {(True, False): 1, (True, True): 2, (False, False): 3, (False, True): 4}
    [p.impacto >= 3.5, p.esfuerzo >= 3.5], axis=1)
r = r.sort_values("puntaje", ascending=False)
r.to_csv(ROOT / "PR03_priorizado.csv", index=False)
print(r[["codigo", "puntaje", "impacto", "esfuerzo", "cuadrante"]].to_string(index=False))
for cuadrante in range(1, 5):
    print(f"Cuadrante {cuadrante}: " + ", ".join(r.loc[r.cuadrante.eq(cuadrante), "codigo"]))
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(r.esfuerzo, r.impacto, color="#156776", s=55)
for p in r.itertuples():
    ax.annotate(p.codigo, (p.esfuerzo, p.impacto), xytext=(7, 4), textcoords="offset points")
ax.axhline(3.5, color="gray", linestyle="--")
ax.axvline(3.5, color="gray", linestyle="--")
ax.set(xlim=(.7, 5.5), ylim=(.8, 5.2), xlabel="Esfuerzo", ylabel="Impacto",
       title="COOPAC Frontera Sur | Matriz esfuerzo-impacto provisional")
fig.tight_layout()
fig.savefig(ROOT / "graficos" / "PR_esfuerzo_impacto.png", dpi=160)
