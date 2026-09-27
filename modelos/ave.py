"""Subclasse Ave — especialização de Animal (herança + polimorfismo)."""

from modelos.animal import Animal


class Ave(Animal):
    """Representa uma ave do zoológico."""

    def __init__(self, id_animal, nome, especie, idade,
                 tipo_alimentacao, recinto, status_saude, pode_voar="Sim"):
        super().__init__(id_animal, nome, especie, idade,
                         tipo_alimentacao, recinto, status_saude)
        self.pode_voar = pode_voar

    def alimentar(self):
        # Polimorfismo: comportamento específico da ave.
        return (f"A ave {self.nome} foi alimentada com {self.tipo_alimentacao} "
                f"(oferecida em comedouro elevado).")

    def tratar(self):
        # Polimorfismo: comportamento específico da ave.
        return (f"A ave {self.nome} teve asas e bico inspecionados "
                f"(voa: {self.pode_voar}).")

    def _extra_para_csv(self):
        return str(self.pode_voar)

    def exibir_dados(self):
        return super().exibir_dados() + f" | Tipo: Ave | Voa: {self.pode_voar}"
