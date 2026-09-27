"""Classe Recinto — local onde os animais ficam."""


class Recinto:
    """Representa um recinto do zoológico."""

    def __init__(self, id_recinto, nome, tipo, capacidade,
                 localizacao, status_limpeza="Limpo"):
        self.id_recinto = int(id_recinto)
        self.nome = nome
        self.tipo = tipo
        self.capacidade = int(capacidade)
        self.localizacao = localizacao
        self.status_limpeza = status_limpeza

    # ---------- Comportamentos ----------
    def limpar(self):
        """Marca o recinto como limpo."""
        self.status_limpeza = "Limpo"
        return f"Recinto {self.nome} foi limpo."

    def verificar_disponibilidade(self, quantidade_animais=0):
        """Verifica se há vaga para mais animais."""
        return int(quantidade_animais) < int(self.capacidade)

    def exibir_dados(self):
        return (f"[Recinto {self.id_recinto}] {self.nome} | Tipo: {self.tipo} | "
                f"Capacidade: {self.capacidade} | Local: {self.localizacao} | "
                f"Limpeza: {self.status_limpeza}")

    # ---------- Persistência ----------
    def to_dict(self):
        return {
            "id_recinto": self.id_recinto,
            "nome": self.nome,
            "tipo": self.tipo,
            "capacidade": self.capacidade,
            "localizacao": self.localizacao,
            "status_limpeza": self.status_limpeza,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            id_recinto=int(dados["id_recinto"]),
            nome=dados["nome"],
            tipo=dados["tipo"],
            capacidade=int(dados["capacidade"]),
            localizacao=dados["localizacao"],
            status_limpeza=dados.get("status_limpeza", "Limpo"),
        )
