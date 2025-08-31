# Python xatoliklari: qisqa qoʻllanma (+ English commentary)

Python’dagi xatoliklarni ikkiga bo‘lish qulay: **syntax xatoliklari** (kodni umuman ishlatmaydi) va **runtime istisnolari** (kod ishlayotganda yuzaga keladi). Quyida har bir turga sodda misollar, **to‘g‘rilash yo‘llari**, va yonida **English izohlar** bilan ketma-ket ko‘rsataman.

*EN: We’ll group problems into “Syntax errors” (caught before the code runs) and “Runtime exceptions” (raised while running). Each section includes quick fixes and English notes.*

---

## 1) SyntaxError (shu jumladan IndentationError)

### 1.1. Yopilmagan satr (EOL while scanning string literal)
```python
message = "Hello world
print(message)
```
**Nima bo‘ldi?** Satr yopilmagan.  
**To‘g‘rilash:**
```python
message = "Hello world"
print(message)
```

*EN: A missing closing quote triggers a SyntaxError before execution. Always check matching quotes.*

---

### 1.2. Kutilmagan EOF (EOF while parsing)
```python
def add(a, b):
    return a + b

result = add(1, 2  # yopuvchi qavs qolib ketgan
```
**To‘g‘rilash:**
```python
result = add(1, 2)
```

*EN: An unmatched parenthesis at the end of the file produces “unexpected EOF”.*

---

### 1.3. IndentationError (joy tashlash noto‘g‘ri)
```python
def greet():
print("Hi")   # noto‘g‘ri joy tashlash
```
**To‘g‘rilash:**
```python
def greet():
    print("Hi")
```

*EN: Python uses indentation to define blocks. Mixed tabs/spaces or wrong levels cause IndentationError.*

---

## 2) Runtime Exceptions (kod ishga tushganda)

### 2.1. TypeError
**Misol 1:** tur aralashmasi
```python
x = 1 + '2'   # raqam + satr mumkin emas
```
**To‘g‘rilash:**
```python
x = 1 + int('2')  # yoki str(1) + '2'
```

*EN: Add numbers to numbers, strings to strings. Convert explicitly.*

**Misol 2:** “callable” emas
```python
nums = [1, 2, 3]
nums(0)   # ro‘yxatni funksiya kabi chaqirib bo‘lmaydi
```
**To‘g‘rilash:**
```python
nums[0]
```

*EN: Lists are subscriptable (`[]`), not callable (`()`).*

---

### 2.2. NameError
**Misol 1:** nom aniqlanmagan
```python
print(good_news)   # bunday o‘zgaruvchi yo‘q
```
**To‘g‘rilash:**
```python
good_news = "All is well"
print(good_news)
```

*EN: You referenced a variable before defining it.*

**Misol 2:** noto‘g‘ri funksiya nomi
```python
def add(a, b): return a + b
result = addd(2, 3)   # adashib yozildi
```
**To‘g‘rilash:**
```python
result = add(2, 3)
```

*EN: Typos in identifiers lead to NameError.*

---

### 2.3. ValueError
**Misol 1:** noto‘g‘ri qiymat
```python
int("12a")
```
**To‘g‘rilash:**
```python
int("12")   # yoki xatoni ushla:
# try:
#     int("12a")
# except ValueError:
#     ...
```

*EN: The type is correct (string → int), but the *value* isn’t parsable.*

**Misol 2:** matematik taqiqlangan qiymat
```python
import math
math.sqrt(-1)
```
**To‘g‘rilash:**
```python
# Komleks ildiz uchun:
import cmath
cmath.sqrt(-1)
```

*EN: `math.sqrt()` doesn’t accept negative numbers; use `cmath` for complex results.*

---

### 2.4. IndexError
**Misol 1:** indeks diapazondan tashqarida
```python
items = ["a", "b", 1]
items[3]   # 0..2 mavjud, 3 yo‘q
```
**To‘g‘rilash:**
```python
items[-1]  # oxirgi element
# yoki indeksni tekshirish
```

*EN: Always ensure the index is within bounds.*

**Misol 2:** bo‘sh ro‘yxatdan `pop()`
```python
[].pop()
```
**To‘g‘rilash:**
```python
stack = []
if stack:
    stack.pop()
```

*EN: Popping from an empty list raises IndexError.*

---

### 2.5. ZeroDivisionError
**Misol 1:**
```python
10 / 0
```
**Misol 2:**
```python
nums = []
avg = sum(nums) / len(nums)
```
**To‘g‘rilash:**
```python
nums = []
avg = (sum(nums) / len(nums)) if nums else 0.0  # yoki None
```

*EN: Guard against zero denominators before dividing.*

---

### 2.6. Logic Errors (xato natija, lekin istisno yo‘q)

**Misol 1:** `is` o‘rniga `==`
```python
a = "ab"
b = "".join(["a", "b"])

print(a is b)   # noto‘g‘ri: identiklikni tekshiradi
print(a == b)   # to‘g‘ri: qiymat tengligini tekshiradi
```

*EN: `is` checks object identity, `==` checks value equality.*

**Misol 2:** noto‘g‘ri o‘rtacha
```python
nums = [10, 20, 30]
avg = sum(nums) / len(nums + 1)  # noto‘g‘ri
```
**To‘g‘rilash:**
```python
avg = sum(nums) / len(nums)
```

*EN: Don’t modify the list when computing its length.*

---

### 2.7. KeyError
**Misol 1:** mavjud bo‘lmagan kalit
```python
user = {"id": 1}
user["name"]   # KeyError
```
**To‘g‘rilash:**
```python
user.get("name")  # None qaytaradi yoki default bering
```

*EN: `.get()` avoids KeyError and returns a default instead.*

**Misol 2:** hisoblagichni oshirish
```python
counts = {}
k = "apple"
counts[k] += 1   # KeyError (k hali yo‘q)
```
**To‘g‘rilash 1 (get):**
```python
counts[k] = counts.get(k, 0) + 1
```
**To‘g‘rilash 2 (setdefault):**
```python
counts.setdefault(k, 0)
counts[k] += 1
```
**To‘g‘rilash 3 (defaultdict):**
```python
from collections import defaultdict
counts = defaultdict(int)
counts[k] += 1
```
**To‘g‘rilash 4 (Counter):**
```python
from collections import Counter
counts = Counter()
counts[k] += 1
counts.update([k])
```

*EN: `get`, `setdefault`, `defaultdict`, and `Counter` are idiomatic for frequency counting.*

---

### 2.8. FileNotFoundError
**Misollar:**
```python
open("main.txt", "r")
```
```python
from pathlib import Path
Path("main.json").read_text(encoding="utf-8")
```
**To‘g‘rilash:**
```python
from pathlib import Path
p = Path("main.txt")
if p.exists():
    print(p.read_text(encoding="utf-8"))
else:
    print("File topilmadi")
```

*EN: Check existence or handle with `try/except`.*

---

### 2.9. PermissionError
**Misollar (Linux/macOS):**
```python
open("/root/data/main.py", "w")   # odatda ruxsat yo‘q
open("readonly.txt", "w")         # fayl read-only bo‘lsa
```
**Yechim:**
- Ruxsatlarni to‘g‘rilash (`chmod`, OS darajasida).
- To‘g‘ri joyga yozish (foydalanuvchi katalogi va h.k.).
- `try/except PermissionError` bilan ishlash.

*EN: This arises from the OS. Fix file permissions or choose a writable path.*

---

### 2.10. TimeoutError
**Misol 1 (qo‘l bilan ko‘tarish):**
```python
import time
start = time.time()
while True:
    if time.time() - start > 1.0:
        raise TimeoutError("Waited 1 second, no result")
```

**Misol 2 (`asyncio.wait_for`):**
```python
import asyncio

async def work():
    await asyncio.sleep(2)

asyncio.run(asyncio.wait_for(work(), timeout=0.5))
```

*EN: In async code, wrap awaited tasks with `asyncio.wait_for` to enforce deadlines.*

---

### 2.11. ConnectionError (tarmoqqa oid)
**Socket misoli (ConnectionRefusedError):**
```python
import socket
s = socket.socket()
s.connect(("127.0.0.1", 1))  # ehtimol rad etiladi (past port)
```

**`requests` misoli (kutubxona istisnosi):**
```python
import requests
requests.get("http://localhost:9999")  # requests.exceptions.ConnectionError
```

*EN: Low-level sockets raise `ConnectionRefusedError`/`TimeoutError` (subclasses of `OSError`).
`requests` raises its own `requests.exceptions.ConnectionError`. Handle accordingly.*

---

### 2.12. AssertionError
**Misol 1:**
```python
x = -3
assert x > 0, "x must be positive"
```

**Misol 2:**
```python
den = 0
assert den != 0, "Denominator must not be 0"
```

*EN: Assertions are for internal invariants in development/tests. Don’t rely on them for user-facing validation (they can be disabled with `-O`). Use explicit checks and raise proper exceptions in production code.*

---

## Qanday ushlash va toza tutish?

**Try/Except bilan aniq ushlang:**
```python
try:
    n = int(input_str)
except ValueError as e:
    # EN: Tell the user what went wrong and how to fix it.
    print("Raqam kiriting, masalan: 42")
```

**Bir nechta tur uchun:**
```python
try:
    avg = sum(nums) / len(nums)
except ZeroDivisionError:
    avg = 0.0
except TypeError:
    nums = list(nums)  # yoki ma’lumotni tozalash
    avg = sum(nums) / len(nums)
```

**O‘zingizning istisnoyingizni yarating:**
```python
class ConfigError(Exception):
    pass

def load_config(path):
    if not path.exists():
        raise ConfigError(f"Config yo‘q: {path}")
```

*EN: Catch only what you can handle, be specific, and surface helpful messages. Prefer custom exceptions for domain-specific problems.*

---

## Qisqa xulosa

- **SyntaxError/IndentationError**: kod *boshlanmasdan* oldin ushlanadi — qavslar, qo‘shtirnoqlar, joy tashlashni tekshiring.  
- **Runtime Exceptions**: ish davomida yuzaga keladi — `TypeError`, `ValueError`, `IndexError`, `ZeroDivisionError`, `KeyError`, `FileNotFoundError`, `PermissionError`, `TimeoutError`, `ConnectionError`, va hokazo.  
- **Logic Errors**: istisno yo‘q, lekin natija noto‘g‘ri — testlar, `assert` (dev), va kod ko‘rib chiqish bilan tuting.  
- **Yaxshi odatlar**: aniq `try/except`, foydali xabarlar, kerak bo‘lsa `defaultdict`/`Counter`, va `requests` kabi kutubxonalar istisnolarini alohida ko‘rib chiqing.

*EN: Keep errors informative, handle only what you can fix, and write tests to prevent logic bugs from slipping through.*