
"""
O'zbekcha:
  Mavzu: Maxsus (custom) exception yaratish.
  Xatolik turlari: DomainError (biznes qoidasi buzilganda).
  Qayerda ishlatish: Biznes qoidalari, validatsiya.

English:
  Topic: Creating a custom exception.
  Error types: DomainError (when business rule is violated).
  When to use: Business rules and validations.
"""

class DomainError(Exception):
    """UZ: Biznes qoidasi buzilganda.  EN: Raised when a business rule is violated."""
    pass

def buy_ticket(age: int):
    if age < 0:
        # UZ: Ma'noli, domen-ga mos xato
        # EN: Meaningful, domain-specific error
        raise DomainError("UZ: Yosh manfiy bo'lishi mumkin emas.  EN: Age cannot be negative.")
    return age

if __name__ == "__main__":
    for a in [25, -3]:
        try:
            print("age:", a, "=>", buy_ticket(a))
        except DomainError as e:
            print("Caught:", e)
