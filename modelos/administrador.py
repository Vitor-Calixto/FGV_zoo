"""Classe Administrador — consulta dados e relatórios."""

from collections import Counter


class Administrador:
    """Representa o administrador que acompanha as atividades."""

    def __init__(self, id_administrador=1, nome="Administrador"):
        self.id_administrador = int(id_administrador)
        self.nome = nome

    def gerar_relatorio_atividades(self, atividades):
        """Gera relatório geral: total + agrupamentos por tipo, animal e tratador."""
        total = len(atividades)
        por_tipo = dict(Counter(a.tipo_atividade for a in atividades))
        por_animal = dict(Counter(a.animal for a in atividades))
        por_tratador = dict(Counter(a.tratador for a in atividades))
        return {
            "total": total,
            "por_tipo": por_tipo,
            "por_animal": por_animal,
            "por_tratador": por_tratador,
        }

    def consultar_atividades_por_tratador(self, atividades, nome_tratador):
        """Filtra atividades de um tratador específico (busca parcial)."""
        alvo = (nome_tratador or "").strip().lower()
        return [a for a in atividades if alvo in (a.tratador or "").lower()]

    def consultar_total_atividades(self, atividades):
        """Retorna apenas o total de atividades."""
        return len(atividades)

    def exibir_dados(self):
        return f"[Administrador {self.id_administrador}] {self.nome}"
