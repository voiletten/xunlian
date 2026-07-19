import time
import threading
import asyncio

async def greeting(name,delay):

    await asyncio.sleep(delay)
    print(f"hello{name}")
    return name


async def main():
    start = time.time()
    list1 = await asyncio.gather(greeting("Alice", 1),greeting("Bob", 2),greeting("Carol", 3))
    print(list1)
    end = time.time()
    print(f"总时间:{end-start}")


asyncio.run(main())












