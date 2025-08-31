# 1) Mavjud bo'lmagan faylni o'qish uchun ochish -> FileNotFoundError.
#    Opening a non-existent file for reading -> FileNotFoundError.
open("main.txt", "r")

# # Safer:
# try:
#     with open("main.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("Fayl topilmadi | File not found")


# 2) Yo'lda mavjud bo'lmagan faylni Path.read_text() bilan o'qish -> FileNotFoundError.
#    Using Path.read_text() on a missing file -> FileNotFoundError.
from pathlib import Path
Path("configs/settings.json").read_text(encoding="utf-8")

# # Safer:
# p = Path("configs/settings.json")
# if p.exists():
#     print(p.read_text(encoding="utf-8"))
# else:
#     print("Fayl yo'q | File does not exist")


# 3) Mavjud bo'lmagan faylni o'chirishga urinish -> FileNotFoundError.
#    Trying to delete a missing file -> FileNotFoundError.
import os
os.remove("tmp/output.log")

# # Safer:
# if os.path.exists("tmp/output.log"):
#     os.remove("tmp/output.log")
# else:
#     print("O'chirish uchun fayl topilmadi | Nothing to delete, file not found")