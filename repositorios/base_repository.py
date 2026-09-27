"""Utilidades base para os repositórios CSV."""

import csv
import os


def garantir_arquivo(caminho, cabecalho):
    """Cria pasta e arquivo com cabeçalho caso não existam."""
    pasta = os.path.dirname(caminho)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)
    if not os.path.exists(caminho):
        try:
            with open(caminho, mode="w", newline="", encoding="utf-8-sig") as f:
                writer = csv.DictWriter(f, fieldnames=cabecalho)
                writer.writeheader()
        except OSError as e:
            print(f"Erro ao criar arquivo {caminho}: {e}")
    return caminho


def ler_todos(caminho, cabecalho):
    """Lê todas as linhas do CSV. Retorna lista de dicts (vazia se inexistente)."""
    garantir_arquivo(caminho, cabecalho)
    try:
        with open(caminho, mode="r", newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            return [dict(linha) for linha in reader if any((v or "").strip() for v in linha.values())]
    except FileNotFoundError:
        return []
    except OSError as e:
        print(f"Erro ao ler arquivo {caminho}: {e}")
        return []


def salvar_todos(caminho, cabecalho, linhas):
    """Regrava o CSV inteiro a partir de uma lista de dicts."""
    garantir_arquivo(caminho, cabecalho)
    try:
        with open(caminho, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(linhas)
    except OSError as e:
        print(f"Erro ao gravar arquivo {caminho}: {e}")


def adicionar_linha(caminho, cabecalho, linha):
    """Adiciona uma linha ao CSV preservando o histórico."""
    registros = ler_todos(caminho, cabecalho)
    registros.append(linha)
    salvar_todos(caminho, cabecalho, registros)


def proximo_id(registros, campo_id):
    """Calcula o próximo ID livre (max + 1)."""
    maior = 0
    for r in registros:
        try:
            valor = int(str(r.get(campo_id, 0)).strip() or 0)
            maior = max(maior, valor)
        except (ValueError, TypeError):
            continue
    return maior + 1
