# 1) Musbat bo‘lishi kerak
# x musbat bo‘lishi shart, aks holda AssertionError.
# x must be positive, otherwise AssertionError.
x = -3
assert x > 0, "UZ: x musbat bo'lishi kerak | EN: x must be positive"


# 2) Parametr tekshiruvi (tur va qiymat)
# factorial faqat n >= 0 bo‘lgan butun son qabul qiladi.
# factorial accepts only non-negative integers.
def factorial(n):
    assert isinstance(n, int), "UZ: n butun son bo'lsin | EN: n must be int"
    assert n >= 0, "UZ: n manfiy bo'lmasin | EN: n must be non-negative"
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out

factorial(3.5)  # AssertionError


# 3) Bo'sh ro'yxatga taqiqlash
# items bo'sh bo'lmasligi kerak; bo'sh bo'lsa ishlashni to'xtatamiz.
# items must not be empty; stop early if it is.
items = []
assert len(items) > 0, "UZ: ro'yxat bo'sh | EN: list is empty"
first = items[0]  # bu satrga yetmaydi


# 4) Nolga bo‘lishdan oldin tekshiruv
# maxraj 0 bo'lmasligi kerak.
# denominator must not be zero.
num, den = 10, 0
assert den != 0, "UZ: maxraj 0 bo'lmasin | EN: denominator must not be 0"
result = num / den


# 5) Oddiy email formatini tekshirish
# Juda sodda validatsiya: '@' va keyin nuqta borligini tekshiradi.
# Very simple validation: checks '@' and a dot in the domain part.
email = "userexample.com"
assert ("@" in email and "." in email.split("@")[-1]), \
       "UZ: email noto'g'ri | EN: invalid email format"