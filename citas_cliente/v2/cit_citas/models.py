"""
Cit Citas V2, modelos
"""
from collections import OrderedDict
from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class CitCita(Base, UniversalMixin):
    """CitCita"""

    ESTADOS = OrderedDict(
        [
            ("ASISTIO", "Asistió"),
            ("CANCELO", "Canceló"),
            ("PENDIENTE", "Pendiente"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "cit_citas"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    cit_cliente_id = Column(Integer, ForeignKey("cit_clientes.id"), index=True, nullable=False)
    cit_cliente = relationship("CitCliente", back_populates="cit_citas")
    cit_servicio_id = Column(Integer, ForeignKey("cit_servicios.id"), index=True, nullable=False)
    cit_servicio = relationship("CitServicio", back_populates="cit_citas")
    oficina_id = Column(Integer, ForeignKey("oficinas.id"), index=True, nullable=False)
    oficina = relationship("Oficina", back_populates="cit_citas")

    # Columnas
    inicio = Column(DateTime(), nullable=False)
    termino = Column(DateTime(), nullable=False)
    notas = Column(Text(), nullable=False, default="", server_default="")
    estado = Column(Enum(*ESTADOS, name="tipos_estados", native_enum=False))
    asistencia = Column(Boolean(), nullable=False, default=False, server_default="false")

    # Hijos
    # cit_citas_documentos = relationship("CitCitaDocumento", back_populates="cit_cita")

    @property
    def cit_servicio_descripcion(self):
        """Descripción del servicio"""
        return self.cit_servicio.descripcion

    @property
    def cit_cliente_nombre(self):
        """Nombre del cliente"""
        return self.cit_cliente.nombre

    @property
    def oficina_descripcion_corta(self):
        """Descripción corta de la oficina"""
        return self.oficina.descripcion_corta

    def __repr__(self):
        """Representación"""
        return f"<CitCita {self.id}>"
