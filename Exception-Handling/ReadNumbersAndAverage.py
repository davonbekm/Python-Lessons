
"""
  Mavzu: Fayldan sonlarni o'qish va o'rtacha hisoblash (xatolarga chidamli).
  Xatolik turlari: FileNotFoundError, ValueError.
  Qayerda ishlatish: Ma'lumotlarni tozalab o'qish, log/diagnostika bilan davom etish.

  Topic: Read numbers from a file and compute average (error-tolerant).
  Error types: FileNotFoundError, ValueError.
  When to use: Robust ingestion with logging/diagnostics.
"""

def read_numbers(path: str) -> list[int]:
    numbers: list[int] = []
    bad = 0
    try:
        with open(path, encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                try:
                    numbers.append(int(s))
                except ValueError as e:
                    bad += 1
                    print(f"{path}:{line_no} not a valid integer: {s!r} ({e})")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    else:
        if bad == 0 and numbers:
            print("Successfully: all lines are valid.")
        elif numbers:
            print(f"Read {len(numbers)} numbers with {bad} bad line(s).")
        else:
            print("File read, but no valid numbers were found.")
    return numbers

def average(nums: list[int]) -> float:
    if not nums:
        raise ValueError("Empty list: cannot compute average.")
    return sum(nums) / len(nums)

if __name__ == "__main__":
    try:
        nums = read_numbers("numbers.txt")
        avg = average(nums)
    except ValueError as e:
        print("Compute error:", e)
    else:
        print("Average:", avg)
