from pathlib import Path
import networkx as nx
import pandas as pd

ROOT = Path(__file__).resolve().parent
cartera = pd.read_csv(ROOT / "PR01_portafolio_marcado.csv")
ruta = pd.read_csv(ROOT / "PR05_hoja_ruta.csv", keep_default_na=False)
proyectos = ruta.loc[ruta.codigo.ne("")].set_index("codigo")
if not proyectos.index.is_unique:
    raise ValueError("Hay proyectos repetidos en la hoja de ruta.")
grafo = nx.DiGraph()
grafo.add_nodes_from(cartera.codigo)
for p in proyectos.itertuples():
    if p.Index not in grafo or not 1 <= p.mes_inicio <= p.mes_fin <= 12:
        raise ValueError(f"Proyecto o intervalo inválido: {p.Index}")
    if p.anio not in (1, 2, 3) or p.semestre != (p.mes_inicio - 1) // 6 + 1:
        raise ValueError(f"Año o semestre inválido: {p.Index}")
    for previo in filter(None, p.depende_de.split("|")):
        if previo not in proyectos.index:
            raise ValueError(f"Dependencia sin programar: {previo}")
        grafo.add_edge(previo, p.Index)
inicio = (proyectos.anio - 1) * 12 + proyectos.mes_inicio
fin = (proyectos.anio - 1) * 12 + proyectos.mes_fin
for previo, siguiente in grafo.edges:
    if fin[previo] >= inicio[siguiente]:
        raise ValueError(f"Precedencia fin-inicio rota: {previo} → {siguiente}")
for nivel, grupo in enumerate(nx.topological_generations(grafo)):
    print(f"Nivel {nivel}: {', '.join(grupo)}")
for trimestre in range(12):
    primer_mes = trimestre * 3 + 1
    activos = proyectos.loc[(inicio <= primer_mes + 2) & (fin >= primer_mes)]
    if len(activos) > 1 or activos.area.duplicated().any():
        raise ValueError(f"Capacidad o absorción excedida en trimestre {trimestre + 1}")
    print(f"Año {trimestre // 4 + 1}, trimestre {trimestre % 4 + 1}: {len(activos)} proyecto(s)")
print("Dependencias registradas y rotas:", grafo.number_of_edges(), "y 0")
print("Las dependencias técnicas y fechas normativas quedan pendientes de confirmación.")
print(ruta[["ola", "anio", "semestre", "hito"]].to_string(index=False))
