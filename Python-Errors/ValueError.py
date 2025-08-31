# Raqamga aylantirishda noto‘g‘ri belgi bor -> ValueError.
# Invalid literal when converting to int -> ValueError.
int("12a")


# Manfiy sonning ildizi (math) haqiqiy sonlar sohasi uchun taqiqlangan -> ValueError.
# Square root of a negative number in math domain -> ValueError.
import math
math.sqrt(-1)


# Sana formatiga mos bo'lmagan oy (13) -> ValueError.
# Month out of range (13) for the given date format -> ValueError.
from datetime import datetime
datetime.strptime("2025-13-01", "%Y-%m-%d")


# Ro'yxatdan yo'q elementni olib tashlashga urinish -> ValueError.
# Removing a value that is not in the list -> ValueError.
items = [1, 2, 3]
items.remove(4)


# range() da step = 0 bo'lishi mumkin emas -> ValueError.
# range() step cannot be zero -> ValueError.
list(range(0, 10, 0))