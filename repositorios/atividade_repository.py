"""Repositório de atividades — leitura e gravação em atividades.csv."""

import os

from modelos.atividade import Atividade
from repositorios.base_repository import (
    garantir_arquivo, ler_todos, adicionar_linha, proximo_id,
)

CABECALHO = ["id_atividade", "tipo_atividade", "data", "hora",
             "animal", "tratador", "descricao"]

ARQUIVO_PADRAO = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                              "dados", "atividades.csv")


class AtividadeRepository:
    """Persistência de atividades em CSV."""

    def __init__(self, caminho=ARQUIVO_PADRAO):
        self.caminho = caminho
        garantir_arquivo(self.caminho, CABECALHO)

    def listar(self):
        linhas = ler_todos(self.caminho, CABECALHO)
        atividades = []
        for linha in linhas:
            try:
                atividades.append(Atividade.from_dict(linha))
            except (KeyError, ValueError, TypeError) as e:
                print(f"Aviso: linha ignorada em atividades.csv: {linha} ({e})")
        return atividades

    def salvar(self, atividade):
        adicionar_linha(self.caminho, CABECALHO, atividade.to_dict())

    def proximo_id(self):
        return proximo_id(ler_todos(self.caminho, CABECALHO), "id_atividade")
