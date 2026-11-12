"""Формирование текстового отчёта по складу."""
from parts import load_parts, total_count


def make_report(path="parts.txt"):
    parts = load_parts(path)
    lines = ["ОТЧЁТ ПО СКЛАДУ", "-" * 30]
    for p in parts:
        lines.append(f"{p['code']:<8} {p['name']:<22} {p['qty']:>5}")
    lines.append("-" * 30)
    lines.append(f"Итого: {total_count(parts)}")
    return "\n".join(lines)


if __name__ == "__main__":
    print(make_report())
