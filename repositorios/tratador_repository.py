"""Repositório de tratadores — leitura e gravação em tratadores.csv."""

import os

from modelos.tratador import Tratador
from repositorios.base_repository import (
    garantir_arquivo, ler_todos, adicionar_linha, proximo_id,
)

CABECALHO = ["id_tratador", "nome", "turno", "especialidade", "animais_responsaveis"]

ARQUIVO_PADRAO = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                              "dados", "tratadores.csv")


class TratadorRepository:
    """Persistência de tratadores em CSV."""

    def __init__(self, caminho=ARQUIVO_PADRAO):
        self.caminho = caminho
        garantir_arquivo(self.caminho, CABECALHO)

    def listar(self):
        linhas = ler_todos(self.caminho, CABECALHO)
        tratadores = []
        for linha in linhas:
            try:
                tratadores.append(Tratador.from_dict(linha))
            except (KeyError, ValueError, TypeError) as e:
                print(f"Aviso: linha ignorada em tratadores.csv: {linha} ({e})")
        return tratadores

    def salvar(self, tratador):
        adicionar_linha(self.caminho, CABECALHO, tratador.to_dict())

    def buscar_por_id(self, id_tratador):
        try:
            alvo = int(id_tratador)
        except (ValueError, TypeError):
            return None
        for t in self.listar():
            if t.id_tratador == alvo:
                return t
        return None

    def buscar_por_nome(self, nome):
        alvo = (nome or "").strip().lower()
        for t in self.listar():
            if t.nome.strip().lower() == alvo:
                return t
        return None

    def proximo_id(self):
        return proximo_id(ler_todos(self.caminho, CABECALHO), "id_tratador")
