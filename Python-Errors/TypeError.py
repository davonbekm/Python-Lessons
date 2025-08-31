# 1) int va str qo‘shib bo‘lmaydi.
#    Cannot add int and str.
x = 1 + "2"

# 2) Ro‘yxat (list) "callable" emas, funksiya kabi chaqirib bo‘lmaydi.
#    List object is not callable.
nums = [1, 2, 3]
nums(0)

# 3) None indekslab bo‘lmaydi — subscriptable emas.
#    NoneType is not subscriptable.
a = None
a[0]

# 4) int iterable emas — for siklida aylantirib bo‘lmaydi.
#    int is not iterable.
for ch in 123:
    pass

# 5) len(int) — uzunlik faqat kolleksiyalarda bor.
#    len() works on collections, not on int.
len(10)

# 6) Lug‘at kaliti hashable bo‘lishi kerak; list hashable emas.
#    Dict keys must be hashable; list is unhashable.
d = {}
d[[1, 2]] = "x"

# 7) Qatorni (str) faqat butun son (int) ga ko‘paytirish mumkin, float ga emas.
#    Can multiply a string by int, not by float.
"a" * 2.5

# 8) Slice indekslari int/None bo‘lishi kerak; float mumkin emas.
#    Slice indices must be integers or None.
lst = [1, 2, 3]
lst[0:1.5]

# 9) Funksiyaga noto‘g‘ri argumentlar soni/type berildi.
#    Wrong number/type of function arguments.
def add(a, b): 
    return a + b

add(1)        # yetishmaydi
# add(1, 2, 3)  # ortiqcha

# 10) join faqat satrlar ketma-ketligiga ishlaydi; int borligi xato.
#     join expects an iterable of strings; ints cause TypeError.
",".join([1, 2, 3])