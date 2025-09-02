
"""
O'zbekcha:
  Mavzu: raise va 'from e' bilan zanjirlash.
  Xatolik turlari: ValueError (parsingda).
  Qayerda ishlatish: Pastki qatlam xatosini yuqori qatlamga ma'noli xabar bilan ko'tarish.

English:
  Topic: raise and chaining with 'from e'.
  Error types: ValueError (during parsing).
  When to use: Re-throwing lower-level errors with a clearer, domain-specific message.
"""

def parse_age(text: str) -> int:
    try:
        return int(text)
    except ValueError as e:
        # UZ: Foydalanuvchiga aniqroq xabar; asl sabab e bilan zanjirlash
        # EN: Clearer message for users; keep original cause with 'from e'
        raise ValueError(f"UZ: Yosh noto'g'ri formatda: {text!r}  EN: Age is not correct format: {text!r}") from e

if __name__ == "__main__":
    for sample in ["12", "12a"]:
        try:
            print("Input:", sample, "=>", parse_age(sample))
        except ValueError as e:
            print("Caught:", e)
