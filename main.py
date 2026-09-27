"""Sistema de Controle de Animais em um Zoológico — ponto de entrada (main.py).

Execução: python main.py
"""

from modelos.administrador import Administrador
from repositorios.animal_repository import AnimalRepository
from repositorios.tratador_repository import TratadorRepository
from repositorios.recinto_repository import RecintoRepository
from repositorios.atividade_repository import AtividadeRepository
from servicos.animal_service import AnimalService
from servicos.tratador_service import TratadorService
from servicos.recinto_service import RecintoService
from servicos.atividade_service import AtividadeService


# ---------- Instâncias globais (composição) ----------
animal_repo = AnimalRepository()
tratador_repo = TratadorRepository()
recinto_repo = RecintoRepository()
atividade_repo = AtividadeRepository()

animal_service = AnimalService(animal_repo)
tratador_service = TratadorService(tratador_repo)
recinto_service = RecintoService(recinto_repo)
atividade_service = AtividadeService(atividade_repo, animal_service,
                                     tratador_service, recinto_service)
admin = Administrador(1, "Administrador")


# ---------- Helpers de entrada ----------
def ler_texto(prompt, obrigatorio=True):
    """Lê texto com validação de campo obrigatório."""
    valor = input(prompt).strip()
    if obrigatorio and not valor:
        raise ValueError("Campo obrigatório vazio.")
    return valor


def ler_inteiro(prompt):
    """Lê inteiro com tratamento de erro."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        raise ValueError("Valor inválido. Digite um número inteiro.")


def pausar():
    input("\nPressione ENTER para continuar...")


def exibir_menu():
    print("\n===== SISTEMA DE ZOOLÓGICO =====")
    print("1 - Cadastrar animal")
    print("2 - Listar animais")
    print("3 - Cadastrar tratador")
    print("4 - Listar tratadores")
    print("5 - Cadastrar recinto")
    print("6 - Listar recintos")
    print("7 - Alimentar animal")
    print("8 - Tratar animal")
    print("9 - Limpar recinto")
    print("10 - Registrar banho de sol")
    print("11 - Relatório de atividades")
    print("0 - Sair")


# ---------- Funcionalidades ----------
def op_cadastrar_animal():
    print("\n--- Cadastrar animal ---")
    try:
        nome = ler_texto("Nome: ")
        especie = ler_texto("Espécie (ex: Panthera leo): ")
        idade = ler_inteiro("Idade: ")
        tipo_alimentacao = ler_texto("Tipo de alimentação (Carnívoro/Herbívoro/Onívoro...): ")
        recinto = ler_texto("Recinto (nome ou ID): ")
        status_saude = ler_texto("Status de saúde (Saudável/Em tratamento...): ")
        print("Tipo: 1-Mamífero  2-Ave  3-Réptil  4-Animal genérico")
        escolha = input("Escolha o tipo [1-4]: ").strip()
        mapa = {"1": "Mamifero", "2": "Ave", "3": "Reptil", "4": "Animal"}
        tipo = mapa.get(escolha, "Animal")
        extra = ""
        if tipo == "Mamifero":
            extra = input("Tipo de pelagem (ex: Pelos curtos) [opcional]: ").strip()
        elif tipo == "Ave":
            extra = input("Pode voar? (Sim/Não) [padrão Sim]: ").strip() or "Sim"
        elif tipo == "Reptil":
            extra = input("Venenoso? (Sim/Não) [padrão Não]: ").strip() or "Não"
        animal = animal_service.cadastrar(nome, especie, idade, tipo_alimentacao,
                                          recinto, status_saude, tipo, extra)
        print(f"\nAnimal cadastrado com sucesso! ID = {animal.id_animal}")
        print(animal.exibir_dados())
    except (ValueError, LookupError, OSError) as e:
        print(f"Erro: {e}")


def op_listar_animais():
    print("\n--- Animais cadastrados ---")
    try:
        animais = animal_service.listar()
        if not animais:
            print("Nenhum animal cadastrado.")
            return
        for a in animais:
            print(a.exibir_dados())
        print(f"\nTotal: {len(animais)} animal(is).")
    except OSError as e:
        print(f"Erro ao listar animais: {e}")


def op_cadastrar_tratador():
    print("\n--- Cadastrar tratador ---")
    try:
        nome = ler_texto("Nome: ")
        turno = ler_texto("Turno (Manhã/Tarde/Noite): ")
        especialidade = ler_texto("Especialidade (ex: Mamíferos, Aves...): ")
        responsaveis = input("Animais responsáveis (separados por ';') [opcional]: ").strip()
        tratador = tratador_service.cadastrar(nome, turno, especialidade, responsaveis)
        print(f"\nTratador cadastrado com sucesso! ID = {tratador.id_tratador}")
        print(tratador.exibir_dados())
    except (ValueError, OSError) as e:
        print(f"Erro: {e}")


def op_listar_tratadores():
    print("\n--- Tratadores cadastrados ---")
    try:
        tratadores = tratador_service.listar()
        if not tratadores:
            print("Nenhum tratador cadastrado.")
            return
        for t in tratadores:
            print(t.exibir_dados())
        print(f"\nTotal: {len(tratadores)} tratador(es).")
    except OSError as e:
        print(f"Erro ao listar tratadores: {e}")


def op_cadastrar_recinto():
    print("\n--- Cadastrar recinto ---")
    try:
        nome = ler_texto("Nome (ex: Recinto 01): ")
        tipo = ler_texto("Tipo (ex: Jaula, Viveiro, Terrário): ")
        capacidade = ler_inteiro("Capacidade (nº de animais): ")
        localizacao = ler_texto("Localização (ex: Ala Norte): ")
        status = input("Status de limpeza [padrão Limpo]: ").strip() or "Limpo"
        recinto = recinto_service.cadastrar(nome, tipo, capacidade, localizacao, status)
        print(f"\nRecinto cadastrado com sucesso! ID = {recinto.id_recinto}")
        print(recinto.exibir_dados())
    except (ValueError, OSError) as e:
        print(f"Erro: {e}")


def op_listar_recintos():
    print("\n--- Recintos cadastrados ---")
    try:
        recintos = recinto_service.listar()
        if not recintos:
            print("Nenhum recinto cadastrado.")
            return
        for r in recintos:
            print(r.exibir_dados())
        print(f"\nTotal: {len(recintos)} recinto(s).")
    except OSError as e:
        print(f"Erro ao listar recintos: {e}")


def _pedir_dados_atividade(usa_recinto=False):
    rotulo = "Recinto (nome ou ID)" if usa_recinto else "Animal (nome ou ID)"
    alvo = ler_texto(f"{rotulo}: ")
    tratador = ler_texto("Tratador (nome ou ID): ")
    data = input("Data (DD/MM/AAAA) [ENTER = hoje]: ").strip()
    hora = input("Hora (HH:MM) [ENTER = agora]: ").strip()
    descricao = input("Descrição [ENTER = automática]: ").strip()
    return alvo, tratador, data, hora, descricao


def op_alimentar():
    print("\n--- Alimentar animal ---")
    try:
        alvo, tratador, data, hora, descricao = _pedir_dados_atividade()
        atv = atividade_service.alimentar(alvo, tratador, data, hora, descricao)
        print(f"\n{atv.registrar()}")
    except (ValueError, LookupError, OSError) as e:
        print(f"Erro: {e}")


def op_tratar():
    print("\n--- Tratar animal ---")
    try:
        alvo, tratador, data, hora, descricao = _pedir_dados_atividade()
        atv = atividade_service.tratar(alvo, tratador, data, hora, descricao)
        print(f"\n{atv.registrar()}")
    except (ValueError, LookupError, OSError) as e:
        print(f"Erro: {e}")


def op_limpar_recinto():
    print("\n--- Limpar recinto ---")
    try:
        alvo, tratador, data, hora, descricao = _pedir_dados_atividade(usa_recinto=True)
        atv = atividade_service.limpar_recinto(alvo, tratador, data, hora, descricao)
        print(f"\n{atv.registrar()}")
        print("Status do recinto atualizado para 'Limpo'.")
    except (ValueError, LookupError, OSError) as e:
        print(f"Erro: {e}")


def op_banho_de_sol():
    print("\n--- Registrar banho de sol ---")
    try:
        alvo, tratador, data, hora, descricao = _pedir_dados_atividade()
        atv = atividade_service.banho_de_sol(alvo, tratador, data, hora, descricao)
        print(f"\n{atv.registrar()}")
    except (ValueError, LookupError, OSError) as e:
        print(f"Erro: {e}")


def op_relatorio():
    print("\n--- Relatório de atividades ---")
    try:
        atividades = atividade_service.listar()
        if not atividades:
            print("Nenhuma atividade registrada.")
            return
        rel = admin.gerar_relatorio_atividades(atividades)
        print(f"\nTotal de atividades: {rel['total']}")
        print("\nPor tipo:")
        for tipo, qtd in rel["por_tipo"].items():
            print(f"  - {tipo}: {qtd}")
        print("\nPor animal/recinto:")
        for animal, qtd in rel["por_animal"].items():
            print(f"  - {animal}: {qtd}")
        print("\nPor tratador:")
        for tratador, qtd in rel["por_tratador"].items():
            print(f"  - {tratador}: {qtd}")

        filtro = input("\nFiltrar por tratador (nome ou ENTER para pular): ").strip()
        if filtro:
            encontradas = admin.consultar_atividades_por_tratador(atividades, filtro)
            print(f"\nAtividades de '{filtro}': {len(encontradas)}")
            for a in encontradas:
                print("  " + a.exibir_dados())

        print("\n--- Detalhamento ---")
        for a in atividades:
            print(a.exibir_dados())
    except OSError as e:
        print(f"Erro ao gerar relatório: {e}")


def main():
    acoes = {
        "1": op_cadastrar_animal,
        "2": op_listar_animais,
        "3": op_cadastrar_tratador,
        "4": op_listar_tratadores,
        "5": op_cadastrar_recinto,
        "6": op_listar_recintos,
        "7": op_alimentar,
        "8": op_tratar,
        "9": op_limpar_recinto,
        "10": op_banho_de_sol,
        "11": op_relatorio,
    }
    while True:
        try:
            exibir_menu()
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "0":
                print("Encerrando o sistema. Até logo!")
                break
            acao = acoes.get(opcao)
            if acao is None:
                print("Opção inválida. Tente novamente.")
                continue
            acao()
            pausar()
        except KeyboardInterrupt:
            print("\nEncerrando o sistema. Até logo!")
            break
        except Exception as e:  # garante que o sistema não encerre inesperadamente
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
