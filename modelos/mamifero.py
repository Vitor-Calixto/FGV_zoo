"""Subclasse Mamifero — especialização de Animal (herança + polimorfismo)."""

from modelos.animal import Animal


class Mamifero(Animal):
    """Representa um animal mamífero."""

    def __init__(self, id_animal, nome, especie, idade,
                 tipo_alimentacao, recinto, status_saude, tipo_pelagem="Curta"):
        super().__init__(id_animal, nome, especie, idade,
                         tipo_alimentacao, recinto, status_saude)
        self.tipo_pelagem = tipo_pelagem

    def alimentar(self):
        # Polimorfismo: comportamento específico do mamífero.
        return (f"O mamífero {self.nome} foi alimentado com {self.tipo_alimentacao} "
                f"(pelagem {self.tipo_pelagem}, cuidado com a quantidade).")

    def tratar(self):
        # Polimorfismo: comportamento específico do mamífero.
        return (f"O mamífero {self.nome} passou por exame clínico "
                f"(pelagem e temperatura verificadas).")

    def _extra_para_csv(self):
        return self.tipo_pelagem

    def exibir_dados(self):
        return super().exibir_dados() + f" | Tipo: Mamífero | Pelagem: {self.tipo_pelagem}"
