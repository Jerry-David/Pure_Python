import random
import os
from print_one_by_one import print_one_by_one as pobo  # type: ignore


def is_the_number_right(guess_number, true_number, out=print):
    """判断用户猜测的数字是否正确"""
    if guess_number == true_number:
        out("恭喜您，猜对啦！")
    elif guess_number > true_number:
        out("您猜得太大啦！")
        out("请输入您再次猜测的数字（1~100）：", end="")
        guess_number = int(input(""))
        is_the_number_right(guess_number, true_number, out)
    elif guess_number < true_number:
        out("您猜得太小啦！")
        out("请输入您再次猜测的数字（1~100）：", end="")
        guess_number = int(input(""))
        is_the_number_right(guess_number, true_number, out)


pobo("欢迎来到《猜数字》游戏!")
while True:
    number = random.randint(1, 100)
    pobo("请输入您猜测的数字（1~100）：", end="")
    guess_number = int(input(""))
    is_the_number_right(guess_number, number, pobo)
    pobo("您还想再玩一次吗(y, n)?", end="")
    answer = input("")
    if answer == "y":
        os.system("clear")
        continue
    else:
        pobo("再见！")
        break
