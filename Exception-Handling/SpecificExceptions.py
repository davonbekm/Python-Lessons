
"""
  Mavzu: Aniq turdagi xatolarni ushlash (KeyError, ValueError) va keng guard.
  Xatolik turlari: KeyError (lug'at kaliti yo'q), ValueError (noto'g'ri format).
  Qayerda ishlatish: Lug'atdan o'qish, format/parsing, yuqori qatlamda broad guard.

  Topic: Catching specific exceptions (KeyError, ValueError) and a broad guard.
  Error types: KeyError (missing dict key), ValueError (invalid format).
  When to use: Dict access, format/parsing; use broad guard only at top boundaries.
"""

data = {"age2": "25"}  # UZ: Ataylab 'age' emas, 'age2' qildik (KeyError ko'rish uchun)
                       # EN: Intentionally different key to trigger KeyError

try:
    age = int(data["age"])   # KeyError here
except KeyError:
    print("UZ: Kalit topilmadi (KeyError).  EN: Key not found (KeyError).")
except ValueError:
    print("UZ: Yosh butun son bo'lishi kerak (ValueError).  EN: Age must be an integer (ValueError).")
except Exception as e:
    # UZ: Juda keng; faqat yuqori qatlamda "guard" sifatida ishlatish tavsiya etiladi
    # EN: Very broad; recommended only as a top-level guard
    print("UZ: Noma'lum xato.  EN: Unexpected error.", e)
    raise
else:
    print("UZ: Hammasi joyida:  EN: Everything is OK:", age)
finally:
    print("UZ: Tozalash.  EN: Cleanup.")
