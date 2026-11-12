# 07_portafolio/PR06_presupuesto.py
import pandas as pd, matplotlib.pyplot as plt

tco = pd.read_csv("PF02_tco.csv").set_index("codigo")
hr  = pd.read_csv("PR05_hoja_ruta.csv")

CAMBIO_PCT, CONTINGENCIA_PCT = .10, .12    # gestión del cambio y contingencia
AÑOS = ["Año 1", "Año 2", "Año 3"]

filas = []
for a in AÑOS:
    proys = hr[hr["Año"] == a]["Proyecto"].tolist()
    capex = tco.loc[[p for p in proys if p in tco.index], "costo_unico"].sum()
    # OPEX: acumula el de todos los proyectos ya entregados en años anteriores o en este
    entregados = hr[hr["Año"] <= a]["Proyecto"].tolist()
    opex = tco.loc[[p for p in entregados if p in tco.index], "costo_anual"].sum()
    cambio = capex * CAMBIO_PCT
    subtotal = capex + opex + cambio
    filas.append({"año": a, "proyectos": len(proys), "capex": capex, "opex_acumulado": opex,
                  "gestion_cambio": cambio, "subtotal": subtotal,
                  "contingencia": subtotal * CONTINGENCIA_PCT,
                  "total": subtotal * (1 + CONTINGENCIA_PCT)})

pr = pd.DataFrame(filas)
pr.to_csv("PR06_presupuesto.csv", index=False)
print(pr.round(0).to_string(index=False))
print(f"\nTOTAL DEL PLAN (3 años): S/ {pr.total.sum():,.0f}")
print(f"  CAPEX: S/ {pr.capex.sum():,.0f}  ({pr.capex.sum()/pr.total.sum():.0%})")
print(f"  OPEX : S/ {pr.opex_acumulado.sum():,.0f}  ({pr.opex_acumulado.sum()/pr.total.sum():.0%})")
print(f"\nOPEX del año 1: S/ {pr.opex_acumulado.iloc[0]:,.0f}")
print(f"OPEX del año 3: S/ {pr.opex_acumulado.iloc[-1]:,.0f}  "
      f"(×{pr.opex_acumulado.iloc[-1]/max(pr.opex_acumulado.iloc[0],1):.1f})")
print("\n→ El OPEX NO BAJA: cada proyecto entregado lo incrementa de forma permanente.")
print("  Este es el compromiso real que la gerencia asume al aprobar el plan.")

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(pr.año, pr.capex, label="Inversión (CAPEX)", color="#16285C")
ax.bar(pr.año, pr.opex_acumulado, bottom=pr.capex, label="Gasto operativo acumulado (OPEX)", color="#0EA5E9")
ax.bar(pr.año, pr.gestion_cambio, bottom=pr.capex+pr.opex_acumulado,
       label="Gestión del cambio", color="#F59E0B")
ax.bar(pr.año, pr.contingencia, bottom=pr.capex+pr.opex_acumulado+pr.gestion_cambio,
       label="Contingencia", color="#94A3B8")
ax2 = ax.twinx()
ax2.plot(pr.año, pr.opex_acumulado, "o--", color="#B91C1C", lw=2.5, label="Curva de OPEX")
ax2.set_ylabel("OPEX acumulado (S/)", color="#B91C1C")
ax.set_xlabel("Año"); ax.set_ylabel("S/"); ax.set_xticks(pr.año)
ax.set_title("Presupuesto plurianual del PETI y crecimiento del gasto operativo")
ax.legend(loc="upper left"); plt.tight_layout()
plt.savefig("../graficos/PR_presupuesto.png", dpi=140)
