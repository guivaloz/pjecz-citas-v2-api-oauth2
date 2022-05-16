"""
Cit Clientes Recuperaciones v1, CRUD (create, read, update, and delete)
"""
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from lib.pwgen import generar_aleatorio

from .models import CitClienteRecuperacion
from .schemas import CitClienteRecuperacionIn
from ..cit_clientes.crud import get_cit_cliente_from_email

EXPIRACION_HORAS = 48


def post_cit_cliente_recuperacion(db: Session, recuperacion: CitClienteRecuperacionIn) -> CitClienteRecuperacion:
    """Recibir los datos para la recuperacion de la contrasena de un cliente"""

    # Consultar Cliente (tambien valida el correo electronico)
    cit_cliente = get_cit_cliente_from_email(db, recuperacion.email)

    # Consultar si existe una recuperacion para ese cliente
    posible_cit_cliente_recuperacion = db.query(CitClienteRecuperacion).filter_by(cit_cliente_id=cit_cliente.id).first()
    if posible_cit_cliente_recuperacion is not None:
        raise ValueError("Ya existe una recuperacion para ese email.")

    # Insertar recuperacion
    cit_cliente_recuperacion = CitClienteRecuperacion(
        cit_cliente=cit_cliente,
        expiracion=datetime.now() + timedelta(hours=EXPIRACION_HORAS),
        cadena_validar=generar_aleatorio(largo=24),
        ya_recuperado=False,
    )
    db.add(cit_cliente_recuperacion)
    db.commit()
    db.refresh(cit_cliente_recuperacion)
    return cit_cliente_recuperacion