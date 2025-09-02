
"""
  Mavzu: Resurslar bilan ishlash — with (context manager) va try/finally.
  Xatolik turlari: FileNotFoundError.
  Qayerda ishlatish: Fayl, soket, ulanishlarni ochish/yopish.

  Topic: Resource handling — with (context manager) and try/finally.
  Error types: FileNotFoundError.
  When to use: Opening/closing files, sockets, connections.
"""

# WITH: tavsiya etiladi
def read_with(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()

# TRY/FINALLY: agar 'with' yo'q bo'lsa
def read_try_finally(path: str) -> str:
    f = open(path, encoding="utf-8")
    try:
        return f.read()
    finally:
        f.close()

# Xatoni to'g'ri zanjirlash
def read_or_raise(path: str) -> str:
    try:
        return read_with(path)
    except FileNotFoundError as e:
        # UZ: Asl xatoni e sifatida ushlab, ma'lum xabar bilan qayta ko'taramiz
        # EN: Capture original as e and re-raise with a clearer message
        raise FileNotFoundError(f"UZ: Fayl topilmadi: {path!r}  EN: File not found: {path!r}") from e

if __name__ == "__main__":
    try:
        print(read_or_raise("input.txt"))
    except FileNotFoundError as e:
        print("Caught:", e)
