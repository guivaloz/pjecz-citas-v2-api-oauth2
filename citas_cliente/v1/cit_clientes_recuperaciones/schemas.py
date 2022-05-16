"""
Cit Clientes Recuperaciones v1, esquemas de pydantic
"""
from datetime import datetime
from pydantic import BaseModel


class CitClienteRecuperacionIn(BaseModel):
    """Esquema para entregar recuperacion de contraseña"""

    email: str


class CitClienteRecuperacionOut(CitClienteRecuperacionIn):
    """Esquema para entregar recuperacion de contraseña"""

    expiracion: datetime