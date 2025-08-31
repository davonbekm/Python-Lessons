# 1) Identity vs Equality (is vs ==)
# 'is' obyektning bir xilligi (identifikatori) ni tekshiradi, qiymat tengligini emas.
# 'is' checks object identity, not value equality.

# Noto'g'ri / Wrong
a = "ab"
b = "".join(["a", "b"])
print(a is b)   # ko'pincha False; qiymatlar teng bo'lsa ham
# often False even though values are equal

# To'g'ri / Correct
print(a == b)   # True (qiymatlar teng) / values are equal


# 2) O'rtacha (average) hisobida noto'g'ri maxraj
# (len(nums) + 1) qo'yib yuborish matematik xato.
# Using (len(nums) + 1) in the denominator is a math bug.

# Noto'g'ri / Wrong
nums = [10, 20, 30]
avg = sum(nums) / (len(nums) + 1)  # 60 / 4 = 15 (xato)
print(avg)

# To'g'ri / Correct
avg = sum(nums) / len(nums)        # 60 / 3 = 20 (to'g'ri)
print(avg)


# 3) Off-by-one xatosi (range chegaralari)
# 1 dan N gacha yig'indi deyapmiz, lekin N ni kiritmayapmiz.
# Summing 1..N but accidentally exclude N.

# Noto'g'ri / Wrong
N = 10
total = sum(range(1, N))  # faqat 1..9 ni qo'shadi => 45
print(total)

# To'g'ri / Correct
total = sum(range(1, N + 1))  # 1..10 => 55
print(total)


# 4) Raqamlar satr ko'rinishida leksikografik saralanishi
# "10" < "2" bo'lib qoladi; raqam sifatida saralash kerak.
# Sorting numeric strings lexicographically ("10" < "2") is wrong.

# Noto'g'ri / Wrong
scores = ["2", "10", "1"]
print(sorted(scores))  # ['1', '10', '2'] (xato ma'no)

# To'g'ri / Correct
print(sorted(scores, key=int))  # ['1', '2', '10'] (raqam sifatida)


# 5) Floating nuqtali tenglikni bevosita tekshirish
# 0.1 + 0.2 ning aniqligi tufayli to'g'ridan-to'g'ri 0.3 ga teng bo'lmasligi mumkin.
# 0.1 + 0.2 may not equal 0.3 exactly due to floating-point precision.

# Noto'g'ri / Wrong
if 0.1 + 0.2 == 0.3:
    print("OK")
else:
    print("Not equal (bu kutilmagan)")

# To'g'ri / Correct
import math
if math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-09, abs_tol=0.0):
    print("OK (isclose bilan)")