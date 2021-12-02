
import time


# 使用方法一: tqdm
from tqdm import trange
for i in trange(3):
    #do something
    time.sleep(1)
    pass

# 使用方法二: trange
from tqdm import tqdm
for i in tqdm(range(3)):
     #do something
     time.sleep(1)
     pass

# 使用方法三: 手动方法
import tqdm
bar = tqdm(["a", "b", "c", "d"])
for char in bar:
    time.sleep(1)
    bar.set_description("Processing %s" % char)