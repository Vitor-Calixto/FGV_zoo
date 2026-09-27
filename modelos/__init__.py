"""Pacote de modelos do domínio do zoológico."""

from modelos.animal import Animal
from modelos.mamifero import Mamifero
from modelos.ave import Ave
from modelos.reptil import Reptil
from modelos.tratador import Tratador
from modelos.recinto import Recinto
from modelos.atividade import Atividade
from modelos.administrador import Administrador

__all__ = ["Animal", "Mamifero", "Ave", "Reptil",
           "Tratador", "Recinto", "Atividade", "Administrador"]
