"""Serviço de animais — regras de negócio e validações."""

from modelos.mamifero import Mamifero
from modelos.ave import Ave
from modelos.reptil import Reptil
from modelos.animal import Animal


class AnimalService:
    """Orquestra cadastro e consulta de animais."""

    def __init__(self, repository):
        self.repo = repository

    def _validar_obrigatorio(self, valor, nome_campo):
        if valor is None or str(valor).strip() == "":
            raise ValueError(f"Campo obrigatório vazio: {nome_campo}.")
        return str(valor).strip()

    def cadastrar(self, nome, especie, idade, tipo_alimentacao,
                  recinto, status_saude, tipo="Animal", extra=""):
        """Valida, instancia a subclasse correta e persiste."""
        nome = self._validar_obrigatorio(nome, "nome")
        especie = self._validar_obrigatorio(especie, "espécie")
        tipo_alimentacao = self._validar_obrigatorio(tipo_alimentacao, "tipo_alimentacao")
        recinto = self._validar_obrigatorio(recinto, "recinto")
        status_saude = self._validar_obrigatorio(status_saude, "status_saude")

        try:
            idade = int(idade)
        except (ValueError, TypeError):
            raise ValueError("Idade inválida. Digite um número inteiro.")
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")

        tipo = (tipo or "Animal").strip().capitalize()
        novo_id = self.repo.proximo_id()

        if tipo == "Mamifero":
            animal = Mamifero(novo_id, nome, especie, idade, tipo_alimentacao,
                              recinto, status_saude, tipo_pelagem=extra or "Não informada")
        elif tipo == "Ave":
            animal = Ave(novo_id, nome, especie, idade, tipo_alimentacao,
                         recinto, status_saude, pode_voar=extra or "Sim")
        elif tipo == "Reptil":
            animal = Reptil(novo_id, nome, especie, idade, tipo_alimentacao,
                            recinto, status_saude, venenoso=extra or "Não")
        else:
            animal = Animal(novo_id, nome, especie, idade, tipo_alimentacao,
                            recinto, status_saude)

        self.repo.salvar(animal)
        return animal

    def listar(self):
        return self.repo.listar()

    def buscar(self, identificador):
        """Busca por ID (número) ou por nome (texto)."""
        texto = str(identificador).strip()
        animal = None
        if texto.isdigit():
            animal = self.repo.buscar_por_id(int(texto))
        if animal is None:
            animal = self.repo.buscar_por_nome(texto)
        if animal is None:
            raise LookupError(f"Animal '{identificador}' não encontrado.")
        return animal
