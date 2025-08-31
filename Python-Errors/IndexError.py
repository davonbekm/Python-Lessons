# Ro'yxat chegarasidan tashqaridagi indeksga murojaat -> IndexError.
# Accessing a list index beyond its range -> IndexError.
items = ["a", "b", 1]
items[3]  # listda oxirgi indeks 2, 3 yo'q


# Satr (string) uzunligidan katta indeks so'raldi -> IndexError.
# Requesting a string index beyond its length -> IndexError.
s = "abc"
s[5]


# Bo'sh ro'yxatdan pop() qilishga urinish -> IndexError.
# Calling pop() on an empty list -> IndexError.
stack = []
stack.pop()