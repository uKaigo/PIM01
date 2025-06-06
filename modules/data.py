import os
import sys
import json
from typing import Any


def get_data_file(path: str) -> Any:
    """
    Lê um arquivo JSON e retorna seu conteúdo.

    Parameters
    ----------
    path: :class:`str`
        Caminho do arquivo a ser lido.

    Returns
    -------
    :class:`typing.Any`
        O conteúdo do arquivo JSON.
    """
    # Verifica se executando dentro do PyInstaller e ajusta o caminho.
    path = f'{sys._MEIPASS}/{path}' if hasattr(sys, '_MEIPASS') else path  # type: ignore

    if not os.path.exists(path):
        return {}

    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_data_file(path: str, data: Any):
    """
    Salva dados em um arquivo JSON.

    Parameters
    ----------
    path: :class:`str`
        Caminho do arquivo a ser salvo.
    data: :class:`typing.Any`
        Dados a serem salvos no arquivo JSON.
    """
    # Verifica se executando dentro do PyInstaller e ajusta o caminho.
    path = f'{sys._MEIPASS}/{path}' if hasattr(sys, '_MEIPASS') else path  # type: ignore

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
