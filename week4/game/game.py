"""
import random
# 1. 随机整数 (1~10)
rand_int = random.randint(1, 10)
# 2. 随机小数 (0~1)
rand_float = random.random()
# 3. 区间随机小数 (1.0~5.0)
rand_uniform = random.uniform(1.0, 5.0)
# 4. 从列表中随机选一个
items = ["A", "B", "C"]
chosen = random.choice(items)
# 5. 从列表中随机选多个 (不重复)
samples = random.sample(items, 2)
# 6. 打乱列表顺序
random.shuffle(items)
"""
import random
while True:
    try:
        level=int(input("Level: "))
        if level>1:break
    except ValueError:pass
result=random.randint(1,level)
while True:
    try:
        say=int(input("Guess: "))
        if say==result:
            print("Just right!")
            break
        elif say<result:print("Too small!")
        elif say>result:print("Too large!")
    except ValueError:pass