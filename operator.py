num_1 = 15
num_2 = 20
my_name = "Jerry"
your_name = my_name
age = 12
marry_ago = False
marry_now = not marry_ago

# 赋值运算符
print("赋值运算符", end="\n\n")
print(id(my_name), my_name)
print(id(your_name), your_name)
print(id(age), age)

print("\n\n")

# 算数运算符
print("算数运算符", end="\n\n")
print("%d + %d = %d" % (num_1, num_2, num_1 + num_2))
print("%d - %d = %d" % (num_1, num_2, num_1 - num_2))
print("%d * %d = %d" % (num_1, num_2, num_1 * num_2))
print("%d / %d = %d" % (num_1, num_2, num_1 / num_2))
print(str(num_1) + " % " + str(num_2) + " = " + str(num_1 % num_2))
print("%d ** %d = %d" % (num_1, num_2, num_1**num_2))
print("%d // %d = %d" % (num_1, num_2, num_1 // num_2))

print(end="\n\n")

# 关系运算符
print("关系运算符", end="\n\n")
print("%s == %s: %s" % (num_1, num_2, num_1 == num_2))
print("%s != %s: %s" % (num_1, num_2, num_1 != num_2))
print("%s >= %s: %s" % (num_1, num_2, num_1 >= num_2))
print("%s <= %s: %s" % (num_1, num_2, num_1 <= num_2))
print("%s > %s: %s" % (num_1, num_2, num_1 > num_2))
print("%s < %s: %s" % (num_1, num_2, num_1 < num_2))
print("%s is %s: %s" % (num_1, num_2, num_1 is num_2))
print("%s is not %s: %s" % (num_1, num_2, num_1 is not num_2))

print(end="\n\n")

# 逻辑运算符
print("逻辑运算符", end="\n\n")
print("(%s > %s) and (%s < %s) : %s" % (num_1, num_2, num_1, num_2,
                                        (num_1 > num_2) and (num_1 < num_2)))
print("(%s > %s) or (%s < %s) : %s" % (num_1, num_2, num_1, num_2,
                                       (num_1 > num_2) or (num_1 < num_2)))
print("%s = not %s" % (marry_ago, marry_now))

print(end="\n\n")

# 位运算
print("位运算", end="\n\n")
print(bin(3))
print(int(0b11))
print(int(0o75))
print(int(0x3f))

print(r"3 & 2: " + str((3 & 2)))
print(r"3 | 2: " + str((3 | 2)))
print(r"~3: " + str((~3)))
print(r"3 ^ 2: " + str((3 ^ 2)))
print(r"3 << 1: " + str((3 << 1)))
print(r"2 >> 1: " + str((2 >> 1)))
"""
运算图示：

&:
1 True  0 False
   0000 0011 (3)
   0000 0010 (2)
--------------
   0000 0010 (2)

|:
1 True  0 False
   0000 0011 (3)
   0000 0010 (2)
--------------
   0000 0011 (3)

~:
1 True  0 False
   0000 0011 (3)
--------------
   1111 1100 (-3)
-          1
--------------
   1111 1011 (-4)

^:
1 True  0 False
   0000 0011 (3)
   0000 0010 (2)
--------------
   0000 0001 (2)

<<:
1 True  0 False
   0000 0011 (3)
<<         1
--------------
   0000 0110 (6)

>>:
1 True  0 False
   0000 0010 (2)
>>         1
--------------
   0000 0001 (1)
"""

# 三目表达式
print("三目表达式", end="\n\n")

a = 6
b = 5
print(a + b) if a > b else print(b - a)
a = 5
b = 6
print(a + b) if a > b else print(b - a)
