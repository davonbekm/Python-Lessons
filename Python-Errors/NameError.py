# E'lon qilinmagan o'zgaruvchini chaqiryapmiz -> NameError.
# Referencing an undefined variable -> NameError.
print(good_news)  # Error: NameError: name 'good_news' is not defined


# addd nomli funksiya yo'q (xato nom) -> NameError.
# Calling a function that doesn't exist (typo) -> NameError.
def add(a, b): 
    return a + b

result = addd(2, 3)  # Error: NameError: name 'addd' is not defined


# 'math' modulini import qilmasdan ishlatish -> NameError.
# Using 'math' without importing it -> NameError.
# import math  # <-- kerak edi, lekin yo'q
math.sqrt(9)  # Error: NameError: name 'math' is not defined