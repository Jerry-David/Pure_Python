import time


def print_one_by_one(line, end="\n"):
    for i in range(len(line)):
        print("\r" + line[0: i + 1], end="")
        time.sleep(0.05)
    print(end=end)
