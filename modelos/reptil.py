"""Subclasse Reptil — especialização de Animal (herança + polimorfismo)."""

from modelos.animal import Animal


class Reptil(Animal):
    """Representa um réptil do zoológico."""

    def __init__(self, id_animal, nome, especie, idade,
                 tipo_alimentacao, recinto, status_saude, venenoso="Não"):
        super().__init__(id_animal, nome, especie, idade,
                         tipo_alimentacao, recinto, status_saude)
        self.venenoso = venenoso

    def alimentar(self):
        # Polimorfismo: comportamento específico do réptil.
        return (f"O réptil {self.nome} foi alimentado com {self.tipo_alimentacao} "
                f"(manejo com pinça por segurança, venenoso: {self.venenoso}).")

    def tratar(self):
        # Polimorfismo: comportamento específico do réptil.
        return (f"O réptil {self.nome} teve terrário e temperatura verificados "
                f"(venenoso: {self.venenoso}, manejo com EPIs).")

    def _extra_para_csv(self):
        return str(self.venenoso)

    def exibir_dados(self):
        return super().exibir_dados() + f" | Tipo: Réptil | Venenoso: {self.venenoso}"
