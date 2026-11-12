# 07_portafolio/PR04_hoja_ruta.py
import pandas as pd, networkx as nx, matplotlib.pyplot as plt

r  = pd.read_csv("PR03_priorizado.csv")
nn = pd.read_csv("PR01_portafolio_marcado.csv")
DEP = [("PR-04","PR-03"),("PR-04","PR-01"),("PR-05","PR-03"),("PR-06","PR-01"),
       ("PR-07","PR-01"),("PR-07","PR-03"),("PR-09","PR-03"),("PR-14","PR-08")]

CAPACIDAD_SIMULTANEA = 3      # equipo de 5 personas en TI
PRESUPUESTO_ANUAL    = 320000 # S/ acordado con la gerencia en la Entrevista 3

G = nx.DiGraph(); G.add_nodes_from(list(r.codigo) + list(nn[nn.no_negociable].codigo))
G.add_edges_from([(b,a) for a,b in DEP])
nivel = {n: 0 for n in G.nodes}
for n in nx.topological_sort(G):
    for s in G.successors(n):
        nivel[s] = max(nivel[s], nivel[n] + 1)

print("=== NIVELES DE DEPENDENCIA (0 = puede iniciar de inmediato) ===")
for lv in sorted(set(nivel.values())):
    print(f"  Nivel {lv}: {[n for n,v in nivel.items() if v == lv]}")

OLAS = {
 "Ola 1 — Fundacional (Año 1, S1–S2)": ["PR-13","PR-02","PR-11","PR-01","PR-14","PR-12"],
 "Ola 2 — Habilitación (Año 1 S2 – Año 2 S1)": ["PR-03","PR-08","PR-09","PR-10"],
 "Ola 3 — Explotación (Año 2 S2 – Año 3)":     ["PR-04","PR-05","PR-06","PR-07","PR-15"],
}
tco = pd.read_csv("PF02_tco.csv").set_index("codigo")

print("\n=== HOJA DE RUTA POR OLAS ===")
for ola, proys in OLAS.items():
    inv = tco.loc[[p for p in proys if p in tco.index], "inv_inicial"].sum()
    print(f"\n{ola}")
    print(f"  Proyectos: {', '.join(proys)}")
    print(f"  Inversión: S/ {inv:,.0f}")
    # Verificación de dependencias dentro de la ola
    for p in proys:
        pendientes = [d for d in G.predecessors(p)
                      if d not in proys and d not in
                      [x for k, v in OLAS.items() if list(OLAS).index(k) < list(OLAS).index(ola) for x in v]]
        if pendientes:
            print(f"  ⚠ {p} depende de {pendientes}, que no está en esta ola ni en las anteriores")

print(f"\n=== VERIFICACIÓN DE CAPACIDAD ===")
print(f"Capacidad simultánea declarada: {CAPACIDAD_SIMULTANEA} proyectos")
print("→ Distribuir cada ola en semestres de modo que nunca haya más de "
      f"{CAPACIDAD_SIMULTANEA} proyectos activos a la vez.")
print("→ Verificar además que no coincidan en un mismo trimestre dos proyectos")
print("  que afecten a la misma área usuaria (restricción de absorción del cambio, Sección 2.4).")
