from cmath import sqrt
from datetime import datetime
import threading
import asyncio
import time
def seq(name,age):
    print("正在分析，请稍后")
    time.sleep(1)
    print(f"{name}你好，{age}岁")

async def a_seq(name,age):
    print("正在分析，请稍后")
    await asyncio.sleep(1)
    print(f"{name}你好，{age}岁")


tasks = [
    ("alice",15),
    ("bob",16),
    ("candy",18),
    ("david",20),
    ("eric",22)
]

#chuan
start1 = time.time()
for i in tasks:
    seq(i[0],i[1])
end1 = time.time()

#sync
start2 = time.time()
threads = [threading.Thread(target=seq,args=i) for i in tasks]
for t in threads:
    t.start()
for t in threads:
    t.join()
end2 = time.time()
#async


start3 = time.time()
async def main():
     await asyncio.gather(*[a_seq(x,y) for x,y in tasks])
asyncio.run(main())
end3 = time.time()
print(f"串行时间{end1-start1}，并行{end2-start2}，异步时间{end3-start3}")

