"""Classe base Animal — representa um animal genérico do zoológico."""


class Animal:
    """Representa um animal genérico do zoológico."""

    def __init__(self, id_animal, nome, especie, idade,
                 tipo_alimentacao, recinto, status_saude):
        self.id_animal = int(id_animal)
        self.nome = nome
        self.especie = especie
        self.idade = int(idade)
        self.tipo_alimentacao = tipo_alimentacao
        self.recinto = recinto
        self.status_saude = status_saude

    # ---------- Comportamentos ----------
    def alimentar(self):
        """Retorna mensagem padrão de alimentação (polimórfico)."""
        return (f"{self.nome} ({self.especie}) foi alimentado "
                f"com dieta {self.tipo_alimentacao}.")

    def tratar(self):
        """Retorna mensagem padrão de tratamento (polimórfico)."""
        return f"{self.nome} recebeu cuidado/tratamento de rotina."

    def tomar_banho_de_sol(self):
        """Registra banho de sol."""
        return f"{self.nome} tomou banho de sol."

    def exibir_dados(self):
        """Exibe os dados do animal de forma legível."""
        return (f"[Animal {self.id_animal}] {self.nome} | Espécie: {self.especie} | "
                f"Idade: {self.idade} | Alimentação: {self.tipo_alimentacao} | "
                f"Recinto: {self.recinto} | Saúde: {self.status_saude}")

    # ---------- Persistência ----------
    def to_dict(self):
        """Converte o objeto em dicionário para gravação no CSV."""
        return {
            "id_animal": self.id_animal,
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "tipo_alimentacao": self.tipo_alimentacao,
            "recinto": self.recinto,
            "status_saude": self.status_saude,
            "tipo": self.__class__.__name__,
            "extra": self._extra_para_csv(),
        }

    def _extra_para_csv(self):
        """Atributo específico da subclasse (sobrescrito nas filhas)."""
        return ""

    @classmethod
    def from_dict(cls, dados):
        """Cria o objeto correto (Animal/Mamifero/Ave/Reptil) a partir do CSV.

        Importação tardia para evitar import circular.
        """
        from modelos.mamifero import Mamifero
        from modelos.ave import Ave
        from modelos.reptil import Reptil

        tipo = (dados.get("tipo") or "Animal").strip()
        extra = (dados.get("extra") or "").strip()
        base = dict(
            id_animal=int(dados["id_animal"]),
            nome=dados["nome"],
            especie=dados["especie"],
            idade=int(dados["idade"]),
            tipo_alimentacao=dados["tipo_alimentacao"],
            recinto=dados["recinto"],
            status_saude=dados["status_saude"],
        )
        if tipo == "Mamifero":
            return Mamifero(tipo_pelagem=extra or "Não informada", **base)
        if tipo == "Ave":
            return Ave(pode_voar=extra or "Não", **base)
        if tipo == "Reptil":
            return Reptil(venenoso=extra or "Não", **base)
        return cls(**base)
