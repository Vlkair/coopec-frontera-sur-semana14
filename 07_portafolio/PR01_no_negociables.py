from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
cartera = pd.read_csv(ROOT / "PF01_portafolio_candidatos.csv", keep_default_na=False)
plazos = pd.to_datetime(cartera.plazo_limite, format="%Y-%m-%d", errors="raise")
cartera["no_negociable"] = plazos.notna() & cartera.norma_referencial.ne("")
cartera["estado_plazo"] = "Sin obligación identificada en los insumos"
cartera.loc[cartera.norma_referencial.ne(""), "estado_plazo"] = "Alcance y plazo pendientes de validar"
cartera.loc[cartera.no_negociable, "estado_plazo"] = "Plazo consignado"
cartera.to_csv(ROOT / "PR01_portafolio_marcado.csv", index=False)
print(cartera[["codigo", "no_negociable", "norma_referencial", "estado_plazo"]].to_string(index=False))
print("No negociables con plazo documentado:", int(cartera.no_negociable.sum()))
