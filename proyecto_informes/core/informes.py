from pathlib import Path
import pandas as pd

def detectar_tipo_archivo(ruta: str | Path) -> str:
    """
    Detecta si un archivo es CSV o Excel según su extensión.
    """
    ruta = Path(ruta)

    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    ext = ruta.suffix.lower()

    if ext == ".csv":
        return "csv"
    if ext in (".xls", ".xlsx"):
        return "excel"

    raise ValueError(f"Extensión no soportada: {ext}")


def leer_archivo(ruta: str | Path) -> pd.DataFrame:
    """
    Función genérica que detecta el tipo de archivo y llama a la función adecuada.
    """
    ruta = Path(ruta)

    # Validación de existencia
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    tipo = detectar_tipo_archivo(ruta)

    if tipo == "csv":
        return pd.read_csv(ruta)

    if tipo == "excel":
        return pd.read_excel(ruta)

    # Esto solo se ejecutaría si detectar_tipo_archivo fallara
    raise ValueError(f"No se pudo determinar cómo leer el archivo: {ruta}")
