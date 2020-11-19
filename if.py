username = input("请输入用户名：").strip().lower()
if username == "admin":
    print("欢迎您，管理员！")
elif username:  # 等同于 elif username != "":
    print("您好，%s！" % username.title())
    age = int(input("请问您的年龄是："))
    if (age > 5) and (age < 16):
        print("欢迎您参赛！")
    else:
        print("对不起，您的年龄尚不满足参赛年龄！")
else:
    print("对不起，用户名不能为空哦！")
