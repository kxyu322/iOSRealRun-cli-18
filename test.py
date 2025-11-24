import asyncio

async def worker(name):
    print(f"[{name}] start")           # ①
    result = await io_task(name)       # ②
    print(f"[{name}] got {result}")    # ⑤
    return result * 10                 # ⑥

async def io_task(who):
    print(f"  <io {who}> open")        # ③
    await asyncio.sleep(1)             # ④
    print(f"  <io {who}> close")       # ④’
    return 42

async def main():
    # create_task 立即返回 Task；并发运行两个 worker
    t1 = asyncio.create_task(worker("A"))
    t2 = asyncio.create_task(worker("B"))
    out = await asyncio.gather(t1, t2) # ⑦
    print("main got:", out)            # ⑧

asyncio.run(main())