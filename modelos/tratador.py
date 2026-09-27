"""Classe Tratador — funcionário responsável por cuidar dos animais."""


class Tratador:
    """Representa o tratador do zoológico."""

    def __init__(self, id_tratador, nome, turno, especialidade,
                 animais_responsaveis=""):
        self.id_tratador = int(id_tratador)
        self.nome = nome
        self.turno = turno
        self.especialidade = especialidade
        if isinstance(animais_responsaveis, list):
            self.animais_responsaveis = ";".join(animais_responsaveis)
        else:
            self.animais_responsaveis = (animais_responsaveis or "").strip()

    # ---------- Comportamentos ----------
    def alimentar_animal(self, animal):
        """Retorna mensagem de alimentação executada pelo tratador."""
        return f"Tratador {self.nome} alimentou o animal {animal.nome}."

    def tratar_animal(self, animal):
        """Retorna mensagem de tratamento executado pelo tratador."""
        return f"Tratador {self.nome} tratou o animal {animal.nome}."

    def limpar_recinto(self, recinto):
        """Retorna mensagem de limpeza executada pelo tratador."""
        return f"Tratador {self.nome} limpou o recinto {recinto.nome}."

    def registrar_atividade(self, atividade):
        """Retorna mensagem de registro de atividade."""
        return (f"Atividade '{atividade.tipo_atividade}' registrada por "
                f"{self.nome} para {atividade.animal}.")

    def exibir_dados(self):
        """Exibe os dados do tratador."""
        resp = self.animais_responsaveis or "-"
        return (f"[Tratador {self.id_tratador}] {self.nome} | Turno: {self.turno} | "
                f"Especialidade: {self.especialidade} | Responsável por: {resp}")

    # ---------- Persistência ----------
    def to_dict(self):
        return {
            "id_tratador": self.id_tratador,
            "nome": self.nome,
            "turno": self.turno,
            "especialidade": self.especialidade,
            "animais_responsaveis": self.animais_responsaveis,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            id_tratador=int(dados["id_tratador"]),
            nome=dados["nome"],
            turno=dados["turno"],
            especialidade=dados["especialidade"],
            animais_responsaveis=dados.get("animais_responsaveis", ""),
        )
