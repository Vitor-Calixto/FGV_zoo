"""Pacote de repositórios (persistência em CSV)."""

from repositorios.animal_repository import AnimalRepository
from repositorios.tratador_repository import TratadorRepository
from repositorios.recinto_repository import RecintoRepository
from repositorios.atividade_repository import AtividadeRepository

__all__ = ["AnimalRepository", "TratadorRepository",
           "RecintoRepository", "AtividadeRepository"]
