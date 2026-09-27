"""Serviço de tratadores — regras de negócio e validações."""

from modelos.tratador import Tratador


class TratadorService:
    """Orquestra cadastro e consulta de tratadores."""

    def __init__(self, repository):
        self.repo = repository

    def _obrigatorio(self, valor, campo):
        if valor is None or str(valor).strip() == "":
            raise ValueError(f"Campo obrigatório vazio: {campo}.")
        return str(valor).strip()

    def cadastrar(self, nome, turno, especialidade, animais_responsaveis=""):
        nome = self._obrigatorio(nome, "nome")
        turno = self._obrigatorio(turno, "turno")
        especialidade = self._obrigatorio(especialidade, "especialidade")
        novo_id = self.repo.proximo_id()
        tratador = Tratador(novo_id, nome, turno, especialidade, animais_responsaveis)
        self.repo.salvar(tratador)
        return tratador

    def listar(self):
        return self.repo.listar()

    def buscar(self, identificador):
        texto = str(identificador).strip()
        tratador = None
        if texto.isdigit():
            tratador = self.repo.buscar_por_id(int(texto))
        if tratador is None:
            tratador = self.repo.buscar_por_nome(texto)
        if tratador is None:
            raise LookupError(f"Tratador '{identificador}' não encontrado.")
        return tratador
