"""
Cit Clientes V2, modelos
"""
from datetime import datetime
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class CitCliente(Base, UniversalMixin):
    """CitCliente"""

    # Nombre de la tabla
    __tablename__ = "cit_clientes"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombres = Column(String(256), nullable=False)
    apellido_primero = Column(String(256), nullable=False)
    apellido_segundo = Column(String(256), nullable=False, default="")
    curp = Column(String(18), unique=True, nullable=False)
    telefono = Column(String(64), nullable=False, default="")
    email = Column(String(256), unique=True, nullable=False)
    contrasena_md5 = Column(String(256), nullable=False, default="")
    contrasena_sha256 = Column(String(256), nullable=False, default="")
    renovacion = Column(Date(), nullable=False)
    # limite_citas_pendientes = Column(Integer(), nullable=False)

    # Hijos
    cit_clientes_recuperaciones = relationship("CitClienteRecuperacion", back_populates="cit_cliente")
    cit_citas = relationship("CitCita", back_populates="cit_cliente")
    cit_pagos = relationship("CitPago", back_populates="cit_cliente")

    @property
    def nombre(self):
        """Junta nombres, apellido primero y apellido segundo"""
        return self.nombres + " " + self.apellido_primero + " " + self.apellido_segundo

    @property
    def permissions(self):
        """Entrega un diccionario con todos los permisos si no ha llegado la fecha de renovación"""
        if self.renovacion < datetime.now().date():
            return {}
        # Los permisos son fijos para todos los clientes, donde 1 es solo lectura
        return {
            "AUTORIDADES": 1,
            "CIT CITAS": 3,
            "CIT DIAS DISPONIBLES": 1,
            "CIT HORAS DISPONIBLES": 1,
            "CIT OFICINAS SERVICIOS": 1,
            "CIT PAGOS": 3,
            "CIT SERVICIOS": 1,
            "CIT TRAMITES SERVICIOS": 1,
            "DISTRITOS": 1,
            "DOMICILIOS": 1,
            "MATERIAS": 1,
            "OFICINAS": 1,
        }

    def __repr__(self):
        """Representación"""
        return f"<CitCliente {self.email}>"
