# Учёт деталей склада - точка входа
from parts import load_parts, total_count, find_part

parts = load_parts("parts.txt")
print("Позиций на складе:", len(parts))
print("Всего деталей:", total_count(parts))
print("Поиск MIG-002:", find_part(parts, "MIG-002"))
