"""
Oficinas V2, esquemas de pydantic
"""
from pydantic import BaseModel


class OficinaOut(BaseModel):
    """Esquema para entregar oficinas"""

    id: int
    distrito_id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    domicilio_id: int
    domicilio_completo: str
    clave: str
    descripcion: str
    descripcion_corta: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
