# Nolga bo‘lish — ruxsat etilmaydi -> ZeroDivisionError.
# Division by zero is not allowed -> ZeroDivisionError.
10 / 0


# Bo'sh ro'yxatning o'rtacha qiymati: len(nums) = 0 bo'lgani uchun nolga bo'linadi.
# Average of an empty list: len(nums) = 0, causing division by zero.
nums = []
avg = sum(nums) / len(nums)