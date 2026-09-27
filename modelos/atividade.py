"""Classe Atividade — ação realizada no zoológico."""


class Atividade:
    """Representa uma atividade (alimentação, tratamento, limpeza, banho de sol)."""

    def __init__(self, id_atividade, tipo_atividade, data, hora,
                 animal, tratador, descricao=""):
        self.id_atividade = int(id_atividade)
        self.tipo_atividade = tipo_atividade
        self.data = data
        self.hora = hora
        self.animal = animal
        self.tratador = tratador
        self.descricao = descricao or ""

    def registrar(self):
        """Mensagem de confirmação do registro."""
        return (f"Atividade {self.id_atividade} ({self.tipo_atividade}) registrada: "
                f"{self.animal} por {self.tratador} em {self.data} {self.hora}.")

    def exibir_dados(self):
        return (f"[{self.id_atividade}] {self.tipo_atividade} | Data: {self.data} "
                f"{self.hora} | Animal: {self.animal} | Tratador: {self.tratador} | "
                f"Descrição: {self.descricao}")

    def to_dict(self):
        return {
            "id_atividade": self.id_atividade,
            "tipo_atividade": self.tipo_atividade,
            "data": self.data,
            "hora": self.hora,
            "animal": self.animal,
            "tratador": self.tratador,
            "descricao": self.descricao,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            id_atividade=int(dados["id_atividade"]),
            tipo_atividade=dados["tipo_atividade"],
            data=dados["data"],
            hora=dados["hora"],
            animal=dados["animal"],
            tratador=dados["tratador"],
            descricao=dados.get("descricao", ""),
        )
