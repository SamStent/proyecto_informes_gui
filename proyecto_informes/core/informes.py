import pandas as pd
from pathlib import Path

# ----------------------------
# LECTURA DE ARCHIVOS
# ----------------------------

def leer_csv(ruta: str | Path, sep: str = ",") -> pd.DataFrame:
    """Lee un archivo CSV y devuelve un DataFrame."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo CSV: {ruta}")
    return pd.read_csv(ruta, sep=sep)


def leer_excel(ruta: str | Path, hoja: str | int | None = None) -> pd.DataFrame:
    """Lee un archivo Excel y devuelve un DataFrame."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo Excel: {ruta}")
    return pd.read_excel(ruta, sheet_name=hoja)



# -----------------------------
# EXPORTACIÓN DE ARCHIVOS
# -----------------------------

def export_csv(df: pd.DataFrame, ruta: str | Path, sep: str = ","):
    """Exporta un DataFrame a CSV."""
    ruta = Path(ruta)
    df.to_csv(ruta, sep=sep, index=False)


def export_excel(df: pd.DataFrame, ruta: str | Path, hoja: str = "Hoja1"):
    """Exporta un DataFrame a Excel."""
    ruta = Path(ruta)
    df.to_excel(ruta, sheet_name=hoja, index=False)
