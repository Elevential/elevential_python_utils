from openpyxl import Workbook


def create_from_dict(dicionario_lista_dicionarios):
    """
    Função de criação genérica de arquivos .xlsx

    Essa função recebe um dicionário de listas de dicionários,
    Cada chave de "dicionário_lista_dicionarios" criará uma aba no xlsx,
    para o header será usado as chaves encontradas no indice 0 de cada lista.
    Cada dicionário na lista será uma linha no xlsx.

    Parametros:
    -----------
    dicionario_lista_dicionarios: dict
        Dicionário onde cada chave será uma aba do xlsx
    arquivo_temp: file
        arquivo onde salvaremos o dicionário
    """
    wb = Workbook()
    default = wb.active
    for titulo, lista_dicionario in dicionario_lista_dicionarios.items():
        wb.create_sheet(titulo)
        sheet = wb.get_sheet_by_name(titulo)
        sheet.title = titulo
        if lista_dicionario:
            header = tuple(lista_dicionario[0].keys())
            sheet.append(header)
            for dicionario in lista_dicionario:
                sheet.append(tuple(dicionario.values()))
        dims = {}
        for row in sheet.rows:
            for cell in row:
                if cell.value:
                    dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))  
        for col, value in dims.items():
            sheet.column_dimensions[col].width = value
    wb.remove_sheet(default)
    return wb


def as_text(value):
    if value is None:
        return ""
    return str(value)