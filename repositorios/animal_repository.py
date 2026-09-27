"""Repositório de animais — leitura e gravação em animais.csv."""

import os

from modelos.animal import Animal
from repositorios.base_repository import (
    garantir_arquivo, ler_todos, salvar_todos, adicionar_linha, proximo_id,
)

CABECALHO = ["id_animal", "nome", "especie", "idade", "tipo_alimentacao",
             "recinto", "status_saude", "tipo", "extra"]

ARQUIVO_PADRAO = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                              "dados", "animais.csv")


class AnimalRepository:
    """Persistência de animais em CSV."""

    def __init__(self, caminho=ARQUIVO_PADRAO):
        self.caminho = caminho
        garantir_arquivo(self.caminho, CABECALHO)

    def listar(self):
        """Retorna lista de objetos Animal/Mamifero/Ave/Reptil."""
        linhas = ler_todos(self.caminho, CABECALHO)
        animais = []
        for linha in linhas:
            try:
                animais.append(Animal.from_dict(linha))
            except (KeyError, ValueError, TypeError) as e:
                print(f"Aviso: linha ignorada em animais.csv: {linha} ({e})")
        return animais

    def salvar(self, animal):
        """Adiciona um animal ao CSV."""
        adicionar_linha(self.caminho, CABECALHO, animal.to_dict())

    def buscar_por_id(self, id_animal):
        try:
            alvo = int(id_animal)
        except (ValueError, TypeError):
            return None
        for animal in self.listar():
            if animal.id_animal == alvo:
                return animal
        return None

    def buscar_por_nome(self, nome):
        alvo = (nome or "").strip().lower()
        for animal in self.listar():
            if animal.nome.strip().lower() == alvo:
                return animal
        return None

    def proximo_id(self):
        return proximo_id(ler_todos(self.caminho, CABECALHO), "id_animal")
