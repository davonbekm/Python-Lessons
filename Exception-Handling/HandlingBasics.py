
"""
  Mavzu: Asosiy oqim — try / except / else / finally
  Xatolik turlari: ValueError (inputni int ga o‘girayotganda), lekin naqsh umumiy.
  Qayerda ishlatish: Foydalanuvchi kiritmalari, oddiy parsing, kichik riskli bloklar.

  Topic: Core flow — try / except / else / finally
  Error types: ValueError (when casting input to int), but the pattern is general.
  When to use: User inputs, simple parsing, small risky blocks.
"""

def main():
    try:
        # UZ: Foydalanuvchi raqam kiritadi, int() ValueError berishi mumkin
        # EN: User enters a number, int() may raise ValueError
        risk = int(input("Enter a number (raqam kiriting): "))
    except ValueError as e:
        print("UZ: Iltimos butun son kiriting.  EN: Please enter an integer.", e)
    else:
        # UZ: Faqat xato bo'lmasa ishlaydi
        # EN: Runs only if no exception occurred
        print("UZ: Muvaffaqiyatli:", risk, "  EN: Successfully:", risk)
    finally:
        # UZ: Har doim ishlaydi (tozalash/yopish uchun)
        # EN: Always runs (for cleanup/closing)
        print("UZ/EN: Final code (always).")

if __name__ == "__main__":
    main()
