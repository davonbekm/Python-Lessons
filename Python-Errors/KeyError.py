# 1) Lug'atda mavjud bo'lmagan kalitni o'qish -> KeyError.
# Accessing a missing dictionary key -> KeyError.
user = {"id": 1}
user["name"]  # KeyError: 'name'

# # To'g'ri (safer):
# user.get("name")             # -> None (yoki default)
# user.get("name", "No name")  # -> "No name"


# 2) Hisoblagichni boshlamasdan += 1 qilish -> KeyError.
# Incrementing a counter without initializing -> KeyError.
counts = {}
k = "apple"
counts[k] += 1  # KeyError: 'apple'

# # To'g'ri (safer):
# counts[k] = counts.get(k, 0) + 1
# counts.setdefault(k, 0); counts[k] += 1
# from collections import defaultdict
# d = defaultdict(int); d[k] += 1


# 3) pop() da default bermasdan yo'q kalitni olish -> KeyError.
# dict.pop() on a missing key without a default -> KeyError.
data = {"a": 1}
data.pop("b")  # KeyError: 'b'

# # To'g'ri (safer):
# data.pop("b", None)  # -> None (xato o'rniga default qaytaradi)


# 4) Muhit o'zgaruvchisini (env var) mavjud emas holatda o'qish -> KeyError.
# Reading a missing environment variable -> KeyError.
import os
os.environ["MISSING_ENV_VAR_12345"]  # KeyError: 'MISSING_ENV_VAR_12345'

# # To'g'ri (safer):
# os.environ.get("MISSING_ENV_VAR_12345")          # -> None
# os.environ.get("MISSING_ENV_VAR_12345", "default")


# 5) str.format() da mavjud bo'lmagan kalitdan foydalanish -> KeyError.
# Using a missing named field in str.format() -> KeyError.
"{name} is {age}".format(age=30)  # KeyError: 'name'

# # To'g'ri (safer):
# "{name} is {age}".format(name="Ali", age=30)