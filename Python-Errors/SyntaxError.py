# SyntaxError


# If dan keyin ikki nuqta (:) yo‘q — sintaksis noto‘g‘ri.
# Missing colon (:) after if — invalid syntax.
if True
    print("hi")

# Yopilmagan qavs — ifoda tugallanmagan.
# Unclosed parenthesis — the expression is incomplete.
print(1 + (2 * 3

# Ajratilgan so‘z (keyword) 'class' ni o‘zgaruvchi nomi sifatida ishlatib bo‘lmaydi.
# Reserved keyword 'class' cannot be used as a variable name.
class = 1

# Funksiya parametrlarida non-default parametr default parametrdan keyin kelgan.
# Non-default argument follows default argument in function parameters.
def add(a=0, b):
    return a + b

# 'return' funksiyadan tashqarida yozilgan — ruxsat etilmaydi.
# 'return' outside of a function — not allowed.
return 42


# EOL while scanning string literal


# Ikki qo‘shtirnoq bilan boshlangan satr yopilmagan.
# Double-quoted string not closed before end of line.
title = "Python — EOL demo

# Yakka qo‘shtirnoq bilan boshlangan satr yopilmagan.
# Single-quoted string not closed before end of line.
name = 'Ali

# Raw string oxiri bitta teskari chiziq (\) bilan tugay olmaydi — yopilmagan satr.
# Raw string cannot end with a single backslash — string remains open.
raw_path = r"C:\Users\Davron\Desktop\"

# f-string yopilmagan (qo‘shtirnoq yetishmaydi). Ichki ifoda tugallangan bo‘lsa ham, satrning o‘zi yopilmadi.
# f-string not closed (missing closing quote). The inner expression is fine, but the string itself isn't closed.
f_line = f"result: {1 + 2}

# Bayt satr (bytes literal) yopilmagan.
# Bytes literal not closed.
bytes_text = b"ABC


# EOF while parsing


# Yopilmagan qavs — fayl oxirida parser kutayotgan joyida tugaydi.
# Unclosed parenthesis — file ends while parser still expects a ')'.
print("value:", 1 + 2

# Yopilmagan ro‘yxat (]) yetishmaydi.
# Unclosed list — missing closing ']'.
nums = [1, 2, 3

# Yopilmagan lug‘at (}) yetishmaydi.
# Unclosed dict — missing closing '}'.
user = {"id": 1, "name": "Alice"

# Uch qo‘shtirnoqli ko‘p qatorli matn yopilmagan.
# Triple-quoted multiline string not closed.
doc = """Hello,
This is a long text that never closes...

# Ko‘p qatorli ifoda ochilgan, lekin yakunlovchi qavs bilan yopilmagan.
# Multi-line parenthesized expression started but never closed.
total = (
    1 +
    2 +
    3