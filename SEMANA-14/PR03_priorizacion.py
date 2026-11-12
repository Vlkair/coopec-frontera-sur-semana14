# 07_portafolio/PR03_priorizacion.py
import pandas as pd, matplotlib.pyplot as plt

PESOS = {"contribucion":.25, "beneficio":.20, "urgencia":.15, "habilitacion":.15,
         "riesgo_no_hacer":.10, "facilidad":.10, "aceptacion":.05}
assert abs(sum(PESOS.values()) - 1) < 1e-9

CALIF = pd.DataFrame([
 # codigo, contribucion, beneficio, urgencia, habilitacion, riesgo_no_hacer, facilidad, aceptacion
 ("PR-01", 5, 3, 3, 5, 4, 3, 3),   # gobierno del dato — habilitador
 ("PR-03", 4, 3, 3, 5, 4, 2, 3),   # capa de integración — habilitador
 ("PR-04", 5, 5, 4, 2, 4, 2, 4),   # canal digital
 ("PR-05", 4, 4, 3, 1, 3, 4, 4),   # consulta de estado
 ("PR-06", 4, 5, 3, 1, 4, 3, 3),   # ruteo
 ("PR-07", 4, 4, 2, 1, 3, 3, 3),   # tablero de gestión
 ("PR-08", 3, 3, 3, 2, 4, 4, 4),   # mesa de servicio
 ("PR-10", 3, 2, 3, 1, 3, 5, 3),   # gestión del conocimiento
 ("PR-12", 3, 2, 2, 1, 3, 4, 3),   # continuidad de infraestructura
 ("PR-13", 5, 2, 4, 3, 5, 5, 5),   # comité de gobierno de TI
 ("PR-14", 3, 2, 3, 2, 4, 4, 4),   # instrumentación de monitoreo
 ("PR-15", 3, 3, 2, 1, 2, 4, 5),   # autoservicio de trabajadores
], columns=["codigo"] + list(PESOS))

CALIF["puntaje"] = sum(CALIF[c]*w for c, w in PESOS.items()).round(3)
CALIF = CALIF.sort_values("puntaje", ascending=False)

tco = pd.read_csv("PF02_tco.csv")[["codigo","tco_5","inv_inicial","meses"]]
r = CALIF.merge(tco, on="codigo", how="left")
r.to_csv("PR03_priorizado.csv", index=False)

print("=== PORTAFOLIO PRIORIZADO (sin los no negociables) ===")
print(r[["codigo","puntaje","contribucion","habilitacion","facilidad","tco_5"]].to_string(index=False))

# --- Matriz esfuerzo-impacto ---
r["impacto"]  = (r.contribucion*.5 + r.beneficio*.3 + r.riesgo_no_hacer*.2).round(2)
r["esfuerzo"] = (6 - r.facilidad).round(2)
r["cuadrante"] = [
  "① Ganancia rápida" if i >= 3.5 and e < 3.5 else
  "② Apuesta mayor"   if i >= 3.5 and e >= 3.5 else
  "③ Relleno"         if i < 3.5 and e < 3.5 else
  "④ Sumidero"
  for i, e in zip(r.impacto, r.esfuerzo)]

print("\n=== MATRIZ ESFUERZO-IMPACTO ===")
for c in ["① Ganancia rápida","② Apuesta mayor","③ Relleno","④ Sumidero"]:
    sub = r[r.cuadrante == c]
    print(f"\n{c}: {list(sub.codigo)}")
print("\n→ El cuadrante ④ contiene los candidatos a NO EJECUTAR. Deben declararse")
print("  explícitamente en el plan, con el riesgo que la organización asume.")

fig, ax = plt.subplots(figsize=(10,8))
COL = {"① Ganancia rápida":"#16A34A","② Apuesta mayor":"#0EA5E9",
       "③ Relleno":"#94A3B8","④ Sumidero":"#B91C1C"}
for c, g in r.groupby("cuadrante"):
    ax.scatter(g.esfuerzo, g.impacto, s=g.tco_5/900, c=COL[c], label=c,
               edgecolors="black", alpha=.8)
    for _, x in g.iterrows():
        ax.annotate(x.codigo, (x.esfuerzo, x.impacto), fontsize=8, ha="center", va="center")
ax.axhline(3.5, color="#64748B", ls="--", lw=1); ax.axvline(3.5, color="#64748B", ls="--", lw=1)
ax.set_xlabel("Esfuerzo →"); ax.set_ylabel("Impacto →")
ax.set_title("Matriz esfuerzo-impacto del portafolio\n(el tamaño representa el TCO a 5 años)")
ax.legend(loc="lower left", fontsize=8); ax.grid(alpha=.25)
plt.tight_layout(); plt.savefig("../graficos/PR_esfuerzo_impacto.png", dpi=140)
