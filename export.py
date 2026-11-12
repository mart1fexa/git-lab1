"""Экспорт списка деталей склада в CSV-файл."""
from parts import load_parts


def export_csv(src="parts.txt", dst="parts.csv"):
    parts = load_parts(src)
    with open(dst, "w", encoding="utf-8") as f:
        f.write("code,name,qty\n")
        for p in parts:
            f.write(f"{p['code']},{p['name']},{p['qty']}\n")
    return len(parts)


def export_names(parts):
    return "\n".join(p["name"] for p in parts)
