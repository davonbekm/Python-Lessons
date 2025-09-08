# Python’da Xatoliklar bilan Ishlash — Exceptions & Error Handling (+ English commentary)

> : Exception Handling `try / except / else / finally`, `raise`, `raise ... from e`, `assert`, `enumerate`, EAFP vs LBYL.

---

## Re'ja
- [1. Asosiy tushuncha (TL;DR)](#1-tez-tushuncha-tldr)
- [2. Asosiy naqsh: try / except / else / finally](#2-asosiy-naqsh-try--except--else--finally)
- [3. Xatoni ko‘tarish: raise va from e](#3-xatoni-kotarish-raise-va-from-e)
- [4. Bir nechta except, keng guard, va custom exception](#4-bir-nechta-except-keng-guard-va-custom-exception)
- [5. EAFP vs LBYL](#5-eafp-vs-lbyl)
- [6. Resurslar: with va finally](#6-resurslar-with-va-finally)
- [7. Ee: Fayldan o‘qish va o‘rtacha...](#7-amaliy-mini-loyiha-fayldan-oqish-va-ortacha)
- [8. assert](#8-assert--qachon-ishlatamiz-qachon-yoq)
- [9. enumerate nima qiladi](#9-enumerate-nima-qiladi)
- [10. English version](#14-english-version)

---

## 1) Asosiy tushuncha (TL;DR)
- **try** — xatoga moyil kod shu yerda.
- **except** — xato bo‘lsa shu ishga tushadi (aniq turini ushlashga harakat qiling).
- **else** — **xato bo‘lmasa** ishga tushadi (muvaffaqiyat yo‘li).
- **finally** — **har doim** ishlaydi (tozalash/yopish).
- **raise** — xatoni ataylab ko‘tarish.
- **raise ... from e** — yangi xatoni asl sabab (`e`) bilan zanjirlash.
- **assert** — ichki/invariant tekshiruvlar (prod’da o‘chishi mumkin).
- **EAFP** (Python-uslubi) ko‘pincha **LBYL**dan afzal.

---

## 2) Asosiy naqsh: `try / except / else / finally`

```python
try:
    risk = int(input("Son kiriting: "))  # ValueError bo‘lishi mumkin
except ValueError as e:
    print("Raqam kiriting, iltimos:", e)
else:
    print("Muvaffaqiyatli o‘qildi:", risk)  # faqat xato bo‘lmasa
finally:
    print("Har holda bajariladigan ish (masalan, resursni yopish).")
```

**Tavsiyalar:**
- `try` ichiga faqat xatarga moyil qatorlarni qo‘ying.
- “Hammasi joyida bo‘lsa bajariladigan” ishlarni `else`ga.
- Tozalash ishlari `finally`da (unda `return` yozishdan saqlaning).

---

## 3) Xatoni ko‘tarish: `raise` va `from e`

```python
def parse_age(text: str) -> int:
    try:
        return int(text)
    except ValueError as e:
        # foydalanuvchiga ma'noli xabar + asl sabab zanjiri
        raise ValueError(f"Yosh noto‘g‘ri formatda: {text!r}") from e
```

- `{text!r}` — qiymatni **repr** ko‘rinishida (qo‘shtirnoqlar bilan) ko‘rsatadi.
- `from e` — traceback’da “asl sabab”ni saqlaydi (diagnostika oson).

**Oddiy foydalanish:**

```python
try:
    age = parse_age("12a")
except ValueError as e:
    print("Xato:", e)  # -> Yosh noto‘g‘ri formatda: '12a'
```

---

## 4) Bir nechta `except`, keng guard, va custom exception

```python
class DomainError(Exception):
    """Biznes qoidasi buzilganda."""

def buy_ticket(age: int):
    if age < 0:
        raise DomainError("Yosh manfiy bo‘lishi mumkin emas")

data = {"age": "25"}
try:
    age = int(data["age"])           # KeyError yoki ValueError
except KeyError:
    print("Kalit topilmadi.")
except ValueError:
    print("Yosh butun son bo‘lishi kerak.")
except Exception as e:               # keng guard (faqat yuqori qatlamda)
    print("Noma'lum xato:", e)
    raise
else:
    print("OK:", age)
finally:
    print("Tozalash.")
```

---

## 5) EAFP vs LBYL

```python
# EAFP — “Oldin qil, xato bo‘lsa tut” (Python-uslubi)
try:
    value = cache[key]
except KeyError:
    value = compute_and_store(key)

# LBYL — “Avval tekshir, keyin qil”
if key in cache:
    value = cache[key]
else:
    value = compute_and_store(key)
```

**Nega EAFP ko‘p hollarda yaxshi?**  
Race/TOCTOU holatlarida ishonchliroq; lug‘atga 2 marta murojaat qilmaydi.

---

## 6) Resurslar: `with` va `finally`

```python
# To'g'ri:
with open("input.txt", encoding="utf-8") as f:
    text = f.read()

# Agar context manager bo'lmasa:
f = open("input.txt", encoding="utf-8")
try:
    text = f.read()
finally:
    f.close()
```

---

## 7) Amaliy mini-loyiha: fayldan o‘qish va o‘rtacha

**Faylni o‘qish (yomon satrlarni tashlab ketish):**

```python
def read_numbers(path: str) -> list[int]:
    numbers = []
    try:
        with open(path, encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    numbers.append(int(line))
                except ValueError as e:
                    print(f"{path}:{line_no} noto‘g‘ri son: {line!r} ({e})")
    except FileNotFoundError:
        print(f"Fayl topilmadi: {path}")
        return []
    else:
        print("Fayl muvaffaqiyatli o‘qildi.")
    return numbers
```

**O‘rtacha hisoblash:**

```python
def average(nums: list[int]) -> float:
    if not nums:
        raise ValueError("Bo‘sh ro‘yxat: o‘rtacha hisoblab bo‘lmaydi.")
    return sum(nums) / len(nums)
```

**Barchasini bog‘lash:**

```python
try:
    nums = read_numbers("numbers.txt")
    avg = average(nums)
except ValueError as e:
    print("Hisoblash xatosi:", e)
else:
    print("O‘rtacha:", avg)
```

**Loop izohi (juda sodda):**
- `enumerate(f, start=1)` — satr raqamlarini beradi (`line_no`).
- `strip()` — bo‘sh joy va `
`ni olib tashlaydi.
- Bo‘sh satr bo‘lsa — `continue` bilan o‘tkazib yuboriladi.
- `int(line)` o‘tsa — ro‘yxatga qo‘shiladi; bo‘lmasa xabar chiqariladi.

---

## 8) `assert` — qachon ishlatamiz, qachon yo‘q

- **Kerak**: ichki/invariant tekshiruvlar (dev/testda), masalan “natija [0,1] oralig‘ida bo‘lishi kerak”.
- **Kerak emas**: foydalanuvchi kiritmalari va biznes qoidalari (ular uchun `raise` yozing).

```python
def mean(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Bo‘sh ro‘yxat")
    m = sum(nums) / len(nums)
    assert min(nums) <= m <= max(nums), "Mean invariant buzildi"
    return m
```

> `python -O` bilan ishga tushirilsa `assert`lar olib tashlanadi.

---

## 9) `enumerate` nima qiladi

```python
colors = ["red", "green", "blue"]

for i, c in enumerate(colors, start=1):
    print(i, c)
# 1 red
# 2 green
# 3 blue
```

- Iteratsiya vaqtida **indeks+element** juftliklari beradi.
- Fayl o‘qishda ayniqsa qulay: qaysi satrda xato bo‘lganini aniq ko‘rsatadi.

---

## 14) English version

### Quick Summary (TL;DR)
- **try** — risky code lives here.  
- **except** — runs on error (catch specific types).  
- **else** — runs **only if no error**.  
- **finally** — runs **always** (cleanup).  
- **raise** — deliberately throw an error.  
- **raise ... from e** — chain a clearer error to the original cause.  
- **assert** — internal checks (may be removed).  
- Prefer **EAFP** over LBYL in Python.

### Core pattern
```python
try:
    n = int(input("Enter a number: "))
except ValueError as e:
    print("Please enter an integer:", e)
else:
    print("Parsed:", n)
finally:
    print("Always runs.")
```

### Raising and chaining
```python
def parse_age(text: str) -> int:
    try:
        return int(text)
    except ValueError as e:
        raise ValueError(f"Age is not correct format: {text!r}") from e
```

### Multiple except & custom exception
```python
class DomainError(Exception):
    """Violation of a business rule."""

def buy_ticket(age: int):
    if age < 0:
        raise DomainError("Age cannot be negative")
```

### EAFP vs LBYL
```python
# EAFP
try:
    value = cache[key]
except KeyError:
    value = compute_and_store(key)

# LBYL
if key in cache:
    value = cache[key]
else:
    value = compute_and_store(key)
```

### Resource handling
```python
with open("input.txt", encoding="utf-8") as f:
    text = f.read()
```

### Mini-project: read & average
```python
def read_numbers(path: str) -> list[int]:
    numbers = []
    try:
        with open(path, encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    numbers.append(int(line))
                except ValueError as e:
                    print(f"{path}:{line_no} not a valid integer: {line!r} ({e})")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    else:
        print("File read successfully.")
    return numbers

def average(nums: list[int]) -> float:
    if not nums:
        raise ValueError("Empty list: cannot compute average.")
    return sum(nums) / len(nums)

try:
    nums = read_numbers("numbers.txt")
    avg = average(nums)
except ValueError as e:
    print("Compute error:", e)
else:
    print("Average:", avg)
```

### `assert` — when to use
- For internal invariants only; **don’t** validate user input with `assert`.
```python
def mean(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Empty list")
    m = sum(nums) / len(nums)
    assert min(nums) <= m <= max(nums), "Mean invariant violated"
    return m
```

### `enumerate` quick demo
```python
colors = ["red", "green", "blue"]
for i, c in enumerate(colors, start=1):
    print(i, c)
# 1 red
# 2 green
# 3 blue
```

### Best-practice checklist
- Keep `try` small; move the happy path to `else`.
- Catch specific types; avoid bare `except:`.
- Don’t swallow errors.
- Preserve cause with `raise NewError(...) from e`.
- Avoid `return` inside `finally`.
- Prefer `with` for resources.
- Use broad `except Exception` only as a boundary guard.

### Interview quick answers
- When does `else` run? → Only if `try` had no exception.  
- What does `finally` do? → Always runs (cleanup).  
- Why `raise ... from e`? → Clear message + original cause.  
- `assert` vs `raise`? → `assert` for internal checks; `raise` for real errors.  
- EAFP vs LBYL? → Prefer EAFP in Python.

---

**Author’s note:** Happy coding!
