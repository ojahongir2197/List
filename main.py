# List tushunchai

# 1
a = [10, 20, 30, 40]
print(len(a))

# 2
a = [5, 8, 12, 7]
print(a)

# 3
mevalar = ["olma", "anor", "uzum"]
print(mevalar)

# 4
sonlar = [1, 2, 3, 4, 5]
print(sonlar[-1])

# 5
a = [11, 22, 33]
print(a[0])


# List yaratish usullari
# 1
a = list((1, 2, 3, 4))
print(a)

# 2
a = [10, 20, 30]
a.append(40)
print(a)

# 3
davlatlar = ["Uzbekistan", "Kazakhstan"]
davlatlar.append("Kyrgyzstan")
print(davlatlar)

# 4
a = [7, 8, 9]
print(len(a))

# 5
a = [1, 2, 3, 4]
for son in a:
    print(son)


# List elementlariga murojaat qilish

# 1
a = [5, 10, 15, 20]
print(a[1])

# 2
a = [4, 6, 8, 10]
print(a[2])

# 3
a = [9, 8, 7, 6]
print(a[-1])

# 4
a = [1, 2, 3, 4, 5]
print(a[1:3])

# 5
a = [100, 200, 300]
a[0] = 500
print(a)
