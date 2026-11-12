"""Модуль работы со списком деталей склада."""


def load_parts(path):
    """Читает файл с деталями: код;наименование;количество."""
    parts = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            code, name, qty = line.split(";")
            parts.append({"code": code, "name": name, "qty": int(qty)})
    return parts


def total_count(parts):
    """Общее количество деталей на складе."""
    return sum(p["qty"] for p in parts)


def find_part(parts, code):
    """Поиск детали по коду."""
    for p in parts:
        if p["code"] == code:
            return p
    return None
