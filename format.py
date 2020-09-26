# 用%格式化字符串
print("用%格式化字符串", end="\n\n")
print("你好%s世界%s" % ("，", "！"))
print("我今年%d岁了。" % 12)
print("我今年%04d岁了。" % 12)
print("我今天长高了%.2f厘米" % 8.367)
print("我今天长高了%.4f厘米" % 8.367)


print("\n\n\n")


# 用format格式化字符串
print("用format格式化字符串", end="\n\n")
print("你好{}世界{}".format("，", "！"))
print("我今年{}岁了。".format(12))
print("我今天长高了{}厘米".format(8.367))
