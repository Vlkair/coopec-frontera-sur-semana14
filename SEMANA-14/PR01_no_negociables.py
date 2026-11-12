# 07_portafolio/PR01_no_negociables.py
import pandas as pd

p = pd.read_csv("PF01_portafolio_candidatos.csv")

NO_NEGOCIABLES = {          # proyecto: (norma, plazo límite, fundamento)
 "PR-02": ("D. S. 016-2024-JUS", "<fecha límite normativa>", "Registro de actividades de tratamiento: obligación vigente"),
 "PR-11": ("Ley 29733 art. 9",   "<fecha límite normativa>", "Medidas de seguridad sobre datos personales"),
 "PR-09": ("Fin de soporte del fabricante", "<fecha límite del fabricante>", "Sin soporte no hay parches de seguridad"),
}
p["no_negociable"] = p.codigo.isin(NO_NEGOCIABLES)
p["plazo_limite"]  = p.codigo.map(lambda c: NO_NEGOCIABLES.get(c, (None,None,None))[1])
p["fundamento_nn"] = p.codigo.map(lambda c: NO_NEGOCIABLES.get(c, (None,None,None))[2])

print("=== PROYECTOS NO NEGOCIABLES ===")
print(p[p.no_negociable][["codigo","nombre","plazo_limite","fundamento_nn"]].to_string(index=False))
print("\n→ NO entran al modelo de priorización. Se ubican en la hoja de ruta por su plazo,")
print("  con al menos un trimestre de margen antes de la fecha límite.")
print(f"\nProyectos que sí compiten en el modelo: {(~p.no_negociable).sum()}")
p.to_csv("PR01_portafolio_marcado.csv", index=False)
