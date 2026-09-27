"""Serviço de recintos — regras de negócio e validações."""

from modelos.recinto import Recinto


class RecintoService:
    """Orquestra cadastro, consulta e limpeza de recintos."""

    def __init__(self, repository):
        self.repo = repository

    def _obrigatorio(self, valor, campo):
        if valor is None or str(valor).strip() == "":
            raise ValueError(f"Campo obrigatório vazio: {campo}.")
        return str(valor).strip()

    def cadastrar(self, nome, tipo, capacidade, localizacao,
                  status_limpeza="Limpo"):
        nome = self._obrigatorio(nome, "nome")
        tipo = self._obrigatorio(tipo, "tipo")
        localizacao = self._obrigatorio(localizacao, "localizacao")
        try:
            capacidade = int(capacidade)
        except (ValueError, TypeError):
            raise ValueError("Capacidade inválida. Digite um número inteiro.")
        if capacidade <= 0:
            raise ValueError("Capacidade deve ser maior que zero.")
        novo_id = self.repo.proximo_id()
        recinto = Recinto(novo_id, nome, tipo, capacidade,
                          localizacao, status_limpeza or "Limpo")
        self.repo.salvar(recinto)
        return recinto

    def listar(self):
        return self.repo.listar()

    def buscar(self, identificador):
        texto = str(identificador).strip()
        recinto = None
        if texto.isdigit():
            recinto = self.repo.buscar_por_id(int(texto))
        if recinto is None:
            recinto = self.repo.buscar_por_nome(texto)
        if recinto is None:
            raise LookupError(f"Recinto '{identificador}' não encontrado.")
        return recinto

    def marcar_como_limpo(self, recinto):
        """Atualiza o status do recinto para 'Limpo' e persiste."""
        recinto.limpar()
        self.repo.atualizar(recinto)
        return recinto
