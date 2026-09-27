"""Repositório de recintos — leitura e gravação em recintos.csv."""

import os

from modelos.recinto import Recinto
from repositorios.base_repository import (
    garantir_arquivo, ler_todos, salvar_todos, adicionar_linha, proximo_id,
)

CABECALHO = ["id_recinto", "nome", "tipo", "capacidade",
             "localizacao", "status_limpeza"]

ARQUIVO_PADRAO = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                              "dados", "recintos.csv")


class RecintoRepository:
    """Persistência de recintos em CSV."""

    def __init__(self, caminho=ARQUIVO_PADRAO):
        self.caminho = caminho
        garantir_arquivo(self.caminho, CABECALHO)

    def listar(self):
        linhas = ler_todos(self.caminho, CABECALHO)
        recintos = []
        for linha in linhas:
            try:
                recintos.append(Recinto.from_dict(linha))
            except (KeyError, ValueError, TypeError) as e:
                print(f"Aviso: linha ignorada em recintos.csv: {linha} ({e})")
        return recintos

    def salvar(self, recinto):
        adicionar_linha(self.caminho, CABECALHO, recinto.to_dict())

    def atualizar(self, recinto_atualizado):
        """Atualiza um recinto existente (ex.: status de limpeza)."""
        linhas = ler_todos(self.caminho, CABECALHO)
        novas = []
        for linha in linhas:
            try:
                if int(linha.get("id_recinto", -1)) == recinto_atualizado.id_recinto:
                    novas.append(recinto_atualizado.to_dict())
                else:
                    novas.append(linha)
            except (ValueError, TypeError):
                novas.append(linha)
        salvar_todos(self.caminho, CABECALHO, novas)

    def buscar_por_id(self, id_recinto):
        try:
            alvo = int(id_recinto)
        except (ValueError, TypeError):
            return None
        for r in self.listar():
            if r.id_recinto == alvo:
                return r
        return None

    def buscar_por_nome(self, nome):
        alvo = (nome or "").strip().lower()
        for r in self.listar():
            if r.nome.strip().lower() == alvo:
                return r
        return None

    def proximo_id(self):
        return proximo_id(ler_todos(self.caminho, CABECALHO), "id_recinto")
