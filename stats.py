def average_qty(parts):
    return sum(p["qty"] for p in parts) / len(parts)


def max_qty(parts):
    return max(parts, key=lambda p: p["qty"])
