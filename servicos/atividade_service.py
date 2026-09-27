"""Serviço de atividades — registra alimentação, tratamento, limpeza e banho de sol."""

from datetime import datetime

from modelos.atividade import Atividade


class AtividadeService:
    """Centraliza o registro de atividades com validações de negócio."""

    TIPOS_VALIDOS = ("Alimentação", "Tratamento", "Limpeza", "Banho de sol")

    def __init__(self, repository, animal_service, tratador_service,
                 recinto_service=None):
        self.repo = repository
        self.animais = animal_service
        self.tratadores = tratador_service
        self.recintos = recinto_service

    def _data_hora_padrao(self, data, hora):
        agora = datetime.now()
        data = (data or "").strip() or agora.strftime("%d/%m/%Y")
        hora = (hora or "").strip() or agora.strftime("%H:%M")
        return data, hora

    def _registrar(self, tipo, nome_animal, nome_tratador,
                   data, hora, descricao, nome_recinto=None):
        # Regra: animal precisa existir (exceto limpeza, que exige recinto).
        # Regra: tratador precisa existir para executar a atividade.
        # Regra: toda atividade gera um registro.
        tratador = self.tratadores.buscar(nome_tratador)

        if tipo == "Limpeza":
            if self.recintos is None:
                raise ValueError("Serviço de recintos não configurado.")
            recinto = self.recintos.buscar(nome_recinto or nome_animal)
            animal_nome = f"Recinto {recinto.nome}"
            self.recintos.marcar_como_limpo(recinto)
            if descricao is None or str(descricao).strip() == "":
                descricao = f"Limpeza do recinto {recinto.nome}."
        else:
            animal = self.animais.buscar(nome_animal)
            animal_nome = animal.nome
            # Demonstra polimorfismo: o comportamento varia por tipo de animal.
            if tipo == "Alimentação":
                acao = animal.alimentar()
            elif tipo == "Tratamento":
                acao = animal.tratar()
            elif tipo == "Banho de sol":
                acao = animal.tomar_banho_de_sol()
            else:
                acao = ""
            if descricao is None or str(descricao).strip() == "":
                descricao = acao
            if tipo == "Alimentação":
                tratador.alimentar_animal(animal)
            elif tipo == "Tratamento":
                tratador.tratar_animal(animal)

        if not str(descricao).strip():
            descricao = f"{tipo} realizada."

        data, hora = self._data_hora_padrao(data, hora)
        atividade = Atividade(
            id_atividade=self.repo.proximo_id(),
            tipo_atividade=tipo,
            data=data,
            hora=hora,
            animal=animal_nome,
            tratador=tratador.nome,
            descricao=str(descricao).strip(),
        )
        self.repo.salvar(atividade)
        return atividade

    # ---------- Métodos públicos (um por funcionalidade do menu) ----------
    def alimentar(self, nome_animal, nome_tratador, data="", hora="", descricao=""):
        return self._registrar("Alimentação", nome_animal, nome_tratador,
                               data, hora, descricao)

    def tratar(self, nome_animal, nome_tratador, data="", hora="", descricao=""):
        return self._registrar("Tratamento", nome_animal, nome_tratador,
                               data, hora, descricao)

    def limpar_recinto(self, nome_recinto, nome_tratador,
                       data="", hora="", descricao=""):
        return self._registrar("Limpeza", nome_recinto, nome_tratador,
                               data, hora, descricao, nome_recinto=nome_recinto)

    def banho_de_sol(self, nome_animal, nome_tratador, data="", hora="", descricao=""):
        return self._registrar("Banho de sol", nome_animal, nome_tratador,
                               data, hora, descricao)

    def listar(self):
        return self.repo.listar()
